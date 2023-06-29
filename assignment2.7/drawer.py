import matplotlib.pyplot as plt
class Drawer:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def plot_sensor_anomalies(self, sensor, name):
        broken = self.df[self.df['machine_status'] == 'BROKEN']
        recovery = self.df[self.df['machine_status'] == 'RECOVERING']
        normal = self.df[self.df['machine_status'] == 'NORMAL']
        plt.figure(figsize=(20,5))
        plt.plot(recovery[sensor], linestyle='none', marker='o', color='blue', markersize=5)
        plt.plot(broken[sensor], linestyle='none', marker='X', color='red', markersize=14)
        plt.plot(normal[sensor], linestyle ='none', marker = 'o', color='green', markersize=2)
        plt.plot(self.df[sensor], color='grey')
        plt.title(name)
        return plt
    
    def save_plot(self, plt, name):
        plt.savefig(f'images/{name}.png')