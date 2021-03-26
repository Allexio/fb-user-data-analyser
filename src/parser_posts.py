import utils
from os import getcwd

def parse_posts(user_data: dict) -> dict:
    """ Goes through posts and parses number of posts """

    posts_per_month = {}
    for year in user_data["year_list"]:
        posts_per_month[year] = utils.year_init()

    posts_path = getcwd() + "/temp/posts/your_posts_1.json"
    post_list = utils.json_file_converter(posts_path)
    post_total = len(post_list)

    if not isinstance(post_list, list):
        user_data["nbr_of_posts"] = "1"
        user_data["monthly_posts"] = str(posts_per_month)
        return user_data

    for post in post_list:
        post_timestamp = post["timestamp"]
        post_month, post_year = utils.epoch_to_year_and_month(post_timestamp)
        posts_per_month[int(post_year)][post_month] += 1
    
    monthly_post_list = []
    for year in posts_per_month:
        monthly_post_list.extend(list(posts_per_month[year].values()))

    user_data["nbr_of_posts"] = utils.number_prettify(post_total)
    user_data["monthly_posts"] = str(monthly_post_list)

    return user_data
