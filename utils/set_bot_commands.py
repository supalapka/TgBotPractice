from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start bot"),
            types.BotCommand("help", "Show all commands"),
            types.BotCommand("about", "About bot"),
        ]
    )
