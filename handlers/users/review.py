from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from aiogram.dispatcher.filters import Command
from states.review import Review


@dp.message_handler(text="Send Review \u2B50", state=None)
async def enter_test(message: types.Message):
    await message.answer("Hey!\nPlease send the review of my work to help me.\n(it's not public)")
    await Review.Q1.set()


@dp.message_handler(state=Review.Q1)
async def get_review(message: types.Message, state: FSMContext):
    await message.answer("Thanks!\nReview has been saved.")
    await state.finish()
