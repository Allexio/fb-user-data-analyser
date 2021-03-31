import utils
from os import getcwd, listdir, path
from nudenet import NudeClassifier # nudity detection

def parse_messages(user_data: dict) -> dict:
    """ Goes through messages and parses number of messages and number of photos """
    conversations_directory = getcwd() + "/temp/messages/inbox/"
    conversation_list = listdir(conversations_directory)
    message_total = 0
    photos_total = 0

    message_per_year = {}
    for year in user_data["year_list"]:
        message_per_year[year] = 0

    message_per_month = {}
    for year in user_data["year_list"]:
        message_per_month[year] = utils.year_init()

    photos_per_month = {}
    for year in user_data["year_list"]:
        photos_per_month[year] = utils.year_init()

    message_photo_paths = []

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
            message_month, message_year = utils.epoch_to_year_and_month(message_timestamp)
            message_per_year[int(message_year)] += 1
            message_per_month[int(message_year)][message_month] += 1
            
            if "photos" in message:
                for photo in message["photos"]:
                    if "http" not in photo["uri"]: # make sure it's not an online picture
                        message_photo_paths.append(getcwd()+"/temp/"+photo["uri"])
                        
                    photo_month, photo_year = utils.epoch_to_year_and_month(photo["creation_timestamp"])
                    photos_per_month[int(photo_year)][photo_month] += 1

    # check for any nudity in sent/received pictures
    

    # convert dictionary of message per years to a list of values corresponding to each year
    yearly_message_list = list(message_per_year.values())
    monthly_message_list = []
    for year in message_per_month:
        monthly_message_list.extend(list(message_per_month[year].values()))

    monthly_photo_list = []
    for year in photos_per_month:
        monthly_photo_list.extend(list(photos_per_month[year].values()))


    user_data["nbr_of_messages"] = utils.number_prettify(message_total)
    user_data["nbr_of_conversations"] = utils.number_prettify(len(conversation_list))
    user_data["nbr_of_message_photos"] = utils.number_prettify(photos_total)
    user_data["nbr_of_photos"] = photos_total
    user_data["yearly_messages"] = yearly_message_list
    user_data["monthly_messages_raw"] = monthly_message_list
    user_data["monthly_messages"] = [x / 10 for x in monthly_message_list]
    user_data["monthly_photos"] = monthly_photo_list
    user_data["message_photo_paths"] = message_photo_paths
    return user_data
