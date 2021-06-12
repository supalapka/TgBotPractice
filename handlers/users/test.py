from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from loader import dp

from keyboards.default import menu

from states.test import Test

exit_from_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cancel test"),
        ],
    ], resize_keyboard=True)


@dp.message_handler(text="Take a test \U0001f4dd", state=None)
async def bot_help(message: types.Message):
    if message.text != "Cancel test":
        await message.answer("What is your name?", reply_markup=exit_from_test)
        await Test.Q1.set()
    else:
        await message.answer("menu", reply_markup=menu)


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    if message.text != "Cancel test":
        answer = message.text
        await state.update_data(name=answer)
        await message.answer("What is your full phone number?", reply_markup=exit_from_test)
        await Test.next()
    else:
        await message.answer("menu", reply_markup=menu)
        await state.finish()


@dp.message_handler(state=Test.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    if message.text != "Cancel test":
        answer = message.text
        await state.update_data(phonenum=answer)
        markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton('Send your contact \U0001f4f1', request_contact=True), (KeyboardButton('Cancel test')))
        await message.answer("Can you approve this by sharing your contact?", reply_markup=markup_request)
        await Test.next()
    else:
        await message.answer("menu", reply_markup=menu)
        await state.finish()


@dp.message_handler(state=Test.Q3, content_types=types.ContentTypes.CONTACT)
async def answer_q1(contact: types.Message, state: FSMContext):
    if contact.text != "Cancel test":
        data = await state.get_data()
        print(contact.contact.phone_number)
        if contact.contact.phone_number == data.get("phonenum"):
            await contact.answer("Nice! You didn't deceive me.")
        else:
            await contact.answer("Oh.. Phone numbers do not match.\n" + data.get("phonenum") + "  vs  " + contact.contact.phone_number + "\n\n/menu", reply_markup=ReplyKeyboardRemove())
        await state.finish()
    else:
        await contact.answer("menu", reply_markup=menu)
        await state.finish()


@dp.message_handler(state=Test.Q3)
async def answer_q1(contact: types.Message, state: FSMContext):
    if contact.text == "Cancel test":
        await contact.answer("menu", reply_markup=menu)
        await state.finish()
