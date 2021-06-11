from aiogram import types

from loader import dp

from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("about"), state=None)
async def enter_test(message: types.Message):
    await message.answer("This bot is an example of functionality that i can make. Besides those functions you can order custom bot logic.\n\n"
                         "My job is create the bot and then you decide where bot should be hosted, on your pc or on web.\n"
                         "If you want to host bot in web but don't know how to do that i can to it at extra charge.")


