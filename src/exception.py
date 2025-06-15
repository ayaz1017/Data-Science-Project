

import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    exc_type, exc_obj, exc_tb = error_detail.exc_info()
    if exc_tb is None:
        return f"Error occurred: {str(error)}"
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return f"{self.__class__.__name__}({self.error_message})"
