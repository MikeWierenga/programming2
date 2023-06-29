from sklearn import svm
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, f1_score
import numpy as np
from joblib import dump, load
class IsolationForestModel:
    def __init__(self):
        self.isolationForest = IsolationForest() 
        self.scorer = make_scorer(f1_score)
    def train_model(self, X):
        parameters = {'n_estimators': np.arange(1,100, 25),
              'contamination': ['auto'],
              'max_samples': ['auto'],
              'bootstrap': [True, False]
        }
        clf = GridSearchCV(self.isolationForest, parameters, scoring=self.scorer_f)
        model = clf.fit(X)

        dump(clf, 'isolation.joblib')


    def load_model(self):
        return load('isolation.joblib')

    def predict_value(self):
        pass

    def scorer_f(self, estimator, X):
        return np.mean(estimator.score_samples(X))