import pandas as pd 
from Fertilization_prediction.logger import logging
from Fertilization_prediction.exception import fertilizer_exception
import os
import sys
import numpy as np 
import yaml
import dill

def get_collection_as_dataframe()->pd.DataFrame:

    try:

        logging.info(f"Reading the data")
        df = pd.read_csv('Fertilization Prediction.csv')
        logging.info(f"Founds Columns : {df.columns}")

        logging.info(f"Row and columns in df : {df.shape}")

        return df
    except Exception as e:
        raise fertilizer_exception(e,sys)
    
    
