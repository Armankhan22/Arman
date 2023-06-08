from telethon import TelegramClient 
import logging
import time 

openai_key = "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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6174263163:AAEwpRbm4t2ZSK-N5PqCfZaD81MHf-QAnd0"

bot = TelegramClient("Dalal02_bot", api_id, api_hash).start(bot_token = bot_token)