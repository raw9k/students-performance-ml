"""
Contain function which can be used in for entire application
"""

import os, sys, numpy as np, pandas as pd, dill
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(x_train, y_train, x_test,y_test, models,param):
    try:
        r2_report = {}
        for i in range(len(models)):
            model= list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv = 3, n_jobs= -1 , verbose=3)
            gs.fit(x_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train,y_train)

            y_pred_train = model.predict(x_train)
            y_pred_test = model.predict(x_test)

            train_model_score = r2_score(y_train,y_pred_train)
            test_model_score = r2_score(y_test,y_pred_test)

            r2_report[list(models.keys())[i]] = test_model_score
            
        return r2_report

    except Exception as e:
        raise CustomException(e,sys)
