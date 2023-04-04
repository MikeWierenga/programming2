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
            # print([])
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
                        print(key)
                        dic["months"] = [float(value)]
                    else:
                        dic["months"].append(float(value))
        #calculate averages
        for key, value in dic.items():
            if key == 'Year':
                continue
            dic[key] = sum(value)/ len(value)            
        return dic                
    
class AverageMonth:
    def __init__(self, file):
        self.Reader = Reader(file)

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
        return  [x,data, label]
       


test =   AverageYear('data/dSST.csv')
"""
def main():
    start = input("Enter yes or no to continue:")
 
    while start != 'no':
        print(start)
        toplot = test.average_month_plot(test.calculate_average_month())
        plt.plot(toplot[0], toplot[1], label=toplot[2])
        plt.legend(loc="upper left")
        start = ''
        # plt.show()
        main()
    plt.show()    
    return "im done"
main()
"""
print(test.calculate_average_year())
# plt.show()


# test.calculate_average_month()
# test = Reader('data/dSST.csv')

# print(test.get_line())





