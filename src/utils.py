from ast import literal_eval
from datetime import datetime

def json_file_converter(file_path: str) -> dict:
    """ Opens a json file and returns a corresponding python list or dictionary object """
    with open(file_path, "r") as json_file:
        json_str = json_file.read()
    python_str = json_str.replace("true", "True").replace("false", "False").replace("null", "None")
    python_dict = literal_eval(python_str)
    return python_dict

def epoch_to_year(posix_time: str) -> str:
    """ Takes a timestamp in posix format and returns the corresponding year """
    year = datetime.utcfromtimestamp(posix_time).strftime('%Y')
    return year

def number_prettify(number: int) -> str:
    """ Takes numbers (int or str format), and if they are too big, shortens them in readable format and returns string. """
    # just in case number provided is a string
    number = int(number)
    if number > 1000000:
        number = str(round(number/1000000, 1)) + "M"
    elif number > 1000:
        number = str(round(number/1000, 1)) + "K"
    else:
        number = str(number)
    number = number.replace(".0", "")
    return number