import datetime
from os import getcwd
import utils

def parse_user_info(user_data: dict) -> dict:
    json_path = getcwd() + "/temp/profile_information/profile_information.json"
    info = utils.json_file_converter(json_path)
    profile_data = info["profile"]
    user_name = profile_data["name"]["full_name"]
    join_year = utils.epoch_to_year(profile_data["registration_timestamp"])
    relationship_status = profile_data["relationship"]["status"]
    if "partner" in profile_data["relationship"]:
        relationship_status += " with " + profile_data["relationship"]["partner"]
    relationship_timestamp = utils.epoch_to_year(profile_data["relationship"]["timestamp"])

    current_year = datetime.date.today().year
    year_list = list(range(int(join_year), current_year + 1))

    ex_1 = "None"
    ex_2 = "None"
    ex_3 = "None"
    
    if len(profile_data["previous_relationships"]) > 0:
        ex_1 = profile_data["previous_relationships"][0]["name"]
    if len(profile_data["previous_relationships"]) > 1:
        ex_2 = profile_data["previous_relationships"][1]["name"]
    if len(profile_data["previous_relationships"]) > 2:
        ex_3 = profile_data["previous_relationships"][2]["name"]
    

    # fill in the info
    user_data["user_name"] = user_name
    user_data["join_year"] = join_year
    user_data["year_list"] = year_list
    user_data["relationship_status"] = relationship_status
    user_data["relationship_timestamp"] = relationship_timestamp
    user_data["ex#1"] = ex_1
    user_data["ex#2"] = ex_2
    user_data["ex#3"] = ex_3
    return user_data