from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from functions import admins
from data.config import edit_apitoken, get_env
from states.admin import AddToken
from keyboards.inline import cancel


@dp.message_handler(Command("add_token"), user_id=admins())
async def bot_addtoken(message: types.Message):
	msg = f"Google bard ai ning tokenini kiritng: \n\nJoriy API KEY: `{get_env()['API_KEY']}`"
	await message.answer(msg, reply_markup=cancel.cancel_keyboard)

	await AddToken.token.set()


@dp.message_handler(state=AddToken.token)
async def bot_gettoken(message: types.Message, state: FSMContext):
	edit_apitoken(message.text)

	await message.answer("OK✅")
	await state.finish()