import utils
from os import getcwd

def parse_off_facebook_activities(user_data: dict) -> dict:
    """ Goes through off_facebook_activities and parses number of websites and applications that hand over your data to Facebook """
    off_facebook_activities_path = getcwd() + "/temp/ads_and_businesses/your_off-facebook_activity.json"
    off_facebook_activity_list = utils.json_file_converter(off_facebook_activities_path)["off_facebook_activity"]

    number_of_websites_tracking_the_user = 0
    number_of_applications_tracking_the_user = 0

    events_per_tracker = {}

    for tracking_entity in off_facebook_activity_list:
        if "." in tracking_entity["name"]: # if there's a full stop, assume it's a website and not an application
            number_of_websites_tracking_the_user += 1
        else:
            number_of_applications_tracking_the_user += 1
        events_per_tracker[tracking_entity["name"]] = len(tracking_entity["events"])

    # sort dict of events per tracker by descending value order
    events_per_tracker = {k: v for k, v in sorted(events_per_tracker.items(), reverse=True, key=lambda item: item[1])}
    events_per_tracker_str = html_tracker_list_builder(events_per_tracker)

    user_data["nbr_of_websites_tracking"] = utils.number_prettify(number_of_websites_tracking_the_user)
    user_data["nbr_of_applications_tracking"] = utils.number_prettify(number_of_applications_tracking_the_user)
    user_data["events_per_tracker"] = events_per_tracker_str

    return user_data


def html_tracker_list_builder(events_per_tracker: dict) -> str:
    """ Takes the dict of number of events per trackers, and produces a string in HTML format """
    start_html = """<li class="list-group-item"><div class="widget-content p-0"><div class="widget-content-wrapper"><div class="widget-content-left"><div class="widget-heading">"""
    mid_html = """</div><div class="widget-subheading">"""
    end_html = """</div></div></div></div></li>"""

    html_tracking_events = ""

    for entity in events_per_tracker:
        html_tracking_events += start_html + entity + mid_html + str(events_per_tracker[entity]) + end_html

    return html_tracking_events