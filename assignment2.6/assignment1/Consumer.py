from abc import ABCMeta, abstractmethod
import json
import functools
from matplotlib import pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class Consumer(metaclass=ABCMeta):
    id_gen = 0

    def __init__(self):
        self.id = Consumer.id_gen
        Consumer.id_gen += 1

    @abstractmethod
    def update(self, json_lines):
        pass

    @staticmethod
    def build_plot(x, y, x_label, y_label, title):
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.plot(x, y)
        plt.show()


class AverageYear(Consumer):
    @staticmethod
    def get_year_average(line):
        month_avs = map(lambda month: float(line[month]), months)
        return functools.reduce(lambda m1, m2: m1 + m2, month_avs) / 12

    def update(self, json_lines):
        x_y = list(zip(*[(line['Year'], AverageYear.get_year_average(line)) for line in json.loads(json_lines)]))
        x, y = list(x_y[0]), list(x_y[1])
        Consumer.build_plot(x, y, 'years', 'anomalies', 'AverageYear')


class AverageMonth(Consumer):
    def update(self, json_lines):
        sum_months = [0] * len(months)
        loaded_json = json.loads(json_lines)
        for line in loaded_json:
            sum_months = [sum_months[i] + float(line[months[i]]) for i in range(len(months))]
        y = [sum_months[i] / len(loaded_json) for i in range(len(months))]
        Consumer.build_plot(months, y, 'months', 'anomalies', 'AverageMonth')
