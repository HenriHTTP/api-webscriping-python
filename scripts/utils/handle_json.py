###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

import json
import os
from posix import strerror
from datetime import date, datetime

def serialize_data(data_list: list[dict]) -> list[dict]:
    for item in data_list:
        birthdate_date_exists: bool = (
            'birthdate' in item and isinstance(item['birthdate'], (date, datetime))
        )
        if birthdate_date_exists:
            item['birthdate'] = item['birthdate'].isoformat()
    return data_list

def json_data_generator(data_list: list[dict], file_name: str) -> bool:
    dir_path = (
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
    )
    json_file_name: str = f"{file_name}.json"
    archive_writed = os.path.join(dir_path, json_file_name)
    try:
        data_list = serialize_data(data_list)
        with open(archive_writed, "w") as json_file:
            json.dump(data_list, json_file, indent=1)
        json_archive_exists: bool = (
            os.path.exists(archive_writed) and os.path.getsize(archive_writed) > 0
        )
        if json_archive_exists:
            print("JSON file as created successfully!")
            return True
        return False
    except OSError as error:
        print(f"error {error}")
        return False
