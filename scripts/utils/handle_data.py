###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

from faker import Faker
from uuid import uuid4
import time


def list_data_generator(list_fields: list[str], amount: int) -> list[dict]:
    data_list: list[dict] = []
    start_time = time.time()
    for _ in range(amount):
        template_data: dict[str, any] = generate_single_data(list_fields)
        data_list.append(template_data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time:.2f}s")
    return data_list


def generate_single_data(list_fields: list[str]) -> dict[str, any]:
    template_data: Faker = Faker()
    template_data_dict: dict[str, any] = {
        "id": str(uuid4()),
        "name": template_data.name(),
        "addreass": template_data.address(),
        "email": template_data.email(),
        "phone_number": template_data.phone_number(),
        "birthdate": template_data.date_of_birth(),
        "company": template_data.company(),
        "city": template_data.city(),
        "country": template_data.country(),
    }
    return {
        field: template_data_dict[field]
        for field in list_fields
        if field in template_data_dict
    }


