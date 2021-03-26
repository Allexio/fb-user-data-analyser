import utils
from os import getcwd

def parse_location_history(user_data: dict) -> dict:
    """ Goes through locations and translates a list of locations into html string """
    locations_path = getcwd() + "/temp/location/location_history.json"
    try:
        location_list = utils.json_file_converter(locations_path)["location_history"]
    except FileNotFoundError:
        user_data["location_pings"] = "nodata"
        return user_data

    html_start = "L.marker(["
    html_mid = "]).addTo(mymap).bindPopup(\""
    html_end = "\");\n"

    location_pings = ""

    for ping in location_list:
        x = str(ping["coordinate"]["latitude"])
        y = str(ping["coordinate"]["longitude"])
        month, year = utils.epoch_to_year_and_month(ping["creation_timestamp"])
        location_pings += html_start + x + ", " + y + html_mid + month + " " + year + html_end


    user_data["location_pings"] = location_pings

    return user_data