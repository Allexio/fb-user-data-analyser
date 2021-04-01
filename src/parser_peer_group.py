import utils
from os import getcwd

def parse_peer_group(user_data: dict) -> dict:
    """ Goes through facial recognition information and parses number of photos used for peer_group """

    peer_group_path = getcwd() + "/temp/about_you/friend_peer_group.json"
    try:
        peer_group_info = utils.json_file_converter(peer_group_path)
    except FileNotFoundError:
        user_data["peer_group"] = "Unknown"
        return user_data
    peer_group = peer_group_info["friend_peer_group"]

    user_data["peer_group"] = peer_group

    return user_data
