from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from functions import admins
from data.config import CHANNELS, edit_channels
from states.admin import AddChannelState, DeleteChannelState
from keyboards.inline import cancel


@dp.message_handler(Command("add_channel"), user_id=admins())
async def bot_addchannel(message: types.Message):
	msg = "Kanal yoki guruh qo'shish uchun  `chat_id` sini kriting: "
	await message.answer(msg, reply_markup=cancel.cancel_keyboard)

	await AddChannelState.chat_id.set()


@dp.message_handler(state=AddChannelState.chat_id)
async def bot_channelchat_id(message: types.Message, state: FSMContext):
	edit_channels(message.text, action="add")
	await message.answer("OK✅")

	await state.finish()


# -------------- DELETE Channel ---------------
@dp.message_handler(Command("del_channel"), user_id=admins())
async def bot_deletechannel(message: types.Message):
	msg = "Kanal yoki guruh o'chirish uchun  `chat_id` sini kriting: \n\n"
	if CHANNELS:
		for channel in CHANNELS:
			msg += f"`{channel}`\n"
		await message.answer(msg, reply_markup=cancel.cancel_keyboard)

		await DeleteChannelState.chat_id.set()
	else:
		await message.answer("Obuna bo'lish uchun kannalar mavjud emas")


@dp.message_handler(state=DeleteChannelState.chat_id)
async def bot_channelchat_id(message: types.Message, state: FSMContext):
	try:
		edit_channels(message.text, action="del")
		await message.answer("OK✅")

		await state.finish()
	except Exception as e:
		print(e)
		await message.answer("Bunday chat_id mavjud emas❌\n\nQaytib urinib ko'ring")