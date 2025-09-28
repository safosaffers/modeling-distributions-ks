# View/theme_manager.py

from PySide6.QtCore import QFile, QTextStream
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

class ThemeManager:
    def __init__(self, view_instance):
        self.view = view_instance
        self.current_theme = "light"
        self._init_theme_button()

    def _init_theme_button(self):
        from View.IconButton import IconButton
        from PySide6.QtCore import Qt

        self.btn_change_theme = IconButton(":/images/light_theme.svg", HoverStyle=False)
        self.btn_change_theme.setFixedSize(50, 50)
        self.view.ui.layout_theme.addWidget(self.btn_change_theme, alignment=Qt.AlignCenter, stretch=4)
        self.btn_change_theme.clicked.connect(self.toggle_theme)

    def toggle_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
            self.btn_change_theme.setIcon(QIcon(":/images/dark_theme.svg"))
        else:
            self.current_theme = "light"
            self.btn_change_theme.setIcon(QIcon(":/images/light_theme.svg"))

        self.apply_theme()

    def apply_theme(self):
        self._load_stylesheet(self.view, f":/styles/style_{self.current_theme}.qss")
        self._load_stylesheet(self.view.ui.f_menu, f":/styles/style_{self.current_theme}_menu.qss")
        self._apply_tooltip_stylesheets(f":/styles/style_{self.current_theme}_toolTip.qss")

        # Обновление кнопок навигации (если они зависят от темы)
        if hasattr(self.view, 'navigators'):
            for nav in self.view.navigators.values():
                nav.apply_theme(self.current_theme)

        self.update_buttons()

    def update_buttons(self):
        buttons = [
            self.view.ui.pb_page_0,
            self.view.ui.pb_page_1,
            self.view.ui.pb_page_2,
            self.view.ui.pb_page_3
        ]
        current_page = self.view.ui.sw_pages.currentIndex()

        for i, button in enumerate(buttons):
            if i == current_page:
                color = "rgba(253, 253, 253, 0.7)" if self.current_theme == "light" else "rgba(10, 10, 10, 0.7)"
                button.setStyleSheet(f"QPushButton {{ background: {color}; }}")
            else:
                if self.current_theme == "light":
                    color = "rgba(253, 253, 253, 0.0)"
                    hover_color = "rgb(193, 193, 193)"
                else:
                    color = "rgba(10, 10, 10, 0.0)"
                    hover_color = "rgba(90, 90, 90, 0.9)"
                button.setStyleSheet(f"""
                    QPushButton {{ background: {color}; }}
                    QPushButton:hover {{ background: {hover_color}; }}
                """)

        if hasattr(self.view, 'navigators') and self.view.navigators:
            for idx, nav in self.view.navigators.items():
                nav.nb_Visible(idx == self.view.ui.sw_pages.currentIndex())

    def _load_stylesheet(self, widget: QWidget, filename: str):
        file = QFile(filename)
        if not file.open(QFile.ReadOnly | QFile.Text):
            print(f"Ошибка открытия файла стиля: {filename}")
            return
        stream = QTextStream(file)
        widget.setStyleSheet(stream.readAll())

    def _apply_tooltip_stylesheets(self, filename: str):
        file = QFile(filename)
        if not file.open(QFile.ReadOnly | QFile.Text):
            print(f"Ошибка открытия файла тултипов: {filename}")
            return
        stream = QTextStream(file)
        stylesheet = stream.readAll()

        for child in self.view.ui.__dict__.values():
            if hasattr(child, 'objectName') and isinstance(child, QWidget):
                if child.objectName().startswith("tip"):
                    child.setStyleSheet(stylesheet)