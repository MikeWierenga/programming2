import linecache as lc
import json
import pandas as pd
class CsvConverter:
    
    def __init__(self, file_reader):
        self.file = file_reader
        self.first_line = lc.getline(file_reader, 1).split(',')

    def csv_to_json(self, line):
        keys = self.first_line
    
        value = lc.getline(self.file, line).split(',')
        
        if len( value) == 1:
            # print([])
            return json.dumps([])
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
        pass
    
class AverageMonth:
    def __init__(self, file):
        self.Reader = Reader(file)

    def calculate_average_month(self):
        averages = []
        values = [float(line[month]) for line in self.Reader.get_line()]
        averages.append(sum(values) / len(values))
        
test =   AverageMonth('data/dSST.csv')
print(test.calculate_average_month("Jan"))
# print(test.get_line())





