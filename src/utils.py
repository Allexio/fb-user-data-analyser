from ast import literal_eval
from datetime import datetime

def json_file_converter(file_path: str) -> dict:
    """ Opens a json file and returns a corresponding python list or dictionary object """
    with open(file_path, "r") as json_file:
        json_str = json_file.read()
    python_str = json_str.replace("true", "True").replace("false", "False").replace("null", "None")
    python_dict = literal_eval(python_str)
    return python_dict

def epoch_to_year(posix_time: int) -> str:
    """ Takes a timestamp in posix format and returns the corresponding year """
    # just in case number provided is a string
    posix_time = int(posix_time)
    year = datetime.utcfromtimestamp(posix_time).strftime('%Y')
    month = datetime.utcfromtimestamp(posix_time).strftime('%m')
    print(month)
    return year

def epoch_to_year_and_month(posix_time: int) -> str:
    """ Takes a timestamp in posix format and returns the corresponding year and month"""
    # just in case number provided is a string
    posix_time = int(posix_time)
    year = datetime.utcfromtimestamp(posix_time).strftime('%Y')
    month = datetime.utcfromtimestamp(posix_time).strftime('%m')
    month_name = number_to_month_name(month)
    return month_name, year

def number_to_month_name(month_int: str) -> str:
    """ Takes a month as a 0 padded str and returns a string """
    month_str = ""
    if month_int == "01":
        month_str = "January"
    elif month_int == "02":
        month_str = "February"
    elif month_int == "03":
        month_str = "March"
    elif month_int == "04":
        month_str = "April"
    elif month_int == "05":
        month_str = "May"
    elif month_int == "06":
        month_str = "June"
    elif month_int == "07":
        month_str = "July"
    elif month_int == "08":
        month_str = "August"
    elif month_int == "09":
        month_str = "September"
    elif month_int == "10":
        month_str = "October"
    elif month_int == "11":
        month_str = "November"
    elif month_int == "12":
        month_str = "December"
    return month_str

def year_init():
    """ Initialises an object containing a list of months who have an int with 0 """
    blank_year = {
        "January": 0,
        "February" : 0,
        "March" : 0,
        "April" : 0,
        "May" : 0,
        "June" : 0,
        "July" : 0,
        "August" : 0,
        "September" : 0,
        "October" : 0,
        "November" : 0,
        "December" : 0,
    }
    return blank_year
    

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