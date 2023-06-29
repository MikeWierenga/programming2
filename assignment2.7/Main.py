import os
import data_transformation
import isolationforest
import drawer
import data_searcher
import logger
import numpy as np
import json
def main():
    # looking for new data
    f = open('application.json')
    data = json.load(f)
    input_folder = data['input']
    image_directory = data['img']
    sensors = data['sensors']

    search_data = data_searcher.Data_searcher(input_folder)
    file = search_data.search()
    if file != None:
        log = logger.Log('log', file_name='logfile')
        log.write_to_logger('File has been found')
        data_transform = data_transformation.Data_transformation(f'{input_folder}/{file}')
    
        #transforming data
        fill_data = data_transform.fill_missing_data()
        transformed_data = data_transform.standardscaler()
        X = data_transform.x
       
        log.write_to_logger('Recieved transformed data')
        
        #load model
        model = isolationforest.IsolationForestModel()
        load_model = model.load_model()

        #make prediction
        predictions = load_model.predict(X)
        log.write_to_logger('Received predictions')
        log.write_to_logger('Saving predictions')
        
        #drawing a sensor
        sensordrawer = drawer.Drawer(data_transform.df)
        for sensor  in sensors:
            plot = sensordrawer.plot_sensor_anomalies(sensor, sensor)
            sensordrawer.save_plot(plt=plot, name=sensor)
        log.write_to_logger('Saving image')

        search_data.move_file(destination='data', file=file)
        log.write_to_logger('Resuming listening')
        main()

main()