from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QLineEdit, QLabel, QFrame, QMainWindow, QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QEasingCurve
from weblocker_hosts_manager import *
from GToggle import GToggle
from consts import *
import os
import sys

class WebLockerWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__hosts_manager = WebLockerHostsManager()

        # Example usage
        self.__css_dark_theme_path = self.resource_path(os.path.join('css', 'themes', 'dark_theme.css'))
        self.__css_light_theme_path = self.resource_path(os.path.join('css', 'themes', 'light_theme.css'))
        self.__msedge_blocklist_path = self.resource_path(os.path.join('block_lists', 'msedge_blocklist.txt'))
        
        self.dark_styling = ''
        with open(self.__css_dark_theme_path, FILE_READ) as theme_file:
            self.dark_styling = theme_file.read()
        
        self.light_styling = ''
        with open(self.__css_light_theme_path, FILE_READ) as theme_file:
            self.light_styling = theme_file.read()
        
        self.setStyleSheet(self.dark_styling)
        
        self.__initUI()
 
       
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
        
        
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
        
        
        self.theme_toggle = GToggle(self, QEasingCurve.Type.InOutQuint)
        self.theme_toggle.toggled.connect(self.change_theme)
                
        
        self.theme_label = QLabel(self)
        self.theme_label.setObjectName("theme_label")
        self.theme_label.setText("<b>Dark Mode: </b>")
        self.unblock_website_label.resize(self.unblock_website_label.sizeHint())
        
        
        self.block_msedge_spyware_button = QPushButton('Block MSEdge Spyware', self)
        self.block_msedge_spyware_button.setObjectName("block_msedge_spyware_button")
        self.block_msedge_spyware_button.setToolTip('Click To Block MSEdge Spyware')
        self.block_msedge_spyware_button.clicked.connect(self.block_msedge_spyware)
        self.block_msedge_spyware_button.resize(self.block_msedge_spyware_button.sizeHint())
        
        
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
        
        self.advanced_blocks_layout = QHBoxLayout()
        self.advanced_blocks_layout.addWidget(self.block_msedge_spyware_button)
        self.theme_row_layout.addLayout(self.advanced_blocks_layout)

        
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
    
    
    def block_msedge_spyware(self) -> None:
        print("Blocking MSEdge Spyware And Ads...")
        domains_to_block = ''
        
        with open(self.__msedge_blocklist_path, FILE_READ) as msedge_block_list_file:
            domains_to_block = msedge_block_list_file.read()
            
        self.__hosts_manager.block_domains_list(domains_to_block)
    
    
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
