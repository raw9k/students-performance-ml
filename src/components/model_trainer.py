"""
3. It will have all the code specially for training the model
"""

import os, sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor

from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array,test_array):
        try:
            logging.info("Spliting training and test input data")

            x_train,y_train,x_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )


            models ={
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }


            models_report:dict = evaluate_models(x_train = x_train,y_train = y_train,x_test =  x_test,y_test = y_test, models =models)


            best_model_score = max(sorted(models_report.values()))
            best_model_name = list(models_report.keys())[
                list(models_report.values()).index(best_model_score)
                ]

            best_model = models[best_model_name]
            logging.info("Best model on both training and testing dataset has been found")

            if best_model_score <0.6:
                raise CustomException("No best model found")
            save_object(
                file_path=self.model_trainer_config.trained_model_path,
                obj= best_model
            )


            predicted = best_model.predict(x_test)
            final_r2_score = r2_score(y_test,predicted)

            return final_r2_score
        except Exception as e:
            raise CustomException(e,sys)