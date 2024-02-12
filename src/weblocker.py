import os
import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QLineEdit, QApplication)
from PyQt6.QtGui import QFont
from consts import *

class WebLockerHostsManager(object):
    def __init__(self) -> None:
        self.__os = os.name
        if NT_OS == os.name:
            self.__hosts_path = r'C:\Windows\System32\Drivers\etc\hosts'  
        else:
            raise OSError(f'WebLocker does not support OS [{os.name}]')
                 

    def write_to_hosts(self, website_url: str) -> None:
        with open(self.__hosts_path, FILE_APPEND) as hosts_file:
            hosts_file.write(NEWLINE + NEW_IP + SPACE + website_url)

    
    def block_domain(self, domain: str) -> None:
        if NT_OS == os.name:
            self.block_domain_windows(domain)
    

    def block_domain_windows(self, domain: str) -> None:
        os.system("ipconfig /flushdns")
        self.write_to_hosts(domain)
        os.system("ipconfig /flushdns")
    

class WebLockerWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__hosts_manager = WebLockerHostsManager()
        
        self.__initUI()
        
        
    def __initUI(self) -> None:
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('WebLocker Window Instance')

        self.block_website_line_edit = QLineEdit(self)
        self.block_website_line_edit.setToolTip('Enter Website Domain To Block')
        self.block_website_line_edit.resize(self.block_website_line_edit.sizeHint())
        self.block_website_line_edit.setFixedWidth(150)
        self.block_website_line_edit.move(50, 50)


        self.block_website_button = QPushButton('Block Website', self)
        self.block_website_button.setToolTip('Click To Block A Website')
        self.block_website_button.clicked.connect(self.block_website)
        self.block_website_button.resize(self.block_website_button.sizeHint())
        self.block_website_button.move(250, 50)


        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.setWindowTitle('WebLocker')
        self.center()
        self.show()
    
    
    def block_website(self) -> None:
        domain = self.block_website_line_edit.text()
        print(domain)
        if domain and len(domain):
            self.__hosts_manager.block_domain(domain)
            
            
    def center(self) -> None:
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())    


class WebLocker(object):
    def __init__(self) -> None:
        self.__init_graphics()
    
    
    def __init_graphics(self) -> None:
        self.__app = QApplication(sys.argv)
        self.__window = WebLockerWindow()
        
    
    def run(self) -> None:
        self.__window.show()
        sys(exit(self.__app.exec()))