import random
import requests
from bs4 import BeautifulSoup
import re

recalls_normal = []


def random_recalls():
    try:
        url = 'http://www.banki.ru/'

        page_number = random.randint(1, 13)
        url_get_page = 'http://www.banki.ru/banks/?PAGEN_1=' + str(page_number)
        request_main_page = requests.get(url_get_page).text
        parsed = BeautifulSoup(request_main_page, "lxml")
        banks = parsed.find_all("a", class_="ui-image display-block float-left")

        bank_number = random.randint(1, len(banks))
        url_get_bank = url + banks[bank_number]['href']
        request_bank = requests.get(url_get_bank).text
        bank_url_name_mas = str(''.join(banks[bank_number]['href'])).split('/')
        bank_url_name = bank_url_name_mas[3]
        url_get_recalls = url + "services/responses/bank/" + bank_url_name
        request_recalls = BeautifulSoup(requests.get(url_get_recalls).text)
        recalls = str(request_recalls.find_all("div", {
            "class": "responses__item__message markup-inside-small markup-inside-small--bullet"}))
        recalls = re.sub(r'\<[^>]*\>', '', recalls)
        recalls = recalls.replace("\t", "").split("\n")
        recalls_return = []
        for i in range(1, len(recalls) - 1):
            recalls_return.append(recalls[i])
        return recalls_return, url_get_recalls
    except:
        random_recalls()
