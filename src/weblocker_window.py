from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QLineEdit, QLabel)
from PyQt6.QtGui import QFont
from weblocker_hosts_manager import *
from consts import *

class WebLockerWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__hosts_manager = WebLockerHostsManager()
        
        styling = ''
        with open(os.path.abspath("./css/themes/light_theme.css"), FILE_READ) as theme_file:
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


        self.unblock_website_label = QLabel(self)
        self.unblock_website_label.setObjectName('unblock_website_label')
        self.unblock_website_label.setText("<b>Enter Domain Of Website To Unblock: </b>")
        self.unblock_website_label.resize(self.unblock_website_label.sizeHint())
        self.unblock_website_label.move(40, 100)


        self.unblock_website_line_edit = QLineEdit(self)
        self.unblock_website_line_edit.setObjectName('unblock_website_line_edit')
        self.unblock_website_line_edit.setToolTip('Enter Website Domain To Unblock')
        self.unblock_website_line_edit.resize(self.unblock_website_line_edit.sizeHint())
        self.unblock_website_line_edit.setFixedWidth(150)
        self.unblock_website_line_edit.move(280, 100)
        

        self.unblock_website_button = QPushButton('Unblock Website', self)
        self.unblock_website_button.setObjectName('unblock_website_button')
        self.unblock_website_button.setToolTip('Click To Unblock A Website')
        self.unblock_website_button.clicked.connect(self.unblock_website)
        self.unblock_website_button.resize(self.unblock_website_button.sizeHint())
        self.unblock_website_button.move(450, 100)


        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.setWindowTitle('WebLocker')
        self.center()
        self.show()
    
    
    def block_website(self) -> None:
        domain = self.block_website_line_edit.text()
        print("Blocking", domain)
        if domain and len(domain):
            self.__hosts_manager.block_domain(domain)
            
            
    def unblock_website(self) -> None:
        domain = self.block_website_line_edit.text()
        print("Unblocking", domain)
        if domain and len(domain):
            self.__hosts_manager.unblock_domain(domain)    
            
            
    def center(self) -> None:
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())    
