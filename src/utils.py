# This will have the utilities/functions like connecting to any sql or mongo db
# or something like saving code in cloud or shipping as docker etc
import os
import sys
import dill
from src.exception import CustomException

def save_object(file_info,obj):
    try:
        dir_path=os.path.dirname(file_info)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_info ,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)