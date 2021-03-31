import utils
from os import getcwd

def parse_facial_recognition(user_data: dict) -> dict:
    """ Goes through facial recognition information and parses number of photos used for facial_recognition """

    facial_recognition_path = getcwd() + "/temp/about_you/face_recognition.json"
    try:
        facial_recognition_info = utils.json_file_converter(facial_recognition_path)
    except:
        user_data["nbr_of_fr_photos"] = 0
        return user_data
    nbr_of_fr_photos = facial_recognition_info["facial_data"]["example_count"]

    user_data["nbr_of_fr_photos"] = utils.number_prettify(nbr_of_fr_photos)

    return user_data
