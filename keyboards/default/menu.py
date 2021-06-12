from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Show Bitcoin price \U0001f4b0"),
        ],
        [
            KeyboardButton(text="Take a test \U0001f4dd"),
            KeyboardButton(text="Order own bot \U0001F916"),
        ],
        [
            KeyboardButton(text="Send Review \u2B50"),
        ],
    ], resize_keyboard=True)