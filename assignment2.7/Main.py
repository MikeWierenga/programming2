import os
import data_transformation
import isolationforest
import drawer
def main():
    data_transform = data_transformation.Data_transformation('data/trainingdata.csv')
    
    #drawing a sensor
    sensordrawer = drawer.Drawer(data_transform.df)
    print(sensordrawer.plot_sensor_anomalies('sensor_00', 'sensor 0'))
    test = sensordrawer.plot_sensor_anomalies('sensor_00', 'sensor 0')
    test,show()

    #transforming data
    fill_data = data_transform.fill_missing_data()
    transformed_data = data_transform.standardscaler()
    X = data_transform.x
    #training a model
    model = isolationforest.IsolationForestModel()
    model.train_model(X)
    #loading a model 
    load_model = model.load_model()
    print(load_model.best_params_)
        # terminal enter algorithm to be used 
   
main()