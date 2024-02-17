from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtGui import QPainter, QColor, QBrush, QPen
from PyQt6.QtCore import Qt, QRect, QPoint, QEasingCurve

class GToggle(QCheckBox):
    def __init__(self, 
                 width: int,
                 height: int,
                 background_color: str,
                 circle_color: str,
                 active_color: str,
                 animation_curve = QEasingCurve

    ) -> None:
        QCheckBox.__init__(self)
        
        self.setFixedSize(width, height)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.__background_color = background_color
        self.__circle_color = circle_color
        self.__active_color = active_color
        
        self.stateChanged.connect(self.debug)
    
    def debug(self):
        # print(f"Status: {self.isChecked()}")
        pass    
        
    def hitButton(self, position: QPoint):
        return self.contentsRect().contains(position)
        
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setPen(Qt.PenStyle.NoPen)        
        #painter.
        
        rect = QRect(0, 0, self.width(), self.height())
        
        if not self.isChecked():
            painter.setBrush(QColor(self.__background_color))
            painter.drawRoundedRect(0, 0, rect.width(), rect.height(), self.height() / 2, self.height() / 2)
            
            painter.setBrush(QColor(self.__circle_color))
            painter.drawEllipse(3, 3, 22, 22)
        else:
            painter.setBrush(QColor(self.__active_color))
            painter.drawRoundedRect(0, 0, rect.width(), rect.height(), self.height() / 2, self.height() / 2)
        
            painter.setBrush(QColor(self.__circle_color))
            painter.drawEllipse(self.width() - 26, 3, 22, 22)
        
        painter.end()