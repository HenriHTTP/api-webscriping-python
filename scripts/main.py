###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

from utils.handle_data import list_data_generator
from utils.handle_csv import generate_csv
from utils.handle_json import json_data_generator
import sys


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)
    list_fields: list[str] = sys.argv[1].split(",")
    amount: int = int(sys.argv[2])
    file_name: str = str(sys.argv[3])
    format_file: str = str(sys.argv[4])
    data = list_data_generator(list_fields, amount)
    if format_file == "csv":
        generate_csv(data, file_name)
    if format_file == "json":
        json_data_generator(data, file_name)
