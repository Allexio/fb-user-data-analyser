import utils
from os import getcwd

def parse_friends(user_data: dict) -> dict:
    """ Goes through posts and parses number of posts """
    friends_path = getcwd() + "/temp/friends/friends.json"
    removed_friends_path = getcwd() + "/temp/friends/removed_friends.json"

    friends_list = utils.json_file_converter(friends_path)

    friends_total = len(friends_list["friends"])


    user_data["nbr_of_friends"] = utils.number_prettify(friends_total)

    try:
        removed_friends_list = utils.json_file_converter(removed_friends_path)
    except:
        user_data["nbr_of_removed_friends"] = "0"
        return user_data

    removed_friends_total = len(removed_friends_list["deleted_friends"])
    user_data["nbr_of_removed_friends"] = utils.number_prettify(removed_friends_total)

    return user_data
