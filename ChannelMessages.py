import configparser
import json
import asyncio
from datetime import date, datetime
import re
from telethon import TelegramClient, events, sync
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)
# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']

send_to_phone = config['Telegram']['send_to_phone']
username = config['Telegram']['username']
user_input_channel = config['Telegram']['channel_link']
client = TelegramClient('anon', api_id, api_hash)

# Listen to messages from target channel
@client.on(events.NewMessage(chats=user_input_channel))
async def newMessageListener(event):
    # Get message text
    newMessage = event.message.message


    # Apply 1st round of Regex for Subject for current messageContent — return list of keywords found (case—insensitive)
    subjectFiltered = re.findall(r"(?=.*delhi)(?=.*june)", newMessage, re.IGNORECASE)

    if len(subjectFiltered) != 0:
        print(newMessage)
        await client.forward_messages(entity=send_to_phone, messages=event.message)


with client:
    client.run_until_disconnected()
