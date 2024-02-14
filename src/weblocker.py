import os
import platform
import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QLineEdit, QLabel, QApplication)
from PyQt6.QtGui import QFont
from consts import *

class WebLockerHostsManager(object):
    def __init__(self) -> None:
        if WINDOWS == platform.system():
            self.__hosts_path = r'C:\Windows\System32\Drivers\etc\hosts'  
        elif LINUX == platform.system():
            self.__hosts_path = r'/etc/hosts'
        else:    
            raise OSError(f'WebLocker does not support OS [os module: {os.name} | platform module: {platform.system()}]')
                 

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
    

    def block_domain_windows(self, domain: str) -> None:
        os.system("ipconfig /flushdns")
        self.write_to_hosts(domain)
        os.system("ipconfig /flushdns")

    def block_domain_linux(self, domain: str) -> None:
        self.write_to_hosts(domain)
    

class WebLockerWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__hosts_manager = WebLockerHostsManager()
        
        styling = ''
        with open(os.path.abspath("./css/dark_theme.css"), 'r') as theme_file:
            styling = theme_file.read()
        
        self.setStyleSheet(styling)
        
        self.__initUI()
        
        
    def __initUI(self) -> None:
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('WebLocker Window Instance')
    
        self.block_website_label = QLabel(self)
        self.block_website_label.setObjectName('block_website_label')
        self.block_website_label.setText("<b>Enter Domain Of Website To Block: </b>")
        self.block_website_label.resize(self.block_website_label.sizeHint())
        self.block_website_label.move(40, 50)


        self.block_website_line_edit = QLineEdit(self)
        self.block_website_line_edit.setObjectName('block_website_line_edit')
        self.block_website_line_edit.setToolTip('Enter Website Domain To Block')
        self.block_website_line_edit.resize(self.block_website_line_edit.sizeHint())
        self.block_website_line_edit.setFixedWidth(150)
        self.block_website_line_edit.move(280, 50)
        

        self.block_website_button = QPushButton('Block Website', self)
        self.block_website_button.setObjectName('block_website_button')
        self.block_website_button.setToolTip('Click To Block A Website')
        self.block_website_button.clicked.connect(self.block_website)
        self.block_website_button.resize(self.block_website_button.sizeHint())
        self.block_website_button.move(450, 50)


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