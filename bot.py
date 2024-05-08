"""
    Main bot interface
"""

import os
import json
from dotenv import load_dotenv
import requests
import matplotlib.pyplot as plt

from message import *

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

offset = StaticMethods.getStartOffset(URL)
request = requests.get(f'{URL}getUpdates')


def help():
    StaticMethods.sendText(BOT_TOKEN, chat_id=message.chat_id, text='Доступные команд: \n /getgraph \n')


def getgraph():
    with open('data.txt', 'r') as f:
        data = f.read().split()[-60:]
        plt.figure()
        plt.plot([i for i in range(len(data))], data)
        plt.xlabel('последние измерения')
        plt.ylabel('Значения углекислого газа')
        plt.title('Данные')
        plt.savefig(f'main.jpg')
        StaticMethods.sendPhoto(BOT_TOKEN, message.chat_id, photo_path='main.jpg')

comands = {
    '/help': help,
    '/getgraph': getgraph,
}

while True:
    result = request.json()
    for i in result['result']:
        message = StaticMethods.parseMessage(i)

        """
        Тут функции обработки сообщений
        """
        print(message.chat_id)
        command = message.text
        if command in comands:
            comands[command]()
        else:
            StaticMethods.sendText(BOT_TOKEN, chat_id=message.chat_id, text=f"Команда не расспознана\nСписок доступных комманд: /help")
        """
        Конец обработки
        """

        offset += 1
    request = requests.get(f'{URL}getUpdates?offset={offset}')


