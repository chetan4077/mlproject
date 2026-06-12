#Whole model training will come here
import os
import sys

from dataclasses import dataclass
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
    )
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info('Splitting data in training nd test data')
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
                )

            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Nearest Neighbor Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "XG Boost Regressor": XGBRegressor(),
                "Cat Boost Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor()
            }
            model_res:dict=evaluate_models(X_train,y_train,X_test,y_test,models)

            best_model_name=max(model_res,key=model_res.get)
            best_model_score=model_res[best_model_name]
            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise CustomException('No best Model found having R2 Score > 60 %')
            logging.info("Best model and it's R2 Score found")

            save_object(
                file_info=self.model_trainer_config.trained_model_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)
            r2_sq=r2_score(y_test,predicted)
            return r2_sq, best_model
        except Exception as e:
            raise CustomException(e,sys)
