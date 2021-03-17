from shutil import copytree, rmtree
from os import getcwd, listdir

def generate_report(user_data: dict):
    """ Takes a user data dictionary and generates HTML files with it """

    project_dir = getcwd()
    template_dir = project_dir + "/report_template"
    generated_dir = project_dir + "/report_generated"

    print("Deleting previously generated report.")
    # if a report already exists, delete it.
    try:
        rmtree(generated_dir)
    except FileNotFoundError:
        print("No generated report found, skipping deletion.")

    # copy template to generated dir
    copytree(template_dir, generated_dir)

    # for every html file in the generated directory
    for file_path in listdir(generated_dir):
        if ".html" in file_path:
            with open(template_dir+"/"+file_path, "r") as html_file:
                html_str = html_file.read()
            # replace keywords with actual values
            generated_html = keyword_replacer(user_data, html_str)
            with open(generated_dir+"/"+file_path, "w") as html_file:
                html_file.write(generated_html)

    # also replace keywords in the script file
    with open(template_dir + "/assets/scripts/main.js", "r", encoding="utf8") as script_file:
        script_str = script_file.read()
    generated_script = keyword_replacer(user_data, script_str)
    with open(generated_dir + "/assets/scripts/main.js", "w", encoding="utf8") as script_file:
        script_file.write(generated_script)


def keyword_replacer(user_data: dict, html: str) -> str:
    """ Takes the user data dict and an html file as string and replaces keywords with real values. """
    for keyword, value in user_data.items():
        print(keyword)
        print(value)
        print("replacing " + keyword + " with " + value)
        keyword = "{" + keyword + "}"
        html = html.replace(keyword, value)
    #html = html.replace("user_name", user_data["user_name"])
    return html