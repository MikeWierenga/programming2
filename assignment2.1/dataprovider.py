import pandas as pd
class DataProvider:
    def __init__(self):
        print('test')
        self.df = pd.read_csv("dSST.csv")    
    
    def get_data(self, *kwargs):
        data = ''
        if len(kwargs) == 0:
            data = self.df
        elif len(kwargs) == 1 and isinstance(kwargs[0], int):

            data = self.df[self.df['Year'] == kwargs[0]]
        elif len(kwargs) == 1 and isinstance(kwargs[0], list):
            data = self.df.loc[(self.df['Year'] >= kwargs[0][0]) & (self.df['Year'] <= kwargs[0][1])]
        return data.T.to_json()
    
    