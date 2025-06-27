"""
1. Data ingestion is the process of reading data from some
database.
It will have all the code related to reading the data

"""
import sys
import os

from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass 