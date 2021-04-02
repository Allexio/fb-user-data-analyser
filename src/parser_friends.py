import utils
from os import getcwd

def parse_friends(user_data: dict) -> dict:
    """ Goes through posts and parses number of posts """
    friends_path = getcwd() + "/temp/friends/friends.json"
    removed_friends_path = getcwd() + "/temp/friends/removed_friends.json"
    rejected_friends_path = getcwd() + "/temp/friends/rejected_friend_requests.json"

    try:
        nbr_of_rejections = len(utils.json_file_converter(rejected_friends_path)["rejected_requests"])
    except FileNotFoundError:
        nbr_of_rejections = 0

    friends_per_month = {}
    for year in user_data["year_list"]:
        friends_per_month[year] = utils.year_init()

    friends_list = utils.json_file_converter(friends_path)

    friends_total = len(friends_list["friends"])
    for new_friend in friends_list["friends"]:
        month, year = utils.epoch_to_year_and_month(new_friend["timestamp"])
        friends_per_month[int(year)][month] += 1

    


    user_data["nbr_of_friends"] = utils.number_prettify(friends_total)

    try:
        removed_friends_list = utils.json_file_converter(removed_friends_path)
        for removed_friend in removed_friends_list["deleted_friends"]:
            month, year = utils.epoch_to_year_and_month(removed_friend["timestamp"])
            friends_per_month[int(year)][month] -= 1
        removed_friends_total = len(removed_friends_list["deleted_friends"])
    except FileNotFoundError:
        removed_friends_total = 0
        print("Could not parse removed friend data.")

    monthly_friend_list = []
    for year in friends_per_month:
        monthly_friend_list.extend(list(friends_per_month[year].values()))

    # add up the friend changes in every month to have one clean curve
    for i in range(len(monthly_friend_list)):
        if i > 0:
            monthly_friend_list[i] += monthly_friend_list[i-1]
    print(monthly_friend_list)
    
    #initialise dunbar list 
    dunbar_list = []
    for i in range(len(monthly_friend_list)):
        dunbar_list.append(150)

    
    user_data["nbr_of_removed_friends"] = utils.number_prettify(removed_friends_total)
    user_data["monthly_friends"] = monthly_friend_list
    user_data["dunbars_number"] = dunbar_list
    user_data["nbr_of_rejections"] = nbr_of_rejections
    return user_data
