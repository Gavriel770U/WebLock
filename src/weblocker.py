import sys
from PyQt6.QtWidgets import QApplication
from weblocker_window import *
from consts import *

class WebLocker(object):
    def __init__(self) -> None:
        self.__init_graphics()
    
    
    def __init_graphics(self) -> None:
        self.__app = QApplication(sys.argv)
        self.__window = WebLockerWindow()
        
    
    def run(self) -> None:
        self.__window.show()
        sys.exit(self.__app.exec())