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
