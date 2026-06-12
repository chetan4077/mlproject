# This will have the utilities/functions like connecting to any sql or mongo db
# or something like saving code in cloud or shipping as docker etc
import os
import sys
import dill
from sklearn.metrics import r2_score
from src.exception import CustomException

# Creates a pickle object
def save_object(file_info,obj):
    try:
        dir_path=os.path.dirname(file_info)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_info ,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)

# Evaluates R2 Score of each model    
def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        result={}
        for name,model in models.items():
            model.fit(X_train,y_train)
            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)
            train_score=r2_score(y_train,y_train_pred)
            test_score=r2_score(y_test,y_test_pred)
            result[name]=test_score
        return result
    except Exception as e:
        raise CustomException(e,sys)