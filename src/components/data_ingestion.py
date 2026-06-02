# # this file will work on reading data
# import os
# import sys
# import pandas as pd
# from src.exception import CustomException
# from src.logger import logging
# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig

# from sklearn.model_selection import train_test_split
# from dataclasses import dataclass

# @dataclass # helps u define variable directly without __init__()
# class DataIngestionConfig:
#     train_data_path:str=os.path.join('artifacts','train.csv') # training data will come here later
#     test_data_path:str=os.path.join('artifacts','test.csv') # testing data will come here later
#     raw_data_path:str=os.path.join('artifacts','data.csv') # testing data will come here later

# class DataIngestion:
#     def __init__(self):
#         self.ingestion_config=DataIngestionConfig()

#     def initiate_data_ingestion(self):
#         logging.info('Entered Data Ingestion method')
#         try:
#             df = pd.read_csv(r'notebook\data\StudentsPerformance.csv')
#             logging.info('Read the dataset as dataFrame')

#             folder_name=os.path.dirname(self.ingestion_config.train_data_path)
#             os.makedirs(folder_name,exist_ok=True)

#             df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

#             logging.info('Train Test Split Initiated')
#             train_data,test_data=train_test_split(df, test_size=0.25, random_state=42)
#             train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
#             test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
#             logging.info('Data Ingestion Completed')
#             return(
#                 self.ingestion_config.train_data_path,
#                 self.ingestion_config.test_data_path
#             ) # This returned data will help us in data_transformation file to transform data
#         except Exception as e:
#             raise CustomException(e,sys)
        
# if __name__=='__main__':
#     obj=DataIngestion()
#     train_data,test_data=obj.initiate_data_ingestion()

#     data_transformation=DataTransformation()
#     data_transformation.initiate_data_transformation(train_data, test_data)

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    # modeltrainer=ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr,test_arr))


