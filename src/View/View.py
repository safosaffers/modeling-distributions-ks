from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from PySide6.QtCore import QTranslator
from View.Ui_View import Ui_View
import View.assets.resources_rc
from .theme_manager import ThemeManager
from .language_manager import LanguageManager
from PySide6.QtGui import QDoubleValidator, QIntValidator

# For the Pearson criterion visualization
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to avoid conflicts
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import re


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
        self.ui.pb_page_3.clicked.connect(lambda: self.switch_page(3))  # Критерий Пирсона
        self.ui.pb_page_4.clicked.connect(lambda: self.switch_page(4))  # О программе

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

        # Connect the Pearson criterion button
        self.ui.btnPirson.clicked.connect(self.calculate_pearson_criterion)


    def calculate_pearson_criterion(self):
        """Обработчик кнопки вычисления критерия Пирсона"""
        try:
            # Получаем текст из текстового поля
            sample_text = self.ui.teSample.toPlainText().strip()
            
            if not sample_text:
                QMessageBox.warning(self, "Ошибка ввода", "Пожалуйста, введите выборку.")
                return
            
            # Парсим числа из текста (разделители: пробел, запятая, точка с запятой, новая строка)
            # Поддерживаем как целые, так и вещественные числа
            numbers_str = re.split(r'[,\s;]+', sample_text)
            sample = []
            
            for num_str in numbers_str:
                num_str = num_str.strip()
                if num_str:  # Если строка не пустая
                    try:
                        num = float(num_str)
                        sample.append(num)
                    except ValueError:
                        QMessageBox.warning(self, "Ошибка ввода", f"Некорректное число: '{num_str}'")
                        return
            
            if len(sample) < 5:
                QMessageBox.warning(self, "Ошибка", "Выборка должна содержать не менее 5 элементов.")
                return
            
            # Получаем уровень значимости (по умолчанию 0.05, если поле пустое)
            alpha_str = "0.05"  # Можно добавить поле ввода уровня значимости позже
            
            # Вычисляем критерий Пирсона
            from Model.Model import Model
            result = Model.calculate_pearson_criterion(sample, float(alpha_str))
            
            # Обновляем интерфейс с результатами
            self.display_pearson_results(result)
            
        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при обработке выборки: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")


    def display_pearson_results(self, result):
        """Отображает результаты критерия Пирсона в интерфейсе"""
        try:
            # Очищаем предыдущий график
            for child in self.ui.vlHistogram.children():
                child.deleteLater()
            
            # Создаем фигуру matplotlib для гистограммы
            fig = Figure(figsize=(5, 4), dpi=100)
            canvas = FigureCanvas(fig)
            
            # Добавляем фигуру в layout
            self.ui.vlHistogram.addWidget(canvas)
            
            # Рисуем гистограмму
            ax = fig.add_subplot(111)
            
            # Подготовка данных для гистограммы
            observed_freq = result["observed_frequencies"]
            expected_freq = result["expected_frequencies"]
            interval_bounds = result["interval_bounds"]
            num_intervals = len(observed_freq)
            
            # Позиции для столбцов
            x_pos = range(num_intervals)
            
            # Рисуем столбцы для наблюдаемых и ожидаемых частот
            width = 0.35
            ax.bar([x - width/2 for x in x_pos], observed_freq, width, label='Наблюдаемые', alpha=0.7)
            ax.bar([x + width/2 for x in x_pos], expected_freq, width, label='Ожидаемые', alpha=0.7)
            
            ax.set_xlabel('Интервалы')
            ax.set_ylabel('Частота')
            ax.set_title('Критерий Пирсона: наблюдаемые vs ожидаемые частоты')
            ax.legend()
            
            # Устанавливаем подписи оси X как границы интервалов
            ax.set_xticks(x_pos)
            interval_labels = [f'[{interval_bounds[i]:.2f}, {interval_bounds[i+1]:.2f})' 
                              for i in range(len(interval_bounds)-2)]
            # Для последнего интервала используем [] вместо ) если нужно включить последний элемент
            interval_labels.append(f'[{interval_bounds[-2]:.2f}, {interval_bounds[-1]:.2f}]')
            ax.set_xticklabels(interval_labels, rotation=45, ha="right")
            
            fig.tight_layout()
            canvas.draw()
            
            # Выводим информацию о результате в метку
            info_text = (
                f"Критерий Пирсона:\n"
                f"Размер выборки: {result['n']}\n"
                f"Количество интервалов: {result['num_intervals']}\n"
                f"Статистика χ²: {result['chi_squared_statistic']:.4f}\n"
                f"Критическое значение: {result['critical_value']:.4f}\n"
                f"p-значение: {result['p_value']:.4f}\n"
                f"Альфа: {result['alpha']}\n"
                f"Степени свободы: {result['degrees_of_freedom']}\n"
                f"Результат: {result['message']}"
            )
            self.ui.lblPirsonInfo.setText(info_text)
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка отображения", f"Ошибка при отображении результатов: {str(e)}")