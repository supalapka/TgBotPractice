from aiogram import types

from loader import dp

import requests

TICKER_API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


def get_crypto_price():
    response = requests.get(TICKER_API_URL)
    response_json = response.json()
    return response_json["bpi"]["USD"]["rate"]


@dp.message_handler(text="Show Bitcoin price \U0001f4b0")
async def bot_show_price(message: types.Message):
    await message.answer("1 Bitcoin = " + get_crypto_price()+"$")
