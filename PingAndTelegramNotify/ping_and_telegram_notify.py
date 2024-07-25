import os
from dotenv import load_dotenv
import time
import telebot
import socket

def getEnv():
    try:
        load_dotenv()
        token = str(os.environ['TOKEN'])
        channel = str(os.environ['TELEGRAM_USER'])
        ip = str(os.environ['IP_OR_DOMAIN'])
        return (token, channel, ip)
    except Exception as e:
        print(f"Dotenv error: {e}")
        exit()

token, channel, ip = getEnv()

bot = telebot.TeleBot(token)
status = False
pause = 60

"""Проверяет доступность IP и отправляет уведомление в Telegram.
Возвращает True при успешной проверке, False при ошибке.
При ошибках Telegram или хоста возращает True чтобы закончить цикл """
def check_ip():
    try:
        response = os.system('ping -c 1 ' + ip)
        if response == 0:
            print(ip + ' is up!')
            bot.send_message(channel, ip + ' is up')
            return True
        else:
            print(ip + ' is down!')
            time.sleep(pause)
            return False
    except socket.gaierror as e:
        print(f"Error resolving hostname: {e}")
        bot.send_message(channel, f"Error resolving hostname: {e}")
        return True
    except telebot.apihelper.ApiException as e:
        print(f"Telegram API error: {e}")
        return True

while True:
    try:
        new_status = check_ip()
        if new_status:    
            break
    except Exception as e:
        print(f"Unexpected error: {e}")