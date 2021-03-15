import utils
from os import getcwd

def parse_user_info(user_data: dict) -> dict:
    json_path = getcwd() + "/temp/profile_information/profile_information.json"
    info = utils.json_file_converter(json_path)
    profile_data = info["profile"]
    user_name = profile_data["name"]["full_name"]
    join_year = utils.epoch_to_year(profile_data["registration_timestamp"])

    user_data["user_name"] = user_name
    user_data["join_year"] = join_year

    return user_data