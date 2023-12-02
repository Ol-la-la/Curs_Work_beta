import datetime
import json
from collections import deque
from pprint import pprint

import numpy as np
import pandas as pd
import requests

from src.data_path import USER_JSON_PATH, OPERATIONS_PATH


def open_operations_xls(path_xls: str) -> object:
    """
    Считываем файл xls и возвращаем список словарей
    :param path_csv_xls: путь до файла xls.
    :return: список словарей.
    """
    path_user = str(path_xls)
    try:
        reader = pd.read_excel(path_user, index_col='Номер карты')
    except Exception as e:
        return "Указан неверный путь файла"

    reader = pd.DataFrame(reader).replace({np.nan: None})
    return reader


def hello_date():
    current_date_time = datetime.datetime.now()
    if 5 <= current_date_time.hour <= 11:
        return "Доброе утро"
    elif 12 <= current_date_time.hour <= 17:
        return "Добрый день"
    elif 18 <= current_date_time.hour <= 21:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_sum_expenses(dict_expenses: dict) -> float:
    pass


def save_json_file(path_file: str, url_path: str, code: str):
    """
        Функция сравнивает значения валют двух файлов и возвращает совпадения
        :param path_file: Путь до файла user_settings.json
        :param url_path: url - путь до данных центробанка
        :param code: Название валюты
        :return: словарь с данными по заданной валюте
    """
    response = requests.get(url_path)
    response_json = response.json()
    payload = {}
    # response_file = json.load(path_file)
    with open(path_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open("response_txt.json", 'w', encoding='utf-8') as file:
        result = json.dump(response_json, file, ensure_ascii=False)
    return data


# def comparison_json_user(path_file: str, url_path: str, code: str):
#     # записываем результат в json-файл
#     payload = {}
#     response_file = save_json_file(url_path)
#     with open(path_file, 'r', encoding='utf-8') as file:
#         for i in file:
#             if i[code] == response_file[code]:
#                 payload.append(i)

# ^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$


if __name__ == '__main__':
    # headers = {"apikey": "nNfCnDaOSHjJJmbACPzCbkqDvkgrj8Zp"}
    # url = "https://www.cbr-xml-daily.ru/daily_json.js"
    # path_file = USER_JSON_PATH
    # print(save_json_file(path_file, url, "USD"))
    print(open_operations_xls(OPERATIONS_PATH))
