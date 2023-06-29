from sklearn.preprocessing import StandardScaler
import pandas as pd
class Data_transformation:
    """
    This is the location where the 
    data is stored and could be processed if needed
    """
    def __init__(self, data):
        self.df = pd.read_csv(data)
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        self.df.drop(['sensor_15', 'sensor_50'],inplace=True, axis=1)
        self.x = self.df.iloc[:,3:-1]
        

       
    def fill_missing_data(self):
        self.x = self.x.fillna(method = 'ffill')


    def standardscaler(self):
        scaler = StandardScaler()
        self.x = scaler.fit_transform(self.x)
        
    def outliers_fraction(self):
         normal_rows = self.df[df['machine_status']=='NORMAL']
         outliers_fraction = 1 - (len(normal_rows)/(len(self.df)))
         return outliers_fraction 