import utils
from os import getcwd, listdir
from os.path import isdir

def parse_photos(user_data: dict) -> dict:
    """ Goes through photos and parses number of them """
    photos_path = getcwd() + "/temp/photos_and_videos/"
    photos_total = user_data["nbr_of_photos"]
    videos_total = 0
    not_photo_dirs = ["stickers_used", "your_videos.json"]
    for album_path in listdir(photos_path):
        if album_path == "videos":
            videos_total += len(listdir(photos_path + album_path))
        elif album_path != not_photo_dirs and isdir(photos_path + album_path):
            photos_total += len(listdir(photos_path + album_path))

    user_data["nbr_of_photos"] = utils.number_prettify(photos_total)
    user_data["nbr_of_videos"] = utils.number_prettify(videos_total)

    return user_data
