# responsible for exceptopn handling
import os
import sys # contains all exceptions/errors occuring in project

def error_handler(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()