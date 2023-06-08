import linecache as lc
import json
import pandas as pd
import matplotlib.pyplot as plt
class CsvConverter:
    
    def __init__(self, file_reader):
        self.file = file_reader
        self.first_line = lc.getline(file_reader, 1).split(',')

    def csv_to_json(self, line):
        keys = self.first_line
    
        value = lc.getline(self.file, line).split(',')
        
        if len(value) == 1:
            return json.dumps("")
        else:
            assert len(keys) == len(value)
            json_line = {keys[index]: value for index, value in enumerate(value)}
            return json_line
        

class Reader:
    def __init__(self, file):
        self.file = file
        self.obs = []
        self.lines = []
        self.CsvConverter = CsvConverter(file)
        self.read_line_number = 2

    def get_line(self):
        for line in range(5):
            self.lines.append(self.CsvConverter.csv_to_json(line+self.read_line_number))

        self.read_line_number +=5       
        self.notify_observers()

    def add_observer(self, observer):
        self.obs.append(observer)

    def remove_observer(self, observer):
        pass

    def notify_observers(self):
        for observer in self.obs:
            observer.update(self)

    

        
class AverageYear:
    def __init__(self):
        self.data = []
        self.years = []
        self.averages = []
        self.times = 0
        self.five_years = 0

    def calculate_average_year(self):
        dic = {}
        for x in self.data:
            for key, value in x.items():
                if key == 'Year':
                    if key not in dic:
                        dic[key] = [int(value)]
                    else:    
                        dic[key].append(int(value))
                if key in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                    if "months" not in dic:
          
                        dic["months"] = [float(value)]
                    else:
                        dic["months"].append(float(value))
        #calculate averages
  
        for key, value in dic.items():
            if key == 'Year':
                continue
            dic[key] = sum(value[self.five_years:])/ len(value[self.five_years:])    
        self.five_years +=60             
        return dic                
    
    def average_year_data(self, year_averages):
        
        first_year = year_averages['Year'][self.times]
        
        last_year = year_averages['Year'][-1]
        x_value = f'{first_year} - {last_year}'
        
        data = year_averages['months']
        
        self.years.append(x_value)
        self.averages.append(data)
        self.times += 5

    def plot_year(self):
        plt.plot(self.years, self.averages)
        plt.show()

    def update(self, observable):
        
        self.data = observable.lines
        self.average_year_data(self.calculate_average_year())


class AverageMonth:
    def __init__(self):
        self.data = []
        self.plot_data = []
        self.times = 0


    def calculate_average_month(self):
        dic = {}

        for x in self.data:
            for key,value in x.items():
                if key == 'Year':
                    if key not in dic:
                        dic[key] = [int(value)]
                    else:    
                        dic[key].append(int(value))
                if key in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                    if key not in dic:
                        dic[key] = [float(value)]
                    dic[key].append(float(value))
        
        #calculate averages
        for key, value in dic.items():
            if key == 'Year':
                continue
            dic[key] = sum(value)/ len(value)     
          
        print(dic)
        return dic

    def average_month_plot(self, month_averages):
        x = [keys for keys in month_averages.keys()][1:]
        y = [item for item in month_averages.values()]

        label = f'{int(y[0][self.times])} - {int(y[0][-1])}'
        data = y[1:]

        self.times += 5
        self.plot_data.append([x, data, label])
    
    def plot_months(self):

        for x in self.plot_data:
            plt.plot(x[0], x[1], label=x[2])
        plt.legend(loc='upper left')    
        plt.show()

    def update(self, observable):
        self.data = observable.lines
        self.average_month_plot(self.calculate_average_month())




def main():
    producer = Reader('data/dSST.csv')
    monthConsumer = AverageMonth()
    yearConsumer = AverageYear()

    producer.add_observer(monthConsumer)
    producer.add_observer(yearConsumer)
    while True:
        start = input("Enter yes or no to continue:")
        if start == 'no':
            break
        if start == 'yes':
            producer.get_line()
            monthConsumer.plot_months()
            yearConsumer.plot_year()
main()
