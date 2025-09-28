from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QGraphicsOpacityEffect,  QPushButton


class IconButton(QPushButton):
    def __init__(self, icon_path, parent=None, HoverStyle=True, ColorInverse=False):
        super().__init__(parent)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(self.sizeHint() * 2)
        self.setFixedSize(50, 50)
        self.setStyleSheet("background: transparent; border: none;")

        # Прозрачность
        if HoverStyle:
            self.effect = QGraphicsOpacityEffect(opacity=0.5)
            self.setGraphicsEffect(self.effect)
