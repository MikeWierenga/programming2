import os
import data_transformation
import isolationforest
def main():
    data_transform = data_transformation.Data_transformation('data/trainingdata.csv')
    # print(data_transform)
    fill_data = data_transform.fill_missing_data()
    transformed_data = data_transform.standardscaler()
    print(data_transform.x)
    X = data_transform.x
    model = isolationforest.IsolationForestModel()
    model.train_model(X)
    load_model = model.load_model()
    load_model.best_params_
        # terminal enter algorithm to be used 
main()