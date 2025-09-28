from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QTranslator
from View.Ui_View import Ui_View
import View.assets.resources_rc
from .theme_manager import ThemeManager
from .language_manager import LanguageManager
from PySide6.QtGui import QDoubleValidator, QIntValidator


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.app_translator = QTranslator(self)
        if self.app_translator.load(":/languages/language_ru.qm"):
            QApplication.instance().installTranslator(self.app_translator)
        
        self.ui = Ui_View()
        self.ui.setupUi(self)

        # Инициализация менеджеров
        self.theme_manager = ThemeManager(self)
        self.language_manager = LanguageManager(self)

        # Подключение навигации
        self.ui.pb_page_0.clicked.connect(lambda: self.switch_page(0))
        self.ui.pb_page_1.clicked.connect(lambda: self.switch_page(1))
        self.ui.pb_page_2.clicked.connect(lambda: self.switch_page(2))
        self.ui.pb_page_3.clicked.connect(lambda: self.switch_page(3))

        # Начальная страница
        self.switch_page(0)
        self.theme_manager.apply_theme()

        self.set_parameters_validators()

    def switch_page(self, index):
        self.ui.sw_pages.setCurrentIndex(index)
        self.theme_manager.update_buttons()
    

    def set_parameters_validators(self):
        # === Общие настройки для float ===
        float_validator = QDoubleValidator(-1e9, 1e9, 6)
        float_validator.setNotation(QDoubleValidator.StandardNotation)

        # === Общие настройки для положительных float (λ, σ²) ===
        positive_float_validator = QDoubleValidator(1e-6, 1e9, 6)
        positive_float_validator.setNotation(QDoubleValidator.StandardNotation)

        # === Общие настройки для N (объём выборки) ===
        n_validator = QIntValidator(1, 10_000_000)  # от 1 до 10 млн

        # --- Равномерное распределение ---
        self.ui.le_uniform_distribution_a_parameter.setValidator(float_validator)
        self.ui.le_uniform_distribution_b_parameter.setValidator(float_validator)
        self.ui.le_uniform_distribution_N_parameter.setValidator(n_validator)

        # --- Показательное распределение ---
        self.ui.le_exponential_distribution_lamda_parameter.setValidator(positive_float_validator)
        self.ui.le_exponential_distribution_N_parameter.setValidator(n_validator)

        # --- Нормальное распределение ---
        self.ui.le_normal_distribution_a_parameter.setValidator(float_validator)
        # σ² — дисперсия, должна быть > 0
        self.ui.le_normal_distribution_sigma_square_parameter.setValidator(positive_float_validator)
        self.ui.le_normal_distribution_N_parameter.setValidator(n_validator)