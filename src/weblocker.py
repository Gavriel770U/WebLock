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
        self.__window.geometry(GEOMETRY)
        self.__window.title('WebLocker')
        self.__window.config(bg="aquamarine3")
        
        self.__website_block_label = tkinter.Label(master = self.__window, text = 'Enter Website Domain: ')
        self.__website_block_label.place(x = 10, y = 100)
        
        self.__website_block_entry = tkinter.Entry(master = self.__window, width = 40, bd = 5)
        
        self.__website_block_entry.place(x = 150, y = 95)
        
        self.__submit_block_button = tkinter.Button(master = self.__window, text = 'Block Website', 
                command = self.__submit_block_button_command, bd = 5) 
        
        self.__submit_block_button.place(x = 450, y = 95)
        
        
    def __submit_block_button_command(self) -> None:
        domain = self.__website_block_entry.get()
        os.system("ipconfig /flushdns")
        self.__write_to_hosts(domain)
        os.system("ipconfig /flushdns")   
        
         
    def __write_to_hosts(self, website_url: str) -> None:
        with open(self.__hosts_path, FILE_APPEND) as hosts_file:
            hosts_file.write(NEWLINE + NEW_IP + SPACE + website_url)
    
    
    def run(self) -> None:
        self.__window.mainloop()