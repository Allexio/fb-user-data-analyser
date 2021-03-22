import utils
from os import getcwd

def parse_interests(user_data: dict) -> dict:
    """ Goes through interests and parses number of interest per category """
    interests_path = getcwd() + "/temp/ads_and_businesses/ads_interests.json"
    interest_categories_path = getcwd() + "/src/interests.json"

    user_interests = utils.json_file_converter(interests_path)["topics"]
    interest_categories = utils.json_file_converter(interest_categories_path)

    interest_category_count = {}
    interest_category_total = {}

    category_list = list(interest_categories.keys())

    for category in category_list:
        interest_category_count[category] = 0
        interest_category_total[category] = 0
    
    for category in category_list:
        for interest in interest_categories[category]:
            interest_category_total[category] += 1
            if interest in user_interests:
                interest_category_count[category] += 1
    
    # standardise results by dividing by total number of interests per category
    for category in category_list:
        interest_category_count[category] = int((interest_category_count[category] / interest_category_total[category]) * 100)
        
    # transform to list
    interest_count_list = list(interest_category_count.values())

    print("interest_category_count: ", interest_category_count)

    # build a html interest string for the side list of interests
    html_interests = html_interest_list_builder(user_interests, interest_categories)

    user_data["interest_categories"] = category_list
    user_data["interest_count"] = interest_count_list
    user_data["html_interests"] = html_interests

    return user_data

def html_interest_list_builder(user_interests: list, interest_categories: dict) -> str:
    """ Takes a list of user interests and the interest categories dict, and produces a string in HTML format of user interests """
    start_html = """<li class="list-group-item"><div class="widget-content p-0"><div class="widget-content-wrapper"><div class="widget-content-left"><div class="widget-heading">"""
    mid_html = """</div><div class="widget-subheading">"""
    end_html = """</div></div></div></div></li>"""

    html_interests = ""

    for interest in user_interests:
        html_interests += start_html + interest + mid_html + "other" + end_html

    return html_interests