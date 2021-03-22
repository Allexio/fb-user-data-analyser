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

    # instantiate a list of years [1996, 1997, 1998, ... , 2021]
    current_year = datetime.date.today().year
    year_list = list(range(int(join_year), current_year + 1))
    # instantiate a list of months [January 1996, February 1996, March 1996, ... , December 2021]
    month_list = utils.year_init()
    full_month_list = []
    for year in year_list:
        for month in month_list.keys():
            full_month_list.append(month + " " + str(year))

    # remove months in the future
    current_month = datetime.date.today().strftime('%m')
    current_month_name = utils.number_to_month_name(current_month)
    current_month_index = full_month_list.index(current_month_name + " " + str(current_year))
    full_month_list = full_month_list[:current_month_index]

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
    user_data["month_list"] = full_month_list
    user_data["relationship_status"] = relationship_status
    user_data["relationship_timestamp"] = relationship_timestamp
    user_data["ex#1"] = ex_1
    user_data["ex#2"] = ex_2
    user_data["ex#3"] = ex_3
    return user_data