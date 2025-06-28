"""
2. It will have the code related to transformation like
one hot encoding, label encoding etc.
"""

import sys
import os
from dataclasses import dataclass
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj

@dataclass
class DataTransformationConfig:
    preprocessor_obj_path = os.path.join("artifact","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.tranformation_config = DataTransformationConfig()

    def get_data_tranformer(self):
        try:
            numerical_columns = ["writing_score","reading_score"]
            categorical_columns = [
                "gender", "race_ethinicity","parental_level_of_education", "lunch","test_preparation_course"
            ]
            num_pipeline = Pipeline(
                steps=[
                    ("Imputer",SimpleImputer(strategy="meddian")),
                    ("Scaler", StandardScaler())
                ]
            )
            logging.info("Numerical columns has been imputed with mode and Scaled successfully")

            cat_pipeline = Pipeline(
                steps=[
                    ("Imputer",SimpleImputer(strategy="most_frequent")),
                    ("OneHotEncoder",OneHotEncoder()),
                    ("Scaler", StandardScaler())
                ]
            )

            logging.info("Categorical columns has been imputed with mode, encoded with onehotencoding and Scaled successfully")
            
            preprocessor = ColumnTransformer(
                [
                    ("Numerical Pipeline",num_pipeline, numerical_columns),
                    ("Categorical Pipeline",cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor
        
        except:
            raise CustomException(e,sys)
        
    def initiate_data_tranformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("reading training and testing data is completed")

            preprocessing_obj = self.get_data_tranformer()
            target_column_name = "math_score"
            numerical_columns = ["writing_score","reading_score"]


            input_feature_train_df = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]
            
            logging.info("Applying Preprocessor object on training dataframe and testing dataframe")
            
            preprocessed_train_df =preprocessing_obj.fit_transform(input_feature_train_df)
            preprocessed_test_df = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[preprocessed_train_df, np.array(target_feature_train_df)]
            test_arr = np.c_(preprocessed_test_df,np.array(target_feature_test_df))
            
            logging.info("saved Preprocessing object")

            save_obj(
                file_path = self.tranformation_config.preprocessor_obj_path,
                obj = preprocessing_obj
            )




            return(
                train_arr,
                test_arr,
                self.tranformation_config.preprocessor_obj_path
            )




        except Exception as e:
            raise CustomException(e,sys)
            