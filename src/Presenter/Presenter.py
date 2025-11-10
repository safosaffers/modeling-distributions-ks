# Presenter/Presenter.py

from Model.Model import Model
from View.View import View
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem


class Presenter:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

        # Подключаем сигналы
        self.view.ui.pb_uniform_distribution_calculate.clicked.connect(
            self._on_uniform_calculate)
        self.view.ui.pb_exponential_distribution_calculate.clicked.connect(
            self._on_exponential_calculate)
        self.view.ui.pb_normal_distribution_calculate.clicked.connect(
            self._on_normal_calculate)
        
        # Connect the comboBox for Pearson criterion
        self.view.ui.comboBox.currentTextChanged.connect(
            self._on_distribution_type_changed)
        
        # Connect the Pearson criterion button
        self.view.ui.btnPirson.clicked.connect(
            self._on_pearson_criterion_calculate)
        
        # Initialize histogram canvas reference
        self.histogram_canvas = None

    def _show_error(self, message: str):
        QMessageBox.critical(self.view, "Ошибка ввода", message)

    def _on_uniform_calculate(self):
        try:
            a = float(
                self.view.ui.le_uniform_distribution_a_parameter.text().strip())
            b = float(
                self.view.ui.le_uniform_distribution_b_parameter.text().strip())
            N = int(self.view.ui.le_uniform_distribution_N_parameter.text().strip())

            if N <= 0:
                raise ValueError("N должно быть положительным целым числом.")
            if a >= b:
                raise ValueError("Должно выполняться: a < b.")

            # Модель возвращает: (Mx_theor, Dx_theor, Mx_emp, Dx_emp, sample_first_20)
            Mx_theor, Dx_theor, Mx_emp, Dx_emp, sample = self.model._calculate_uniform(
                a, b, N)

            # Обновляем дельты
            self.view.ui.le_uniform_distribution_delta_1.setText(
                f"{abs(Mx_emp - Mx_theor):.6f}")
            self.view.ui.le_uniform_distribution_delta_2.setText(
                f"{abs(Dx_emp - Dx_theor):.6f}")

            # Выводим выборку
            self._display_sample_in_table(
                sample, self.view.ui.tw_uniform_distribution_result)
            
            # Store the sample for Pearson criterion
            self.model.store_sample_uniform(sample)
        except ValueError as e:
            self._show_error(f"Некорректный ввод: {e}")
        except Exception as e:
            self._show_error(f"Ошибка расчёта: {e}")

    def _on_exponential_calculate(self):
        try:
            lamda = float(
                self.view.ui.le_exponential_distribution_lamda_parameter.text().strip())
            N = int(
                self.view.ui.le_exponential_distribution_N_parameter.text().strip())

            if lamda <= 0:
                raise ValueError("λ должно быть > 0.")
            if N <= 0:
                raise ValueError("N должно быть положительным целым числом.")

            Mx_theor, Dx_theor, Mx_emp, Dx_emp, sample = self.model._calculate_exponential(
                lamda, N)

            self.view.ui.le_exponential_distribution_delta_1.setText(
                f"{abs(Mx_emp - Mx_theor):.6f}")
            self.view.ui.le_exponential_distribution_delta_2.setText(
                f"{abs(Dx_emp - Dx_theor):.6f}")

            self._display_sample_in_table(
                sample, self.view.ui.tw_exponential_distribution_result)
            
            # Store the sample for Pearson criterion
            self.model.store_sample_exponential(sample)

        except ValueError as e:
            self._show_error(f"Некорректный ввод: {e}")
        except Exception as e:
            self._show_error(f"Ошибка расчёта: {e}")

    def _on_normal_calculate(self):
        try:
            a = float(
                self.view.ui.le_normal_distribution_a_parameter.text().strip())
            sigma_square = int(
                self.view.ui.le_normal_distribution_sigma_square_parameter.text().strip())
            N = int(self.view.ui.le_normal_distribution_N_parameter.text().strip())

            if sigma_square <= 0:
                raise ValueError("σ должно быть > 0.")
            if N <= 0:
                raise ValueError("N должно быть положительным целым числом.")

            Mx_theor, Dx_theor, Mx_emp, Dx_emp, sample = self.model._calculate_normal(
                a, sigma_square, N)

            self.view.ui.le_normal_distribution_delta_1.setText(
                f"{abs(Mx_emp - Mx_theor):.6f}")
            self.view.ui.le_normal_distribution_delta_2.setText(
                f"{abs(Dx_emp - Dx_theor):.6f}")

            self._display_sample_in_table(
                sample, self.view.ui.tw_normal_distribution_result)
            
            # Store the sample for Pearson criterion
            self.model.store_sample_normal(sample)

        except ValueError as e:
            self._show_error(f"Некорректный ввод: {e}")
        except Exception as e:
            self._show_error(f"Ошибка расчёта: {e}")

    def _display_sample_in_table(self, sample, table_widget, countOfRows=20):
        """Универсальный метод для отображения выборки в таблице, разбитой на 4 столбца."""
        cuttered_sample = sample[:countOfRows]
        num_columns = 4
        num_values = len(cuttered_sample)

        # Вычисляем количество строк: округляем вверх
        num_rows = (num_values + num_columns - 1) // num_columns

        table_widget.setRowCount(num_rows)
        table_widget.setColumnCount(num_columns)
        table_widget.setHorizontalHeaderLabels(
            [f"Столбец {i+1}" for i in range(num_columns)])
        table_widget.horizontalHeader().setStretchLastSection(True)
        table_widget.verticalHeader().setVisible(False)

        # Заполняем таблицу по столбцам (сначала заполняем первый столбец сверху вниз, потом второй и т.д.)
        for idx, value in enumerate(cuttered_sample):
            row = idx % num_rows
            col = idx // num_rows
            table_widget.setItem(row, col, QTableWidgetItem(f"{value:.6f}"))

        table_widget.resizeColumnsToContents()

    def _on_distribution_type_changed(self, text):
        """Handle the distribution type change in the comboBox"""
        # Enable/disable the calculation button based on selection
        if text == "Выберите распределение":
            self.view.ui.btnPirson.setEnabled(False)
            # Clear the sample area
            self.view.ui.teSample.clear()
        elif text == "Задать вручную":
            # Enable button for manual input
            self.view.ui.btnPirson.setEnabled(True)
            # Clear the sample when "Set manually" is selected
            self.view.ui.teSample.clear()
        else:
            # Enable button and populate sample for distribution types
            self.view.ui.btnPirson.setEnabled(True)
            # Get the sample based on selected distribution
            sample = self.model.get_sample_by_type(text)
            if sample:
                # Format the sample as a string with space-separated values
                sample_str = " ".join([f"{value:.6f}" for value in sample])
                self.view.ui.teSample.setPlainText(sample_str)
            else:
                # If no sample exists for this distribution, clear the text area
                self.view.ui.teSample.clear()

    def _on_pearson_criterion_calculate(self):
        """Handle the Pearson criterion calculation"""
        try:
            # Get the selected distribution type from comboBox
            distribution_type = self.view.ui.comboBox.currentText()
            
            # Check if the correct distribution type is selected
            if distribution_type == "Выберите распределение":
                self._show_error("Выберите тип распределения для проверки гипотезы")
                return
            elif distribution_type == "Задать вручную":
                # For manual input, the user needs to enter data themselves
                pass  # Allow manual input
            
            # Read the sample from teSample
            sample_text = self.view.ui.teSample.toPlainText().strip()
            if not sample_text:
                self._show_error("Поле ввода выборки пустое")
                return
            
            # Convert to numeric array
            sample_str_values = sample_text.split()
            sample = []
            for val in sample_str_values:
                try:
                    sample.append(float(val))
                except ValueError:
                    self._show_error(f"Невозможно преобразовать '{val}' в число")
                    return
            
            # Calculate Pearson criterion
            result = self.model.calculate_pearson_criterion_for_distribution(sample, distribution_type)
            
            # Format and display the result
            chi2 = result["chi_squared_statistic"]
            df = result["degrees_of_freedom"]
            p_value = result["p_value"]
            conclusion = result["conclusion"]
            
            result_text = f"χ² = {chi2:.3f}, df = {df}, p = {p_value:.4f}\n{conclusion}"
            
            # Display the result in lblPirsonInfo
            self.view.ui.lblPirsonInfo.setText(result_text)
            
            # Show histogram (placeholder for now - will implement it next)
            self._show_histogram(sample, result)
            
        except ValueError as e:
            self._show_error(f"Ошибка при вычислениях: {e}")
        except Exception as e:
            self._show_error(f"Непредвиденная ошибка: {e}")

    def _show_histogram(self, sample, result):
        """Display the histogram and theoretical density"""
        try:
            import matplotlib
            matplotlib.use('Qt5Agg')  # Use Qt5Agg backend for compatibility
            from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
            from matplotlib.figure import Figure
            import numpy as np
            from scipy import stats
            
            # Clear any existing widgets in the histogram layout
            layout = self.view.ui.vlHistogram
            # Store canvas references to avoid premature deletion
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    # Delete the widget properly
                    widget = child.widget()
                    widget.deleteLater()
            
            # Create a matplotlib figure
            fig = Figure(figsize=(5, 4), dpi=100)
            canvas = FigureCanvas(fig)
            
            # Store reference to prevent deletion
            if not hasattr(self, '_canvas_refs'):
                self._canvas_refs = []
            self._canvas_refs.append(canvas)
            
            # Add the canvas to the layout
            layout.addWidget(canvas)
            
            # Create the plot
            ax = fig.add_subplot(111)
            
            # Plot histogram of the sample with density=True
            n, bins, patches = ax.hist(sample, bins=result["k"], density=True, 
                                      alpha=0.6, color='skyblue', label='Гистограмма выборки')
            
            # Add theoretical density based on distribution type
            x_min, x_max = min(sample), max(sample)
            x_range = x_max - x_min
            # Extend range slightly for better visualization
            x = np.linspace(x_min - 0.1*x_range, x_max + 0.1*x_range, 1000)
            
            distribution_type = result["distribution_type"]
            params = result["parameters"]
            
            if distribution_type == "Нормальное распределение":
                mu = params["mu"]
                sigma = params["sigma"]
                y = stats.norm.pdf(x, loc=mu, scale=sigma)
                ax.plot(x, y, 'r-', label='Теоретическая плотность', linewidth=2)
                
            elif distribution_type == "Равномерное распределение":
                a = params["a"]
                b = params["b"]
                # For uniform distribution, only plot in [a, b] range
                x_uniform = x[(x >= a) & (x <= b)]
                y_uniform = np.full_like(x_uniform, 1.0/(b-a))
                ax.plot(x_uniform, y_uniform, 'r-', label='Теоретическая плотность', linewidth=2)
                
            elif distribution_type == "Показательное распределение":
                lambda_param = params["lambda"]
                # For exponential distribution, only plot for x >= 0
                x_exp = x[x >= 0]  # Only positive x values
                y = stats.expon.pdf(x_exp, scale=1.0/lambda_param)
                ax.plot(x_exp, y, 'r-', label='Теоретическая плотность', linewidth=2)
            
            ax.set_xlabel('Значение')
            ax.set_ylabel('Плотность')
            ax.set_title('Гистограмма и теоретическая плотность')
            ax.legend()
            ax.grid(True, alpha=0.3)
            
            # Refresh the canvas
            canvas.draw()
            
        except ImportError:
            # If matplotlib is not installed, show a simple text message
            layout = self.view.ui.vlHistogram
            from PySide6.QtWidgets import QLabel
            label = QLabel("График недоступен: matplotlib не установлен")
            layout.addWidget(label)
        except Exception as e:
            # Handle any other errors that might occur during plotting
            layout = self.view.ui.vlHistogram
            from PySide6.QtWidgets import QLabel
            label = QLabel(f"Ошибка при построении графика: {str(e)}")
            layout.addWidget(label)
