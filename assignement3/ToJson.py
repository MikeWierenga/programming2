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
        
        if len( value) == 1:
            return json.dumps("")
        else:
            assert len(keys) == len(value)
            json_line = {keys[index]: value for index, value in enumerate(value)}
            return json_line
        

class Reader:
    def __init__(self, file):
        self.file = file
        self.CsvConverter = CsvConverter(file)
        self.read_line_number = 2


    def get_line(self):
        lines = []
        for line in range(5):
            lines.append(self.CsvConverter.csv_to_json(line+self.read_line_number))

        self.read_line_number +=5       
        return lines


class AverageYear:
    def __init__(self, file):
        self.Reader = Reader(file)
        self.years = []
        self.averages = []

    def calculate_average_year(self):
        dic = {}
        for x in self.Reader.get_line():
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
            dic[key] = sum(value)/ len(value)            
        return dic                
    
    def average_year_data(self, year_averages):
        first_year = year_averages['Year'][0]
        last_year = year_averages['Year'][-1]
        x_value = f'{first_year} - {last_year}'
        
        data = year_averages['months']
        self.years.append(x_value)
        self.averages.append(data)

    def plot_year(self):
        # figure = plt.figure()
        plt.plot(self.years, self.averages)
        print(self.years, self.averages)
        plt.show()


class AverageMonth:
    def __init__(self, file):
        self.Reader = Reader(file)
        self.lines = []

    def calculate_average_month(self):
        dic = {}

        for x in self.Reader.get_line():
            for key,value in x.items():
                if key in ['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                    if key not in dic:
                        dic[key] = [float(value)]
                    dic[key].append(float(value))
        
        #calculate averages
        for key, value in dic.items():
            if key == 'Year':
                continue
            dic[key] = sum(value)/ len(value)            
        return dic

    def average_month_plot(self, month_averages):
        x = [keys for keys in month_averages.keys()][1:]
        y = [item for item in month_averages.values()]
        label = f'{int(y[0][0])} - {int(y[0][-1])}'
        data = y[1:]
       
        # plt.legend(loc="upper left")
        self.lines.append([x, data, label])
        
    def plot_months(self):
        for x in self.lines:
            plt.plot(x[0], x[1], label=x[2])
        plt.legend(loc='upper left')    
        plt.show()





def main():
    month =  AverageMonth('data/dSST.csv')
    year = AverageYear('data/dSST.csv')

    while True:
        start = input("Enter yes or no to continue:")
        if start == 'no':
            break
        elif start == 'month':
            month.average_month_plot(month.calculate_average_month())
            month.plot_months()
        elif start == 'year':
            year.average_year_data(year.calculate_average_year())
            year.plot_year()
    
main()





