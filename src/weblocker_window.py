from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QLineEdit, QLabel, QFrame, QMainWindow, QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from weblocker_hosts_manager import *
from GToggle import GToggle
from consts import *

class WebLockerWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__hosts_manager = WebLockerHostsManager()
        
        self.dark_styling = ''
        with open(os.path.abspath("./css/themes/dark_theme.css"), FILE_READ) as theme_file:
            self.dark_styling = theme_file.read()
        
        self.light_styling = ''
        with open(os.path.abspath("./css/themes/light_theme.css"), FILE_READ) as theme_file:
            self.light_styling = theme_file.read()
        
        self.setStyleSheet(self.dark_styling)
        
        self.__initUI()
        
        
    def __initUI(self) -> None:
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('WebLocker Window Instance')
        
        self.container = QFrame()
        self.container.setObjectName('container')
        
        self.main_layout = QVBoxLayout()
    
        self.block_website_label = QLabel(self)
        self.block_website_label.setObjectName('block_website_label')
        self.block_website_label.setText("<b>Enter Domain Of Website To Block: </b>")
        self.block_website_label.resize(self.block_website_label.sizeHint())


        self.block_website_line_edit = QLineEdit(self)
        self.block_website_line_edit.setObjectName('block_website_line_edit')
        self.block_website_line_edit.setToolTip('Enter Website Domain To Block')
        self.block_website_line_edit.resize(self.block_website_line_edit.sizeHint())
        

        self.block_website_button = QPushButton('Block Website', self)
        self.block_website_button.setObjectName('block_website_button')
        self.block_website_button.setToolTip('Click To Block A Website')
        self.block_website_button.clicked.connect(self.block_website)
        self.block_website_button.resize(self.block_website_button.sizeHint())
        self.block_website_button.setFixedWidth(120)


        self.unblock_website_label = QLabel(self)
        self.unblock_website_label.setObjectName('unblock_website_label')
        self.unblock_website_label.setText("<b>Enter Domain Of Website To Unblock: </b>")
        self.unblock_website_label.resize(self.unblock_website_label.sizeHint())


        self.unblock_website_line_edit = QLineEdit(self)
        self.unblock_website_line_edit.setObjectName('unblock_website_line_edit')
        self.unblock_website_line_edit.setToolTip('Enter Website Domain To Unblock')
        self.unblock_website_line_edit.resize(self.unblock_website_line_edit.sizeHint())
        

        self.unblock_website_button = QPushButton('Unblock Website', self)
        self.unblock_website_button.setObjectName('unblock_website_button')
        self.unblock_website_button.setToolTip('Click To Unblock A Website')
        self.unblock_website_button.clicked.connect(self.unblock_website)
        self.unblock_website_button.resize(self.unblock_website_button.sizeHint())
        self.unblock_website_button.setFixedWidth(120)
        
        
        self.theme_toggle = GToggle(self)
        self.theme_toggle.toggled.connect(self.change_theme)
                
        
        self.theme_label = QLabel(self)
        self.theme_label.setObjectName("theme_label")
        self.theme_label.setText("<b>Dark Mode: </b>")
        self.unblock_website_label.resize(self.unblock_website_label.sizeHint())
        
        
        self.block_row_layout = QHBoxLayout()
        self.block_row_layout.addWidget(self.block_website_label)
        self.block_row_layout.addWidget(self.block_website_line_edit)
        self.block_row_layout.addWidget(self.block_website_button)
        self.main_layout.addLayout(self.block_row_layout)
        
        self.unblock_row_layout = QHBoxLayout()
        self.unblock_row_layout.addWidget(self.unblock_website_label)
        self.unblock_row_layout.addWidget(self.unblock_website_line_edit)
        self.unblock_row_layout.addWidget(self.unblock_website_button)
        self.main_layout.addLayout(self.unblock_row_layout)

        self.theme_row_layout = QHBoxLayout()
        self.theme_row_layout.addWidget(self.theme_label, 0)
        self.theme_row_layout.addWidget(self.theme_toggle, 0)
        self.theme_row_layout.insertStretch(-1, 1)
        self.main_layout.addLayout(self.theme_row_layout)

        
        self.container.setLayout(self.main_layout)
        self.setCentralWidget(self.container)
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
        domain = self.unblock_website_line_edit.text()
        print("Unblocking", domain)
        if domain and len(domain):
            self.__hosts_manager.unblock_domain(domain)    
    
    
    def change_theme(self) -> None:
        if not self.theme_toggle.isChecked():
            self.setStyleSheet(self.dark_styling)
        else:
            self.setStyleSheet(self.light_styling)    
            
    def center(self) -> None:
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())    
