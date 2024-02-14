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
            if not (NEW_IP + SPACE + domain + NEWLINE == line):
                updated_data += line
        
        with open(self.__hosts_path, FILE_WRITE) as hosts_file:
            hosts_file.write(updated_data)
        
                    
    def block_domain(self, domain: str) -> None:
        if WINDOWS == platform.system():
            self.block_domain_windows(domain)
        elif LINUX == platform.system():
            self.block_domain_linux(domain)   
    
    
    def unblock_domain(self, domain: str) -> None:
        if WINDOWS == platform.system():
            self.unblock_domain_windows(domain)
        elif LINUX == platform.system():
            self.unblock_domain_linux(domain)


    def block_domain_windows(self, domain: str) -> None:
        os.system("ipconfig /flushdns")
        self.write_to_hosts(domain)
        os.system("ipconfig /flushdns")


    def unblock_domain_windows(self, domain: str) -> None:
        os.system("ipconfig /flushdns")
        self.delete_from_hosts(domain)
        os.system("ipconfig /flushdns")


    def block_domain_linux(self, domain: str) -> None:
        self.write_to_hosts(domain)


    def unblock_domain_linux(self, domain: str) -> None:
        self.delete_from_hosts(domain)
