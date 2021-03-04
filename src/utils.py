from ast import literal_eval

def json_file_converter(file_path: str) -> dict:
    with open(file_path, "r") as json_file:
        json_str = json_file.read()
    python_str = json_str.replace("true", "True").replace("false", "False").replace("null", "None")
    python_dict = literal_eval(python_str)
    return python_dict