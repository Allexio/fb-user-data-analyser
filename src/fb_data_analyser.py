from tkinter import Button, ttk, Tk, Label
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo, showerror
from zipfile import ZipFile
import os
import time
import shutil
import webbrowser
from parser_facebook_ads import parse_ad_interactions
from parser_facial_recognition import parse_facial_recognition
from parser_interests import parse_interests
from parser_location import parse_location_history
from parser_off_facebook_tracking import parse_off_facebook_activities
from parser_peer_group import parse_peer_group
from parser_profile_info import parse_user_info
from parser_friends import parse_friends
from parser_messages import parse_messages
from parser_posts import parse_posts
from parser_comments import parse_comments
from parser_profile_picture import profile_picture_mover
from parser_photos import parse_photos
from processor_nudity_check import check_for_nudity, unsafe_photo_mover
from report_generator import generate_report 

def file_picker() -> str:
    """ Spawns a file select GUI that lets user select a zip file, and returns its path. """
    file_path = askopenfilename(filetypes=[("Zip files", "*.zip")]) # select file GUI
    return file_path

def zip_opener(zip_path: str):
    """ Extracts contents of the facebook data zip folder into a temp folder """
    temp_path = os.getcwd() + "/temp"
    with ZipFile(zip_path, 'r') as zip:
        zip.extractall(path=temp_path)

def validate_uploaded_data():
    """ Checks that the selected directory conforms to what is expected from a facebook data folder. """
    data_valid = True
    # TODO: actually implement data validator.
    if not data_valid:
        delete_temp()
        showerror("Error", "Data uploaded is not valid Facebook data.")
        exit(1)

def delete_temp():
    """ Deletes the temp folder if it exists. """
    temp_path = os.getcwd() + "/temp"
    if os.path.isdir(temp_path):
        shutil.rmtree(temp_path)

def main():
    """ Main thread of the program, handles the GUI and calls to separate modules """

    root = Tk()
    root.title("Facebook Data Analyser")

    welcome_message = """Thanks for choosing to use the FB Data Analyser! \n
    This tool requires you to first download your Facebook data from the Facebook website.\n
    If you have not already done this, you can very easily do it by: 
    1) going on the Facebook website
    2) clicking on the drop down arrow top right
    3) clicking on "settings and privacy"
    4) clicking on "privacy shortcuts"
    5) scrolling down to the "your facebook data" section
    6) clicking on "access my facebook data"
    7) clicking on the "download my data" link
    8) select "all data", "JSON file" (photo quality is irrelevant) and click create file.
    
    Facebook will then send you an e-mail when your data is ready to download, simply follow the instructions provided in the e-mail.
    You do not need to unzip this data, the tool will do this for you."""

    info_text = Label(root, text="Please select your facebook data file.")
    info_text.pack()


    progress = ttk.Progressbar(root, orient='horizontal', length=700)
    progress.config(mode="determinate", maximum=100)
    progress.pack()

    status = Label(root, text="")
    status.pack()
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2 - 300)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    showinfo("Facebook Data Analyser Startup", welcome_message)
    showinfo("Info", "Please select your Facebook zip file...")
    update_status("Selecting a Facebook data zip file", status, root)
    zip_path = file_picker()

    info_text["text"] = "The tool is now running, this can take up to a few minutes, depending on the amount of data and speed of your computer."

    update_status("Unzipping Facebook data archive", status, root)
    zip_opener(zip_path)
    update_progress(progress, 25, root)

    update_status("Validating Data", status, root)
    validate_uploaded_data()
    update_progress(progress, 5, root)

    # Parse data starting here
    user_data = {}

    update_status("Parsing User Information", status, root)
    user_data = parse_user_info(user_data)
    update_progress(progress, 3, root)

    update_status("Parsing Location History", status, root)
    user_data = parse_location_history(user_data)
    update_progress(progress, 5, root)

    update_status("Parsing Facial Recognition Data", status, root)
    user_data = parse_facial_recognition(user_data)
    update_progress(progress, 2, root)

    update_status("Parsing Off-Facebook activities", status, root)
    user_data = parse_off_facebook_activities(user_data)
    update_progress(progress, 5, root)

    update_status("Parsing advertisement interactions", status, root)
    user_data = parse_ad_interactions(user_data)
    update_progress(progress, 1, root)

    update_status("Parsing Interests", status, root)
    user_data = parse_interests(user_data)
    update_progress(progress, 4, root)

    update_status("Parsing Messages", status, root)
    user_data = parse_messages(user_data)
    update_progress(progress, 8, root)

    update_status("Parsing Posts", status, root)
    user_data = parse_posts(user_data)
    update_progress(progress, 3, root)

    update_status("Parsing comments", status, root)
    user_data = parse_comments(user_data)
    update_progress(progress, 1, root)

    update_status("Parsing friends", status, root)
    user_data = parse_friends(user_data)
    update_progress(progress, 3, root)

    update_status("Parsing photos", status, root)
    user_data = parse_photos(user_data)
    update_progress(progress, 3, root)

    update_status("Parsing peer group", status, root)
    user_data = parse_peer_group(user_data)
    update_progress(progress, 1, root)

    update_status("Scanning photos for unsafe content", status, root)
    user_data = check_for_nudity(user_data)
    update_progress(progress, 10, root)

    update_status("Generating Report", status, root)
    generate_report(user_data)
    update_progress(progress, 5, root)

    update_status("Moving Profile Picture", status, root)
    profile_picture_mover()
    update_progress(progress, 3, root)

    update_status("Moving Unsafe Pictures", status, root)
    unsafe_photo_mover(user_data)
    update_progress(progress, 3, root)

    update_status("Deleting Temporary Folder", status, root)
    delete_temp()
    update_progress(progress, 5, root)

    showinfo("Success", "The tool has finished generating your report, it will be automatically opened in your preferred web browser.")
    report_path = os.getcwd() + "/report_generated/index.html"
    webbrowser.open(report_path)

def update_status(new_status: str, label: Label, gui_root: Tk):
    label["text"] = new_status
    gui_root.update()
    time.sleep(0.5) # wait half a sec so people can actually see the message
    

def update_progress(progress_bar: ttk.Progressbar, increment: int, gui_root: Tk):
    progress_bar.step(increment)
    gui_root.update()

main()
