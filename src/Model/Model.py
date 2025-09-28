# Model/Model.py

import random
from typing import List, Tuple
import math
class Model:
    @staticmethod
    def _calculate_uniform(a: float, b: float, N: int) -> Tuple[float, float, float, float, List[float]]:
        """
        Выполняет расчёты для заданных a, b, N.
        
        Возвращает:
            Mx (теоретическое мат. ожидание),
            Dx (теоретическая дисперсия),
            m (выборочное среднее),
            g (выборочная дисперсия),
            первые 20 значений выборки (или меньше, если N < 20)
        """
        if N <= 0:
            raise ValueError("N должно быть положительным целым числом")
        if a >= b:
            raise ValueError("Должно выполняться: a < b")

        # Генерация выборки
        sample = [a + random.random() * (b - a) for _ in range(N)]

        # Теоретические значения
        Mx = (a + b) / 2.0
        Dx = (b - a) ** 2 / 12.0

        # Выборочные значения
        m = sum(sample) / N
        mean_of_squares = sum(x * x for x in sample) / N
        g = mean_of_squares - m * m

        return Mx, Dx, m, g, sample

    @staticmethod
    def _calculate_exponential(lamda: float, N: int) -> Tuple[float, float, float, float, List[float]]:
        """
        Моделирование показательного (экспоненциального) распределения.
        
        :param lamda: параметр λ > 0
        :param N: объём выборки
        :return: (Mx_теор, Dx_теор, Mx_эмп, Dx_эмп, выборка)
        """
        if lamda <= 0:
            raise ValueError("λ must be > 0")
        if N <= 0:
            raise ValueError("N must be > 0")

        # Генерация выборки по формуле: x = -ln(1 - r) / λ
        sample = []
        for _ in range(N):
            r = random.random()  # r ∈ [0, 1)
            x = -math.log(1 - r) / lamda
            sample.append(x)

        # Теоретические значения
        Mx_theor = 1 / lamda
        Dx_theor = 1 / (lamda ** 2)

        # Эмпирические значения
        Mx_emp = sum(sample) / N
        Dx_emp = sum((x - Mx_emp) ** 2 for x in sample) / N

        return Mx_theor, Dx_theor, Mx_emp, Dx_emp, sample

    @staticmethod
    def _calculate_normal(a: float, sigma_square: float, N: int) -> Tuple[float, float, float, float, List[float]]:
        """
        Моделирование нормального распределения.
        
        :param a: параметр a обозначает математическое ожидание
        :param sigma_square: параметр sigma^2 есть дисперсия
        :param N: объём выборки
        :return: (Mx_теор, Dx_теор, Mx_эмп, Dx_эмп, выборка)
        """
        if N <= 0:
            raise ValueError("N должно быть положительным целым числом")
        if sigma_square <= 0:
            raise ValueError("Параметр дисперсии должен быть больше нуля")
        
        # Генерация выборки по формуле: x_i=СУММА[j=1;12](r_j) - 6
        sample=[]
        sigma = math.sqrt(sigma_square)
        for _ in range(N):
            z = sum(random.random() for _ in range(12)) - 6  # Z ~ N(0,1)
            x = a + sigma * z  # X ~ N(a, sigma²)
            sample.append(x)
        
        # Теоретические значения
        Mx_theor = a
        Dx_theor = sigma_square

        # Эмпирические значения
        Mx_emp = sum(sample) / N
        Dx_emp = sum((x - Mx_emp) ** 2 for x in sample) / N

        return Mx_theor, Dx_theor, Mx_emp, Dx_emp, sample