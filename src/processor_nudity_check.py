import utils
from os import getcwd, listdir, path
from nudenet import NudeClassifier # nudity detection
from shutil import copyfile

def check_for_nudity(user_data: dict):
    photo_path_list = user_data["message_photo_paths"]
    print("\nChecking for nudity in message photos. This might take a while depending on the number of photos.")
    classifier = NudeClassifier()
    classification = classifier.classify(photo_path_list, 4)
    unsafe_photo_paths = []
    for photo_path in photo_path_list:
        try:
            if classification[photo_path]["unsafe"] > 0.95:
                print("OYASHII: ", photo_path)
                unsafe_photo_paths.append(photo_path)
        except KeyError:
            print("A photo is mysteriously missing.")

    nbr_of_unsafe_photos = len(unsafe_photo_paths)
    output_html = unsafe_photo_carousel_html_generator(unsafe_photo_paths)
    user_data["unsafe_html"] = output_html
    user_data["nbr_of_unsafe_photos"] = nbr_of_unsafe_photos
    user_data["unsafe_photo_paths"] = unsafe_photo_paths
    return user_data

def unsafe_photo_mover(user_data: dict):
    print("Moving unsafe files to generated directory...")
    iterator = 1
    unsafe_photo_paths = user_data["unsafe_photo_paths"]
    for path in unsafe_photo_paths:
        dest_unsafe_directory = getcwd() + "/report_generated/assets/images/unsafe_pictures/" + str(iterator) + ".jpg"
        copyfile(path, dest_unsafe_directory)
        iterator += 1

def unsafe_photo_carousel_html_generator(unsafe_photo_paths: list) -> str:
    html = """<div class="carousel-item active"><img class="carousel-center" src="assets/images/unsafe_pictures/0.jpg"><div class="carousel-caption d-none d-md-block"><p></p></div></div>"""
    html_item_start = """<div class="carousel-item"><img class="carousel-center" src="assets/images/unsafe_pictures/"""
    html_item_mid = """.jpg"><div class="carousel-caption d-none d-md-block"><p>"""
    html_item_end = """</p></div></div>"""
    iterator = 1
    for path in unsafe_photo_paths:
        photo_caption = "in conversation: " + path[path.find("inbox/")+6:path.find("_")].replace("and", " and ")
        html += html_item_start + str(iterator) + html_item_mid + photo_caption + html_item_end
        iterator += 1
    return html