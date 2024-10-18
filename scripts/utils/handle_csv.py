###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

import pandas as pd
import os


def generate_csv(data: list[dict], file_name: str) -> bool:
    if not data:
        print("The data list is empty. No CSV file will be generated.")
        return False
    try:
        data_frame = pd.DataFrame(data)
        data_frame.to_csv(file_name, index=False)
        if os.path.isfile(file_name):
            print(f"the file '{file_name}' was created successfully.")
        else:
            print(f"the file '{file_name}' was not found after creation.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False

    return True
