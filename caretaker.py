from message import *
from dotenv import load_dotenv
import os
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

with open('allowed_chats.txt', 'r') as f:
    chats_id = f.read().split()

while True:
    with open('data.txt', 'r') as f:
        data = list(map(int, f.read().split()[-30:]))
        if abs(data[0] - data[-1]) > 1000:
            for chat in chats_id:
                StaticMethods.sendText(BOT_TOKEN=BOT_TOKEN, chat_id=chat,
                                       text='КАПЕЦ! ВЫЗЫВАЙ ПОЖАРНЫХ!!! \n У тебя что то горит!')
        elif abs(data[0] - data[-1]) > 70:
            for chat in chats_id:
                StaticMethods.sendText(BOT_TOKEN=BOT_TOKEN, chat_id=chat,
                                       text='Внимание! В вашем доме обнаружен посторонний!')


