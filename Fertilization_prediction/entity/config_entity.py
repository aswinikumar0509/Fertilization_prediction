import os , sys
from Fertilization_prediction.logger import logging
from Fertilization_prediction.exception import fertilizer_exception
from datetime import datetime

FILE_NAME ="Fertilizer Prediction.csv"
Train_File_Name ="train.csv"
Test_File_Name = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):

        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")

        except Exception as e:
            raise fertilizer_exception(e,sys)
        
class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:

            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",Train_File_Name)
            self.test_file_path = os.path.join(self.data_ingestion_dir,Test_File_Name)

            self.test_size = 0.2
        except Exception as e :
            raise fertilizer_exception(e,sys)
        

    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise fertilizer_exception(e,sys)
        