# # this file will do cleaning/transformation
# # Importing Libraries
# import sys
# import os
# import pandas as pd
# import numpy as np
# from dataclasses import dataclass
# from src.exception import CustomException
# from src.logger import logging
# from src.utils import save_object
# #from src.components.data_ingestion import DataIngestion
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder, StandardScaler
# from sklearn.impute import SimpleImputer
# # import sklearn
# from sklearn.pipeline import Pipeline


# @dataclass
# class DataTransformationConfig:
#     preprocessing_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")


# class DataTransformation:
#     def __init__(self):
#         self.data_transformation_config = DataTransformationConfig()

#     def get_transformer_object(self):
#         try:
#             # logging.info("Getting the train data path")
#             # obj = DataIngestion()
#             # train_data_path, test_data_path = obj.initiate_data_ingestion()

#             # logging.info("Read training data from artifacts")
#             # data = pd.read_csv(train_data_path)

#             # logging.info("Adding 2 new col Total and Average Marks in DataSet")
#             # data["total"] = (
#             #     data["math score"] + data["reading score"] + data["writing score"]
#             # )
#             # data["average"] = data["total"] / 3

#             logging.info("Separating Numerical and Categorical Features")
#             num_features = ["writing score", "reading score"]
#             cat_features = [
#                 "gender",
#                 "race ethnicity",
#                 "parental level of education",
#                 "lunch",
#                 "test preparation course",
#             ]

#             logging.info("Creating numerical pipeline")
#             num_pipeline = Pipeline(
#                 steps=[
#                     ("imputer", SimpleImputer(strategy="median")),
#                     ("standard scaler",StandardScaler()),
#                 ]
#             )

#             logging.info("Creating categorical pipeline")
#             cat_pipeline = Pipeline(
#                 steps=[
#                     ("imputer", SimpleImputer(strategy="most_frequent")),
#                     # ("imputer", SimpleImputer(strategy="mode"))
#                     ("one hot encoder", OneHotEncoder()),
#                     # ("standard scaler",StandardScaler())
#                 ]
#             )
#             logging.info("Numerical and categorical Pipeline done")
#             preprocessor = ColumnTransformer(
#                 [
#                     # Format - name, pipeline, data jispe karna hai
#                     ("num_pipeline", num_pipeline, num_features),
#                     ("cat_pipeline", cat_pipeline, cat_features)
#                 ]
#             )

#             return preprocessor
#         except Exception as e:
#             raise CustomException(e, sys)

#     def initiate_data_transformation(self, train_path, test_path):
#         try:
#             logging.info('Reading training nd testing data')
#             train_df=pd.read_csv(train_path)
#             test_df=pd.read_csv(test_path)

#             logging.info('Obtaining Preprocessing Object')
#             preprocessing_obj = self.get_transformer_object()

#             target_col='math score'
#             num_col=['writing score', 'reading score']

#             logging.info('Creating input, target feature for training nd test data')
#             input_feature_train_df=train_df.drop(columns=[target_col])
#             target_feature_train_df=train_df[target_col]
#             input_feature_test_df = test_df.drop(columns=[target_col])
#             target_feature_test_df = test_df[target_col]
#             logging.info('Created input, target feature for training nd test data')

#             logging.info('Applying preprocessing obj on training nd test data')
#             # fit_transform -> learns params from data nd applies transformation from learnt params
#             # transform -> applies transformation directly using learnt params
#             input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
#             input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

#             train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
#             test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
#             logging.info('saved preproessing obj')

#             save_object(
#                 file_info=self.data_transformation_config.preprocessor_obj_file_path,
#                 obj=preprocessing_obj
#             )

#             return(
#                 train_arr,
#                 test_arr,
#                 self.data_transformation_config.preprocessor_obj_file_path
#             )
#         except Exception as e:
#             raise CustomException(e,sys)

import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing score", "reading score"]
            categorical_columns = [
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course",
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math score"
            numerical_columns = ["writing score", "reading score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_info=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)



