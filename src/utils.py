import datetime
import json
import os
from pathlib import Path
from pprint import pprint

import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv

from src.data_path import USER_JSON_PATH, OPERATIONS_PATH


def hello_date():
    """
    Функция выводит текст приветствия в зависимости от текущего времени
    """
    current_date_time = datetime.datetime.now()
    if 5 <= current_date_time.hour <= 11:
        return "Доброе утро"
    elif 12 <= current_date_time.hour <= 17:
        return "Добрый день"
    elif 18 <= current_date_time.hour <= 21:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def open_operations_xls(path_xls: str) -> object:
    """
    Считываем файл xls и возвращаем список словарей
    :param path_xls: Путь до файла xls.
    :return: Список словарей.
    """
    path_user = str(path_xls)
    try:
        reader = pd.read_excel(path_user)
    except AttributeError:
        return "Указан неверный путь файла"

    reader = pd.DataFrame(reader).replace({np.nan: None})
    return reader


def get_sum_expenses():
    """
    Функция группирует карты и выводит сумму платежей по каждой карте
    """
    df = open_operations_xls(OPERATIONS_PATH)
    card_grouped = df.groupby("Номер карты").sum()[["Сумма платежа"]]
    return card_grouped


def get_valute(currencies: list) -> list[dict]:
    """
    Функция выводит курс заданных валют
    :param currencies: Список названий валют
    :return: словарь с данными по заданной валюте
    """
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    response_json = response.json()
    payload = []
    for currency in currencies:
        user_dict = {
            "currency": currency,
            "rate": round(response_json["Valute"][currency]["Value"], 2),
        }
        payload.append(user_dict)
    return payload


def get_api_stock(stocks: list) -> list[dict]:
    """
    Функция выводит стоимость заданных акций
    :param stocks: Список акций
    :return: Список словарей со стоимостью акций
    """
    load_dotenv()
    api_key = os.getenv("API_KEYS_2")
    stocks_list = []
    if api_key is None:
        raise ValueError
    for stock in stocks:
        url = f"https://finnhub.io/api/v1/quote?symbol={stock}&token={api_key}"
        response = requests.get(url)
        response_json = response.json()
        stocks_dict = {"stock": stock, "price": response_json["c"]}
        stocks_list.append(stocks_dict)
    return stocks_list


def open_config_file(config_file: Path) -> list[dict]:
    """
    Открываем файл user_settings.json
    """
    with open(config_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    # path_file = USER_JSON_PATH
    # settings = open_config_file(path_file)
    # print(get_valute(settings["user_currencies"]))
    # pprint(get_api_stock(settings["user_stocks"]))
    print(get_sum_expenses())
