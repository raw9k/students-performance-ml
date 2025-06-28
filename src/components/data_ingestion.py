"""
1. Data ingestion is the process of reading data from some
database.
It will have all the code related to reading the data

"""
import sys
import os

from src.exception import CustomException
from src.logger import logging

import pandas as pd # type: ignore
from sklearn.model_selection import train_test_split # type: ignore

from dataclasses import dataclass

@dataclass
class DataIngestion_config:
    logging.info("Entered into data ingestion config")
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestion_config()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df = pd.read_csv(r"notebook\data\stud.csv")
            logging.info("Dataset has been read as dataframe df")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train Test Split has initiated")
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info("Ingestion of data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ =="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()







""" Code Explainer:

@dataclass is a decorator from Python's dataclasses module that automatically adds special methods to a class like:

__init__() - constructor
__repr__() - string representation
__eq__() - equality comparison


DataIngestion_config class is intended to hold paths to the train, test, and raw data files.

train_data_path: str = os.path.join("artifacts", "train.csv"):
---> os.path.join(...) joins the directory "artifacts" and file "train.csv" using the correct path separator (cross-platform).

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestion_config()

--> Inside __init__(), you create an instance of DataIngestion_config, which holds paths (e.g., train, test, raw).

--> self.ingestion_config will store those paths so the rest of the class can access them.

os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

-->  1. self.ingestion_config.train_data_path
This accesses the train_data_path attribute from the config class you defined earlier.

--> 2. os.path.dirname(...)
Extracts only the directory path from the full file path.

        # os.path.dirname("artifacts/train.csv")  ➝  "artifacts"
Intuition: Before saving a file to "artifacts/train.csv", you must ensure the folder "artifacts" exists.

--> 3. os.makedirs(...)
This creates a directory (or nested directories) if they don’t already exist.
For example:

        # os.makedirs("artifacts/data/temp")  # Creates all 3 levels if needed
Intuition: You never want to assume the folder already exists — this avoids FileNotFoundError.

--> 4. exist_ok=True
Without this, if the directory already exists, Python would throw an error:
    FileExistsError: [Errno 17] File exists

if __name__ =="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

if __name__ == "__main__":
This checks:
“Is this Python file being run directly by the user?”
--> If yes, the block runs.
--> If the file is being imported into another module, this block does not run.

obj = DataIngestion()
--> This creates an object (instance) of your DataIngestion class.

-->This triggers the __init__() method of DataIngestion, which:
    -->Initializes self.ingestion_config using your DataIngestion_config() class.
    -->Sets up paths like train_data_path, test_data_path, etc.

    
obj.initiate_data_ingestion()
    This calls your method that does all the work:

    Reads the raw CSV
    Creates folders if needed
    Saves raw, train, and test data
    Logs each step
    Returns paths to the saved files



"""