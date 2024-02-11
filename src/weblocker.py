import os
import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt6.QtGui import QFont
from consts import *

class WebLockerHostsManager(object):
    def __init__(self) -> None:
        if NT_OS == os.name:
            self.__hosts_path = r'C:\Windows\System32\Drivers\etc\hosts'  
        else:
            raise OSError(f'WebLocker does not support OS [{os.name}]')
        
        
    def __block_domain_windows(self) -> None:
        domain = self.__website_block_entry.get()
        os.system("ipconfig /flushdns")
        self.__write_to_hosts(domain)
        os.system("ipconfig /flushdns")
        
         
    def __write_to_hosts(self, website_url: str) -> None:
        with open(self.__hosts_path, FILE_APPEND) as hosts_file:
            hosts_file.write(NEWLINE + NEW_IP + SPACE + website_url)
    

class WebLockerWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__hosts_manager = WebLockerHostsManager()
        
        self.__initUI()
        
        
    def __initUI(self) -> None:
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('WebLocker Window Instance')

        block_website_button = QPushButton('Block Website', self)
        block_website_button.setToolTip('Click To Block A Website')
        block_website_button.clicked.connect(QApplication.instance().quit)
        block_website_button.resize(block_website_button.sizeHint())
        block_website_button.move(50, 50)

        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.setWindowTitle('WebLocker')
        self.show()

class WebLocker(object):
    def __init__(self) -> None:
        self.__init_graphics()
    
    
    def __init_graphics(self) -> None:
        self.__app = QApplication(sys.argv)
        self.__window = WebLockerWindow()
        
    
    def run(self) -> None:
        self.__window.show()
        sys(exit(self.__app.exec()))