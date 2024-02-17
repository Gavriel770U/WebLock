from PyQt6.QtCore import Qt, QRect, pyqtProperty, QPropertyAnimation, QPoint, \
    QEasingCurve
from PyQt6.QtGui import QColor, QFontMetrics, QPainter, QPainterPath, QBrush, \
    QPen, QFont
from PyQt6.QtWidgets import QCheckBox

class GToggle(QCheckBox):
    bg_color = pyqtProperty(
        QColor, lambda self: self._bg_color,
        lambda self, col: setattr(self, '_bg_color', col))
    circle_color = pyqtProperty(
        QColor, lambda self: self._circle_color,
        lambda self, col: setattr(self, '_circle_color', col))
    active_color = pyqtProperty(
        QColor, lambda self: self._active_color,
        lambda self, col: setattr(self, '_active_color', col))
    disabled_color = pyqtProperty(
        QColor, lambda self: self._disabled_color,
        lambda self, col: setattr(self, '_disabled_color', col))
    text_color = pyqtProperty(
        QColor, lambda self: self._text_color,
        lambda self, col: setattr(self, '_text_color', col))

    def __init__(self, parent=None, animation_curve: QEasingCurve.Type = QEasingCurve.Type.InOutCubic) -> None:
        super().__init__(parent)
        self._bg_color, self._circle_color, self._active_color, \
            self._disabled_color, self._text_color = QColor("#0BF"), \
            QColor("#DDD"), QColor('#777'), QColor("#CCC"), QColor("#000")
        self._circle_pos, self._intermediate_bg_color = None, None
        self.setFixedHeight(18)
        self._animation_duration = 500  # milliseconds
        self.stateChanged.connect(self.start_transition)
        self._user_checked = False  # Introduced flag to check user-initiated changes
        self._animation_curve = animation_curve

    circle_pos = pyqtProperty(
        float, lambda self: self._circle_pos,
        lambda self, pos: (setattr(self, '_circle_pos', pos), self.update()))
    intermediate_bg_color = pyqtProperty(
        QColor, lambda self: self._intermediate_bg_color,
        lambda self, col: setattr(self, '_intermediate_bg_color', col))

    def setDuration(self, duration: int) -> None:
        """
        Set the duration for the animation.
        :param duration: Duration in milliseconds.
        """
        self._animation_duration = duration

    def update_pos_color(self, checked=None) -> None:
        self._circle_pos = self.height() * (1.1 if checked else 0.1)
        if self.isChecked():
            self._intermediate_bg_color = self._active_color
        else:
            self._intermediate_bg_color = self._bg_color

    def start_transition(self, state) -> None:
        if not self._user_checked:  # Skip animation if change isn't user-initiated
            self.update_pos_color(state)
            return
        for anim in [self.create_animation, self.create_bg_color_animation]:
            animation = anim(state)
            animation.start()
        self._user_checked = False  # Reset the flag after animation starts

    def mousePressEvent(self, event) -> None:
        self._user_checked = True  # Set flag when user manually clicks the toggle
        super().mousePressEvent(event)

    def create_animation(self, state):
        return self._create_common_animation(
            state, b'circle_pos', self.height() * 0.1, self.height() * 1.1)

    def create_bg_color_animation(self, state):
        return self._create_common_animation(
            state, b'intermediate_bg_color', self._bg_color, self._active_color)

    def _create_common_animation(self, state, prop, start_val, end_val):
        animation = QPropertyAnimation(self, prop, self)
        animation.setEasingCurve(self._animation_curve)
        animation.setDuration(self._animation_duration)
        animation.setStartValue(start_val if state else end_val)
        animation.setEndValue(end_val if state else start_val)
        return animation

    def showEvent(self, event):
        super().showEvent(event)  # Ensure to call the super class's implementation
        self.update_pos_color(self.isChecked())

    def resizeEvent(self, event):
        self.update_pos_color(self.isChecked())

    def sizeHint(self):
        size = super().sizeHint()
        text_width = QFontMetrics(
            self.font()).boundingRect(self.text()).width()
        size.setWidth(int(self.height() * 2 + text_width * 1.075))
        return size

    def hitButton(self, pos: QPoint) -> bool:
        return self.contentsRect().contains(pos)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        circle_color = QColor(
            self.disabled_color if not self.isEnabled() else self.circle_color)
        bg_color = QColor(
            self.disabled_color if not self.isEnabled() else
            self.intermediate_bg_color)
        text_color = QColor(
            self.disabled_color if not self.isEnabled() else self.text_color)

        bordersradius = self.height() / 2
        togglewidth = self.height() * 2
        togglemargin = self.height() * 0.3
        circlesize = self.height() * 0.8

        bg_path = QPainterPath()
        bg_path.addRoundedRect(
            0, 0, togglewidth, self.height(), bordersradius, bordersradius)
        painter.fillPath(bg_path, QBrush(bg_color))

        circle = QPainterPath()
        circle.addEllipse(
            self.circle_pos, self.height() * 0.1, circlesize, circlesize)
        painter.fillPath(circle, QBrush(circle_color))

        painter.setPen(QPen(QColor(text_color)))
        painter.setFont(self.font())
        text_rect = QRect(int(togglewidth + togglemargin), 0, self.width() -
                          int(togglewidth + togglemargin), self.height())
        text_rect.adjust(
            0, (self.height() - painter.fontMetrics().height()) // 2, 0, 0)
        painter.drawText(text_rect, Qt.AlignmentFlag.AlignLeft |
                         Qt.AlignmentFlag.AlignVCenter, self.text())
        painter.end()