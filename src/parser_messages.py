import utils
from os import getcwd, listdir, path

def parse_messages(user_data: dict) -> dict:
    """ Goes through messages and parses number of messages and number of photos """
    conversations_directory = getcwd() + "/temp/messages/inbox/"
    conversation_list = listdir(conversations_directory)
    message_total = 0
    photos_total = 0
    message_per_year = {}
    for year in user_data["year_list"]:
        message_per_year[year] = 0

    # this is to avoid problems when replacing strings during generation
    user_data["year_list"] = str(user_data["year_list"])

    for conversation_path in conversation_list:
        print("Parsing conversation: " + conversation_path + "...................", end='\r')
        message_list_path = conversations_directory + conversation_path + "/message_1.json"
        photos_path = conversations_directory + conversation_path + "/photos"
        if path.isdir(photos_path):
            photos_total += len(listdir(photos_path))
        message_list = utils.json_file_converter(message_list_path)
        message_total += len(message_list["messages"])
        for message in message_list["messages"]:
            message_timestamp = str(message["timestamp_ms"])[:-3]
            message_year = int(utils.epoch_to_year(message_timestamp))
            message_per_year[message_year] += 1

    # convert dictionary of message per years to a list of values corresponding to each year
    yearly_message_list = list(message_per_year.values())

    user_data["nbr_of_messages"] = utils.number_prettify(message_total)
    user_data["nbr_of_conversations"] = utils.number_prettify(len(conversation_list))
    user_data["nbr_of_message_photos"] = utils.number_prettify(photos_total)
    user_data["nbr_of_photos"] = photos_total # keep this as an int because it will be re-used later in photos
    user_data["yearly_messages"] = str(yearly_message_list)

    return user_data


