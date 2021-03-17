import datetime
from os import getcwd
import utils

def parse_user_info(user_data: dict) -> dict:
    json_path = getcwd() + "/temp/profile_information/profile_information.json"
    info = utils.json_file_converter(json_path)
    profile_data = info["profile"]
    user_name = profile_data["name"]["full_name"]
    join_year = utils.epoch_to_year(profile_data["registration_timestamp"])


    current_year = datetime.date.today().year
    year_list = list(range(int(join_year), current_year + 1))
    user_data["user_name"] = user_name
    user_data["join_year"] = join_year
    user_data["year_list"] = year_list

    return user_data