###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

import pandas as pd
import os


def generate_csv(data: list[dict], file_name: str) -> bool:
    csv_file_name: str = f"{file_name}.csv"
    if not data:
        print("The data list is empty. No CSV file will be generated.")
        return False
    try:
        data_frame = pd.DataFrame(data)
        data_frame.to_csv(csv_file_name, index=False)
        csv_file_exists: bool = os.path.isfile(csv_file_name)
        if csv_file_exists:
            print(f"the file '{csv_file_name}' was created successfully.")
        else:
            print(f"the file '{csv_file_name}.csv' was not found after creation.")
    except Exception as error:
        print(f"Ocorreu um erro: {error}")
        return False

    return True
