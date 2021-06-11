from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp

from aiogram.dispatcher.filters import Command


@dp.message_handler(text="Order own bot \U0001F916")
async def enter_test(message: types.Message):
    url = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Order", url="https://www.fiverr.com/supalapka/create-telegram-bot-low-price")
            ]
        ]
    )
    await message.answer("My fiverr profile:\n"
                         "https://www.fiverr.com/supalapka\n\n"
                         "Order bot development:\n"
                         "https://www.fiverr.com/supalapka/create-telegram-bot-low-price", reply_markup=url)
