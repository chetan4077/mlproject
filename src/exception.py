# responsible for exception handling
import sys # contains all exceptions/errors occuring in project
import logging
from src.logger import logging

def error_handler(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # gives info about the cur exception.
    '''
    Example =
        try:
            a = 1 / 0
        except Exception as e:
            error_handler(e, sys)
    '''
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,
    exc_tb.tb_lineno,
    str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_handler(error_message,error_detail)
    def __str__(self):
        return self.error_message
    
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Division by Zero")
#         raise CustomException(e,sys)

"""
Example --> model_trainer.py

from src.exception import CustomException
from src.logger import logging
import sys

if __name__ == "__main__":

    try:
        logging.info("Starting model training")
        a = 1 / 0

    except Exception as e:
        logging.error("Error occured during model training")
        raise CustomException(e, sys)

"""