import utils
from os import getcwd

def parse_comments(user_data: dict) -> dict:
    """ Goes through comments and parses number of comments """
    comments_path = getcwd() + "/temp/comments/comments.json"
    comment_list = utils.json_file_converter(comments_path)
    comment_total = len(comment_list["comments"])

    user_data["nbr_of_comments"] = utils.number_prettify(comment_total)

    return user_data


