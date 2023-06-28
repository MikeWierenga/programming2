import pandas as pd
class Data_manager:
    def __init__(self, data):
        # timestamp column is of type object needs to change to timestamp
        self.df = pd.read_csv(data)
        self.df = self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        print(self.df.dtypes)

    def split_data(self):
        trainingdata = self.df[self.df['timestamp'].dt.month <=6]
        predictingdata_july = self.df[self.df['timestamp'].dt.month == 7]
        predictingdata_august = self.df[self.df['timestamp'].dt.month == 8]
        return trainingdata, predictingdata_july, predictingdata_august
    
    def df_to_csv(self, data, name):
        data.to_csv(f'data/{name}.csv')

test = Data_manager('data/sensor.csv')
training, predictiondata_july, predictingdata_august = test.split_data()
test.df_to_csv(training, 'trainingdata')
test.df_to_csv(predictiondata_july, 'predictiondata_july')
test.df_to_csv(predictingdata_august, 'predictingdata_august')