"""
    Main bot interface
"""

import os
import json
from dotenv import load_dotenv
import requests
import matplotlib.pyplot as plt
import numpy as np

from message import *

load_dotenv()

print('Started')
BOT_TOKEN = os.getenv('BOT_TOKEN')
URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

offset = StaticMethods.getStartOffset(URL)
request = requests.get(f'{URL}getUpdates')


def help():
    StaticMethods.sendText(BOT_TOKEN, chat_id=message.chat_id, text='Доступные команды:\n/help\n/getgraph\n/start\n')

def start():
    text = 'Привет! Это бот, который поможет сохранить ваш дом в безопасности.\nЧтобы подключить проверку к телеграм аккаунту, добавьте ваш id в файл "allowed_id". '
    StaticMethods.sendText(BOT_TOKEN, chat_id=message.chat_id, text=text)
def getgraph():
    with open('data.txt', 'r') as f:
        data = f.read().split()[-60:]
        data = [int(i) for i in data]
        plt.figure()
        plt.plot(np.arange(0, 6, 0.1), data)
        plt.xlabel('последние измерения')
        plt.ylabel('Значения углекислого газа')
        plt.title('Данные')
        plt.savefig(f'info.jpg')
        StaticMethods.sendPhoto(BOT_TOKEN, message.chat_id, photo_path='info.jpg')

comands = {
    '/help': help,
    '/getgraph': getgraph,
    '/start': start,
}

while True:
    result = request.json()
    for i in result['result']:
        message = StaticMethods.parseMessage(i)

        command = message.text
        if command in comands:
            comands[command]()
            print(f'log: Выполнена команда: {command}')
        else:
            StaticMethods.sendText(BOT_TOKEN, chat_id=message.chat_id, text=f"Команда не расспознана\nСписок доступных комманд: /help")

        offset += 1
    request = requests.get(f'{URL}getUpdates?offset={offset}')


