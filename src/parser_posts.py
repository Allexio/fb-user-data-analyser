import utils
from os import getcwd

def parse_posts(user_data: dict) -> dict:
    """ Goes through posts and parses number of posts """
    posts_path = getcwd() + "/temp/posts/your_posts_1.json"
    post_list = utils.json_file_converter(posts_path)
    post_total = len(post_list)

    user_data["nbr_of_posts"] = utils.number_prettify(post_total)

    return user_data


