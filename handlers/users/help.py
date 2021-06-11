from aiogram import types

from loader import dp

from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("help"))
async def bot_help(message: types.Message):
    text = ("Commands list: ",
            "/start - Start/Restart",
            "/about - About this bot",
            "/menu - show main menu",
            "/review - Send review (not public anywhere")
    
    await message.answer("\n".join(text))
