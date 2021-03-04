import utils
from os import getcwd

def parse_user_info(user_data: dict) -> dict:
    json_path = getcwd() + "/temp/profile_information/profile_information.json"
    info = utils.json_file_converter(json_path)
    user_name = info["profile"]["name"]["full_name"]

    user_data["user_name"] = user_name
    return user_data