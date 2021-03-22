import utils
from os import getcwd

def parse_off_facebook_activities(user_data: dict) -> dict:
    """ Goes through off_facebook_activities and parses number of websites and applications that hand over your data to Facebook """
    off_facebook_activities_path = getcwd() + "/temp/ads_and_businesses/your_off-facebook_activity.json"
    off_facebook_activity_list = utils.json_file_converter(off_facebook_activities_path)["off_facebook_activity"]

    number_of_websites_tracking_the_user = 0
    number_of_applications_tracking_the_user = 0

    for tracking_entity in off_facebook_activity_list:
        if "." in tracking_entity["name"]: # if there's a full stop, assume it's a website and not an application
            number_of_websites_tracking_the_user += 1
        else:
            number_of_applications_tracking_the_user += 1

    user_data["nbr_of_websites_tracking"] = utils.number_prettify(number_of_websites_tracking_the_user)
    user_data["nbr_of_applications_tracking"] = utils.number_prettify(number_of_applications_tracking_the_user)

    return user_data
