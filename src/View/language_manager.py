# View/language_manager.py

from PySide6.QtCore import QTranslator
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from View.IconButton import IconButton
from PySide6.QtCore import Qt


class LanguageManager:
    SUPPORTED_LANGUAGES = {
        "ru": ":/images/ru.svg",
        "en": ":/images/en.svg"
    }

    def __init__(self, view_instance):
        self.view = view_instance
        self.current_language = "ru"
        self._init_language_button()

    def _init_language_button(self):
        icon_path = self.SUPPORTED_LANGUAGES[self.current_language]
        self.btn_language = IconButton(icon_path, HoverStyle=False)
        self.btn_language.setFixedSize(40, 40)
        self.view.ui.layout_language.addWidget(
            self.btn_language, alignment=Qt.AlignCenter, stretch=4
        )
        self.btn_language.clicked.connect(self.toggle_language)

    def toggle_language(self):
        # Переключаем язык
        if self.current_language == "ru":
            self.current_language = "en"
        else:
            self.current_language = "ru"

        # Обновляем иконку
        icon_path = self.SUPPORTED_LANGUAGES[self.current_language]
        self.btn_language.setIcon(QIcon(icon_path))

        # Применяем язык
        self.set_language(self.current_language)

    def set_language(self, lang_code: str):
        """Установка выбранного языка."""
        # Удаляем старый переводчик
        app = QApplication.instance()
        if hasattr(self.view, 'app_translator'):
            app.removeTranslator(self.view.app_translator)

        # Создаём и загружаем новый
        self.view.app_translator = QTranslator(self.view)
        if self.view.app_translator.load(f":/languages/language_{lang_code}.qm"):
            app.installTranslator(self.view.app_translator)

        self.current_language = lang_code

        # Обновляем тексты интерфейса
        self.view.ui.retranslateUi(self.view)

        # Обновляем заголовок окна (если нужно)
        self._update_window_title()

    def _update_window_title(self):
        titles = {
            "ru": "Каримов Сафо 5095. Моделирование различных видов распределений",
            "en": "Karimov Safo 5095. Modeling of various types of distributions"
        }

        self.view.setWindowTitle(titles.get(self.current_language, ""))
