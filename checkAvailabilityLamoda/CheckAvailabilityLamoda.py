import os
from dotenv import load_dotenv
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

def getEnv():
    try:
        load_dotenv()
        token = str(os.environ['TOKEN'])
        user = str(os.environ['TELEGRAM_USER'])
        return (token, user)
    except:
        print("Переменные окружения не установлены")
        exit()

def checkExistDataFile():
    try:
        file = open('data.txt')
    except IOError:
        file = open('data.txt', 'w+')
        file.write('0')
        file.close()

def readData():
    file = open('data.txt', 'r', encoding="utf-8")
    data = file.read()
    file.close()
    if data:
        return int(data)
    else:
        sendMesage('<b>[Lamoda]</b> В data файле нет данных. Записываю данные => 0')
        saveData(str(0))
        return 0

def saveData(data):
    file = open('data.txt', 'w', encoding="utf-8")
    file.write(data)
    file.close()


def sendMesage(text):
    token, user = getEnv()
    send_url = 'https://api.telegram.org/bot'+token+'/sendMessage'
    args = {'chat_id': user, 'parse_mode': 'HTML', 'text': text, 'disable_web_page_preview': 'true'}
    response = requests.get(send_url, params=args)


def checkGoods(url):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    result = soup.find(class_="d-catalog-header__product-counter")
    if result:
        string = result.contents[0]    # '1 товар', '10 товаров' и т.п.
        strings = string.split()       # ['1', 'товар']
        return int(strings[0])
    else:
        return int(0)


def main():

    checkExistDataFile()
    local_count = readData()
    url = 'https://www.lamoda.ru/b/23887/'
    web_count = checkGoods(url)

    if local_count == web_count:
        pass
    elif local_count > web_count:
        saveData(str(web_count))
        text = '<b>[Lamoda]</b> Количество товаров <a href="' + url + '">Celio</a> уменьшилось ↓: ' + str(local_count) + ' до ' + str(web_count)
        sendMesage(text)
    else:
        saveData(str(web_count))
        text = '<b>[Lamoda]</b> Количество товаров <a href="' + url + '">Celio</a> увеличилось ↑: ' + str(local_count) + ' до ' + str(web_count)
        sendMesage(text)


if __name__ == "__main__":
    main()
