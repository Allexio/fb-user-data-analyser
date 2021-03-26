from os import getcwd, listdir
from shutil import copyfile

def profile_picture_mover():
    """ Copies the most recent profile picture into the template folder """
    print("Finding profile picture")

    photos_path = getcwd() + "/temp/photos_and_videos/"
    profile_pictures_path = ""
    for path in listdir(photos_path):
        #print(path)
        if "profilepictures" in path.lower() or "photosdeprofil" in path.lower():
            profile_pictures_path = path
            break

    list_of_profile_pics = listdir(photos_path+"/"+profile_pictures_path)
    latest_profile_picture = list_of_profile_pics[len(list_of_profile_pics)-1]
    latest_profile_picture_path = photos_path+profile_pictures_path+"/"+latest_profile_picture
    generated_profile_picture_path = getcwd() + "/report_generated/assets/images/user.jpg"

    print("Found user profile picture in " + latest_profile_picture_path)
    print("Moving user profile picture to " + generated_profile_picture_path)

    copyfile(latest_profile_picture_path, generated_profile_picture_path)
