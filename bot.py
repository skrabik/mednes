"""
    Main bot interface
"""

import os
import json
from dotenv import load_dotenv
import requests

from message import *
from graphics import *

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

offset = StaticMethods.getStartOffset(URL)
request = requests.get(f'{URL}getUpdates')

while True:
    result = request.json()
    for i in result['result']:
        message = StaticMethods.parseMessage(i)

        """
        Тут функции обработки сообщений
        """
        command = message.text
        if command == '/getgraph':
            StaticMethods.sendPhoto(BOT_TOKEN, message.chat_id, photo_path='main.jpg')
        else:
            StaticMethods.sendText(BOT_TOKEN, chat_id=message.chat_id, text=f"{message.text}")
        """
        Конец обработки
        """

        offset += 1
    request = requests.get(f'{URL}getUpdates?offset={offset}')


