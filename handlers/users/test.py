from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from loader import dp

from aiogram.dispatcher.filters import Command

from states.test import Test


@dp.message_handler(text="Take a test \U0001f4dd", state=None)
async def bot_help(message: types.Message):
    await message.answer("What is your name?", reply_markup=ReplyKeyboardRemove())
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    await message.answer("What is your full phone number?")
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(phonenum=answer)
    markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Send your contact \U0001f4f1', request_contact=True))
    await message.answer("Can you approve this by sharing your contact?", reply_markup=markup_request)
    await Test.next()


@dp.message_handler(state=Test.Q3, content_types=types.ContentTypes.CONTACT)
async def answer_q1(contact: types.Message, state: FSMContext):
    data = await state.get_data()
    print(contact.contact.phone_number)
    if contact.contact.phone_number == data.get("phonenum"):
        await contact.answer("Nice! You didn't deceive me.")
    else:
        await contact.answer("Oh.. Phone numbers do not match.\n" + data.get("phonenum") + "  vs  " + contact.contact.phone_number + "\n\n/menu", reply_markup=ReplyKeyboardRemove())
    await state.finish()

