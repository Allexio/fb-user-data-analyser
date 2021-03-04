from tkinter import ttk, Tk, Label
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo, showerror
from zipfile import ZipFile 
import os
import time
import shutil
from report_generator import generate_report
import webbrowser

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
    
    showinfo("Info", "Please select your Facebook zip file...")
    update_status("Selecting a Facebook data zip file", status, root)
    zip_path = file_picker()
    

    update_status("Unzipping Facebook data archive", status, root)
    zip_opener(zip_path)   
    update_progress(progress, 25, root)

    update_status("Validating Data", status, root)
    validate_uploaded_data()
    update_progress(progress, 5, root)
    
    # Parse data starting here
    user_data = {}

    update_status("Generating Report", status, root)
    generate_report(user_data)
    update_progress(progress, 5, root)

    update_status("Deleting Temporary Folder", status, root)
    delete_temp()
    update_progress(progress, 5, root)

    showinfo("Success", "The tool has finished generating your report, it will be automatically opened in your preferred web browser.")
    report_path = os.getcwd() + "/report_website_template/index.html"
    webbrowser.open(report_path)

def update_status(new_status: str, label: Label, gui_root: Tk):
    label["text"] = new_status
    gui_root.update()
    time.sleep(0.7) # wait half a sec so people can actually see the message
    

def update_progress(progress_bar: ttk.Progressbar, increment: int, gui_root: Tk):
    progress_bar.step(increment)
    gui_root.update()



main()
