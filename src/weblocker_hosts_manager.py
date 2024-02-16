import os
import platform
from consts import *

class WebLockerHostsManager(object):
    def __init__(self) -> None:
        if WINDOWS == platform.system():
            self.__hosts_path = WINDOWS_HOSTS_PATH
        elif LINUX == platform.system():
            self.__hosts_path = LINUX_HOSTS_PATH
        else:
            raise OSError(f'WebLocker does not support OS [{platform.system()}]')
                 

    def write_to_hosts(self, domain: str) -> None:
        with open(self.__hosts_path, FILE_APPEND) as hosts_file:
            hosts_file.write(NEWLINE + NEW_IP + SPACE + domain)


    def delete_from_hosts(self, domain: str) -> None:
        updated_data = ''
        data_lines = []
        
        with open(self.__hosts_path, FILE_READ) as hosts_file:
            data_lines = hosts_file.readlines()
        
        for line in data_lines:
            if not (NEW_IP + SPACE + domain == line or NEW_IP + SPACE + domain + NEWLINE == line):
                updated_data += line
        
        with open(self.__hosts_path, FILE_WRITE) as hosts_file:
            hosts_file.write(updated_data)
    
    def windows_wrapper(self, func) -> None:
        def wrap(*args, **kwargs) -> None:
            os.system("ipconfig /flushdns")
            func(*args, **kwargs)
            os.system("ipconfig /flushdns")
        return wrap
    
    def linux_wrapper(self, func) -> None:
        def wrap(*args, **kwargs) -> None:
            func(*args, **kwargs)
        return wrap    
             
                    
    def block_domain(self, domain: str) -> None:
        if WINDOWS == platform.system():
            self.write_to_hosts = self.windows_wrapper(self.write_to_hosts)
            self.write_to_hosts(domain)
        elif LINUX == platform.system():
            self.write_to_hosts = self.linux_wrapper(self.write_to_hosts)
            self.write_to_hosts(domain)
    
    def unblock_domain(self, domain: str) -> None:
        if WINDOWS == platform.system():
            self.delete_from_hosts = self.windows_wrapper(self.delete_from_hosts)
            self.delete_from_hosts(domain)
        elif LINUX == platform.system():
            self.delete_from_hosts = self.linux_wrapper(self.delete_from_hosts)
            self.delete_from_hosts(domain)