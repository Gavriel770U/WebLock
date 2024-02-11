import os
import tkinter
from consts import *

class WebLocker(object):
    def __init__(self) -> None:
        if NT_OS == os.name:
            self.__hosts_path = r'C:\Windows\System32\Drivers\etc\hosts'  
        else:
            raise OSError(f'WebLocker does not support OS [{os.name}]')
    
        self.__window = tkinter.Tk()
        greeting = tkinter.Label(text="Hello, Tkinter")
        greeting.pack()
    
    def __write_to_hosts(self, website_url: str) -> None:
        with open(self.__hosts_path, FILE_APPEND) as hosts_file:
            hosts_file.write(NEWLINE + NEW_IP + SPACE + website_url)
    
    def run(self) -> None:
        self.__write_to_hosts('www.instagram.com')
        
        self.__window.mainloop()