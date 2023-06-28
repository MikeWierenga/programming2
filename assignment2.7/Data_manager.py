import pandas as pd
class Data_manager:
    def __init__(self, data):
        # timestamp column is of type object needs to change to timestamp
        self.df = pd.read_csv(data)
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])


    def split_data(self):
        trainingdata = self.df[self.df['timestamp'].dt.month <=6]
        predictingdata = self.df[self.df['timestamp'].dt.month > 6]
        return trainingdata, predictingdata
    
    def df_to_csv(self, data, name):
        data.to_csv(f'data/{name}.csv')

test = Data_manager('data/sensor.csv')
training, predictiondata = test.split_data()
test.df_to_csv(training, 'trainingdata')
test.df_to_csv(predictiondata, 'predictiondata')