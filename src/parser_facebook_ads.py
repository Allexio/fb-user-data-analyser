import utils
from os import getcwd

def parse_ad_interactions(user_data: dict) -> dict:
    """ Goes through your ad interaction data and parses the number of ad clicks """
    ad_interactions_path = getcwd() + "/temp/ads_and_businesses/advertisers_you've_interacted_with.json"
    ad_interactions_list = utils.json_file_converter(ad_interactions_path)["history"]

    number_of_ads_clicked = len(ad_interactions_list)

    user_data["nbr_of_ads_clicked"] = utils.number_prettify(number_of_ads_clicked)

    return user_data


