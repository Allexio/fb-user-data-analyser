import utils
from os import getcwd, listdir, path

def parse_messages(user_data: dict) -> dict:
    """ Goes through messages and parses number of messages and number of photos """
    conversations_directory = getcwd() + "/temp/messages/inbox/"
    conversation_list = listdir(conversations_directory)
    message_total = 0
    photos_total = 0
    for conversation_path in conversation_list:
        message_list_path = conversations_directory + conversation_path + "/message_1.json"
        photos_path = conversations_directory + conversation_path + "/photos"
        if path.isdir(photos_path):
            photos_total += len(listdir(photos_path))
        message_list = utils.json_file_converter(message_list_path)
        message_total += len(message_list["messages"])

    user_data["nbr_of_messages"] = utils.number_prettify(message_total)
    user_data["nbr_of_conversations"] = utils.number_prettify(len(conversation_list))
    user_data["nbr_of_message_photos"] = utils.number_prettify(photos_total)

    return user_data


