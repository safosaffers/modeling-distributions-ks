# Model/Model.py

import random
from typing import List, Tuple
import math
from scipy import stats
import numpy as np


class Model:
    sample_uniform = []
    sample_exponential = []
    sample_normal = []
    
    def store_sample_uniform(self, sample):
        """Store uniform distribution sample"""
        self.sample_uniform = sample
    
    def store_sample_exponential(self, sample):
        """Store exponential distribution sample"""
        self.sample_exponential = sample
    
    def store_sample_normal(self, sample):
        """Store normal distribution sample"""
        self.sample_normal = sample
    
    def get_sample_by_type(self, distribution_type):
        """Get sample by distribution type"""
        if distribution_type == "Равномерное распределение":
            return self.sample_uniform
        elif distribution_type == "Нормальное распределение":
            return self.sample_normal
        elif distribution_type == "Показательное распределение":
            return self.sample_exponential
        else:
            return []
    
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

    @staticmethod
    def calculate_pearson_criterion(sample: List[float], alpha: float = 0.05, num_intervals: int = None) -> dict:
        """
        Вычисляет критерий Пирсона для проверки гипотезы о виде распределения.
        
        :param sample: выборка случайных величин
        :param alpha: уровень значимости (по умолчанию 0.05)
        :param num_intervals: количество интервалов для группировки данных (если None, будет рассчитано автоматически)
        :return: словарь с результатами критерия Пирсона
        """
        if not sample:
            raise ValueError("Выборка не должна быть пустой")
        
        if len(sample) < 5:
            raise ValueError("Выборка должна содержать не менее 5 элементов")
        
        if not (0 < alpha < 1):
            raise ValueError("Уровень значимости должен быть в интервале (0, 1)")
        
        n = len(sample)
        
        # Выбираем количество интервалов
        if num_intervals is None:
            # Эмпирическое правило: num_intervals = sqrt(n) или 2 * sqrt(n)
            # Но не менее 5 и не более n//2
            num_intervals = max(5, int(math.sqrt(n)))
        
        # Проверка, чтобы интервалов было не больше, чем элементов в выборке
        num_intervals = min(num_intervals, n // 2)
        
        if num_intervals < 5:
            raise ValueError("Размер выборки слишком мал для корректного применения критерия Пирсона")
        
        # Определяем границы интервалов
        min_val = min(sample)
        max_val = max(sample)
        
        # Если все значения одинаковы, расширяем диапазон
        if min_val == max_val:
            min_val -= 0.5
            max_val += 0.5
        
        interval_width = (max_val - min_val) / num_intervals
        
        # Границы интервалов (левая граница включена, правая - нет, кроме последнего)
        interval_bounds = [min_val + i * interval_width for i in range(num_intervals + 1)]
        
        # Исправляем последнюю границу, чтобы включить все значения
        interval_bounds[-1] = max_val
        
        # Вычисляем наблюдаемые частоты
        observed_freq = [0] * num_intervals
        
        for value in sample:
            # Находим интервал для текущего значения
            assigned = False
            for i in range(num_intervals):
                if i == num_intervals - 1:  # Последний интервал - включает верхнюю границу
                    if interval_bounds[i] <= value <= interval_bounds[i + 1]:
                        observed_freq[i] += 1
                        assigned = True
                        break
                else:  # Другие интервалы - левая граница включена, правая - нет
                    if interval_bounds[i] <= value < interval_bounds[i + 1]:
                        observed_freq[i] += 1
                        assigned = True
                        break
            
            # Если не попало ни в один интервал (маловероятно, но на всякий случай)
            if not assigned:
                observed_freq[-1] += 1  # Относим к последнему интервалу
        
        # Вычисляем ожидаемые частоты (предполагаем равномерное распределение)
        expected_freq = [n / num_intervals] * num_intervals
        
        # Вычисляем статистику критерия Пирсона
        chi_squared_stat = 0
        for obs, exp in zip(observed_freq, expected_freq):
            if exp > 0:  # Избегаем деления на 0
                chi_squared_stat += (obs - exp) ** 2 / exp
            else:
                # В редких случаях может быть нулевая ожидаемая частота
                chi_squared_stat = float('inf')
        
        # Степеней свободы = число интервалов - 1 (для равномерного распределения)
        # В общем случае: число интервалов - 1 - число оцененных параметров
        degrees_of_freedom = num_intervals - 1
        
        # Критическое значение из хи-квадрат распределения
        critical_value = stats.chi2.ppf(1 - alpha, degrees_of_freedom)
        
        # p-значение
        p_value = 1 - stats.chi2.cdf(chi_squared_stat, degrees_of_freedom)
        
        # Решение: отвергаем гипотезу, если статистика больше критического значения
        reject_hypothesis = chi_squared_stat > critical_value
        
        # Результат
        result_info = {
            "n": n,
            "num_intervals": num_intervals,
            "interval_bounds": interval_bounds,
            "observed_frequencies": observed_freq,
            "expected_frequencies": expected_freq,
            "chi_squared_statistic": chi_squared_stat,
            "critical_value": critical_value,
            "degrees_of_freedom": degrees_of_freedom,
            "alpha": alpha,
            "p_value": p_value,
            "reject_hypothesis": reject_hypothesis,
            "hypothesis_accepted": not reject_hypothesis,
            "message": f"Гипотеза о виде распределения {'принята' if not reject_hypothesis else 'отвергнута'} на уровне значимости α={alpha}"
        }
        
        return result_info

    @staticmethod
    def calculate_pearson_criterion_for_distribution(sample: List[float], distribution_type: str) -> dict:
        """
        Вычисляет критерий Пирсона для проверки гипотезы о виде распределения.
        
        :param sample: выборка случайных величин
        :param distribution_type: тип распределения ("Равномерное распределение", "Нормальное распределение", "Показательное распределение")
        :return: словарь с результатами критерия Пирсона
        """
        if not sample:
            raise ValueError("Выборка не должна быть пустой")
        
        if len(sample) < 5:
            raise ValueError("Выборка должна содержать не менее 5 элементов")
        
        from scipy import stats
        import numpy as np
        
        n = len(sample)
        
        # Определяем количество интервалов k ≈ sqrt(n), но не менее 5 и не более 20
        k = max(5, min(20, int(math.sqrt(n))))
        
        # Оценка параметров распределения
        if distribution_type == "Нормальное распределение":
            # Для нормального: mu = среднее(data), sigma = стандартное_отклонение(data, ddof=1)
            mu = np.mean(sample)
            sigma = np.std(sample, ddof=1)
            r = 2  # Оценено 2 параметра (mu, sigma)
            
        elif distribution_type == "Равномерное распределение":
            # Для равномерного: a = min(data), b = max(data)
            a = min(sample)
            b = max(sample)
            r = 2  # Оценено 2 параметра (a, b)
            
        elif distribution_type == "Показательное распределение":
            # Для показательного: lambda = 1 / среднее(data)
            lambda_param = 1 / np.mean(sample)
            r = 1  # Оценен 1 параметр (lambda)
        else:
            raise ValueError(f"Неизвестный тип распределения: {distribution_type}")
        
        # Создаем гистограмму для получения наблюдаемых частот
        observed_freq, bin_edges = np.histogram(sample, bins=k)
        
        # Вычисляем ожидаемые частоты
        expected_freq = []
        
        if distribution_type == "Нормальное распределение":
            # Вычисляем ожидаемые вероятности для каждого интервала
            for i in range(k):
                # Вероятность попадания в интервал [bin_edges[i], bin_edges[i+1]]
                prob = stats.norm.cdf(bin_edges[i+1], loc=mu, scale=sigma) - \
                       stats.norm.cdf(bin_edges[i], loc=mu, scale=sigma)
                expected_freq.append(n * prob)
                
        elif distribution_type == "Равномерное распределение":
            # Вычисляем ожидаемые вероятности для каждого интервала
            for i in range(k):
                # Вероятность попадания в интервал [bin_edges[i], bin_edges[i+1]]
                prob = stats.uniform.cdf(bin_edges[i+1], loc=a, scale=b-a) - \
                       stats.uniform.cdf(bin_edges[i], loc=a, scale=b-a)
                expected_freq.append(n * prob)
                
        elif distribution_type == "Показательное распределение":
            # Вычисляем ожидаемые вероятности для каждого интервала
            for i in range(k):
                # Вероятность попадания в интервал [bin_edges[i], bin_edges[i+1]]
                # Для показательного распределения x >= 0
                left_edge = max(0, bin_edges[i])
                right_edge = bin_edges[i+1] 
                prob = stats.expon.cdf(right_edge, scale=1/lambda_param) - \
                       stats.expon.cdf(left_edge, scale=1/lambda_param)
                expected_freq.append(n * prob)
        
        # Объединяем интервалы, где ожидаемая частота < 5
        # Это нужно делать аккуратно - объединять соседние интервалы
        final_observed_freq = []
        final_expected_freq = []
        
        i = 0
        while i < len(observed_freq):
            obs_freq = observed_freq[i]
            exp_freq = expected_freq[i]
            
            # Если текущая ожидаемая частота меньше 5, объединяем с соседними
            while exp_freq < 5 and i < len(observed_freq) - 1:
                i += 1
                if i < len(observed_freq):
                    obs_freq += observed_freq[i]
                    exp_freq += expected_freq[i]
            
            final_observed_freq.append(obs_freq)
            final_expected_freq.append(exp_freq)
            i += 1
        
        # Проверяем, что количество интервалов не слишком мало
        if len(final_observed_freq) < 3:
            raise ValueError("Недостаточно интервалов для корректного применения критерия Пирсона")
        
        # Обновляем количество интервалов после объединения
        k = len(final_observed_freq)
        
        # Вычисляем статистику критерия Пирсона
        chi_squared_stat = 0
        for obs, exp in zip(final_observed_freq, final_expected_freq):
            if exp > 0:
                chi_squared_stat += (obs - exp) ** 2 / exp
            else:
                chi_squared_stat = float('inf')  # Если ожидаемая частота 0
        
        # Число степеней свободы: df = k - 1 - r
        df = k - 1 - r
        
        if df <= 0:
            raise ValueError("Число степеней свободы должно быть положительным")
        
        # p-значение
        p_value = 1 - stats.chi2.cdf(chi_squared_stat, df)
        
        # Решение: если p < 0.05 - гипотеза отвергается
        reject_hypothesis = p_value < 0.05
        
        if reject_hypothesis:
            conclusion = "Гипотеза о соответствии распределению отвергается"
        else:
            conclusion = "Гипотеза о соответствии распределению не противоречит данным"
        
        # Результат
        result_info = {
            "n": n,
            "k": k,
            "bin_edges": bin_edges.tolist() if isinstance(bin_edges, np.ndarray) else list(bin_edges),
            "observed_frequencies": final_observed_freq,
            "expected_frequencies": final_expected_freq,
            "chi_squared_statistic": chi_squared_stat,
            "degrees_of_freedom": df,
            "p_value": p_value,
            "reject_hypothesis": reject_hypothesis,
            "conclusion": conclusion,
            "distribution_type": distribution_type,
            "parameters": {}
        }
        
        # Сохраняем оценённые параметры
        if distribution_type == "Нормальное распределение":
            result_info["parameters"] = {"mu": mu, "sigma": sigma}
        elif distribution_type == "Равномерное распределение":
            result_info["parameters"] = {"a": a, "b": b}
        elif distribution_type == "Показательное распределение":
            result_info["parameters"] = {"lambda": lambda_param}
        
        return result_info