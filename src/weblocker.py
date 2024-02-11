import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from consts import *

class WebLocker(object):
    def __init__(self) -> None:
        if NT_OS == os.name:
            self.__hosts_path = r'C:\Windows\System32\Drivers\etc\hosts'  
        else:
            raise OSError(f'WebLocker does not support OS [{os.name}]')
        
        self.__init_graphics()
    
    
    def __init_graphics(self) -> None:
        self.__app = QApplication(sys.argv)
        self.__window = QWidget()
        self.__window.resize(WIDTH, HEIGHT)
        self.__window.setWindowTitle('WebLocker') 
        
    def __submit_block_button_command(self) -> None:
        domain = self.__website_block_entry.get()
        os.system("ipconfig /flushdns")
        self.__write_to_hosts(domain)
        os.system("ipconfig /flushdns")   
        
         
    def __write_to_hosts(self, website_url: str) -> None:
        with open(self.__hosts_path, FILE_APPEND) as hosts_file:
            hosts_file.write(NEWLINE + NEW_IP + SPACE + website_url)
    
    
    def run(self) -> None:
        self.__window.show()
        
        sys(exit(self.__app.exec()))