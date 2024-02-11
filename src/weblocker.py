import os
import tkinter
from consts import *

class WebLocker(object):
    def __init__(self) -> None:
        if NT_OS == os.name:
            self.__hosts_path = r'C:\Windows\System32\Drivers\etc\hosts'  
        else:
            raise OSError(f'WebLocker does not support OS [{os.name}]')
        
        self.__init_graphics()
    
    def __init_graphics(self) -> None:
        self.__window = tkinter.Tk()
        self.__window.geometry('600x400')
        
        self.__website_block_entry = tkinter.Entry(master = self.__window, bd = 5)
        
        self.__website_block_entry.place(x=100, y=100)
        
        self.__submit_block_button = tkinter.Button(master=self.__window, text = 'Block Website', 
                command = self.__submit_block_button_command, bd=5) 
        
        self.__submit_block_button.place(x=400, y=100)
        
    def __submit_block_button_command(self) -> None:
        domain = self.__website_block_entry.get()
        print(domain)
        
    
    def __write_to_hosts(self, website_url: str) -> None:
        with open(self.__hosts_path, FILE_APPEND) as hosts_file:
            hosts_file.write(NEWLINE + NEW_IP + SPACE + website_url)
    
    def run(self) -> None:
        self.__write_to_hosts('www.instagram.com')
        
        self.__window.mainloop()