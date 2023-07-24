import time
from typing import List
from aiogram_media_group import media_group_handler
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import MediaGroupFilter

from loader import dp, db, bot
from functions import admins
from states.admin import ReklamaState
from keyboards.inline import cancel, other # next qilish `keyboards.inline.cancel` faylida



@dp.message_handler(Command("reklama"), user_id=admins())
async def bot_reklama(message: types.Message, state: FSMContext):
	await message.answer("Reklama uchun matn jo'nating: ", reply_markup=cancel.next_keyboard)
	await ReklamaState.text.set()

	async with state.proxy() as data:
		data['text'] = ''
		data['reply_markup'] = ''


@dp.message_handler(state=ReklamaState.text)
async def bot_reklama_caption(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['text'] = message.text

	await message.answer("Media jo'nating: ", reply_markup=cancel.next_keyboard)
	await ReklamaState.media.set()


@dp.message_handler(MediaGroupFilter(is_media_group=True),
						content_types=['photo','video','audio','document'], state=ReklamaState.media)
@media_group_handler
async def album_handler(messages: List[types.Message], state: FSMContext):
	async with state.proxy() as data:
		media = types.MediaGroup()

		msg:Message = messages[0]
		caption = True
		for message in messages:
			if message.photo:
				media.attach_photo(
						photo=message.photo[-1].file_id,
						caption=data['text'] if caption else None,
					)
			elif message.video:
				media.attach_video(
					message.video.file_id, 
					caption=data['text'] if caption else None,)
			elif message.document:
				media.attach_document(
					message.document.file_id,
					caption=data['text'] if caption else None,)
			elif message.audio:
				media.attach_audio(
					message.audio.file_id,
					caption=data['text'] if caption else None,)

			caption = False
		data['media'] = media

	await message.answer("Reklama uchun tugma jo'nating: ", reply_markup=cancel.next_keyboard)
	await ReklamaState.finish.set()

@dp.message_handler(content_types=['photo','video','audio','document'], state=ReklamaState.media)
async def bot_reklama_singlefile(message: types.Message, state: FSMContext):
	file_id = ""
	type = None
	if message.photo:
		file_id = message.photo[-1].file_id
		type = "photo"
	elif message.video:
		file_id = message.video.file_id
		type = "video"
	elif message.audio:
		file_id = message.audio.file_id
		type = "audio"
	elif message.document:
		file_id = message.document.file_id
		type = "document"

	async with state.proxy() as data:
		data['media'] = file_id
		data['type'] = type

	await message.answer("Reklama uchun tugma jo'nating: \n\nlink, yozuv", reply_markup=cancel.next_keyboard)
	await ReklamaState.button.set()


@dp.message_handler(state=ReklamaState.button)
async def bot_reklama_singlefile(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		try:
			btns = other.create_button(message.text)
			data['reply_markup'] = btns
		except Exception as e:
			pass
		

	await message.answer("Reklama jo'natilishini tasdiqlang: \n\nIstalgan yozuv yozing", 
						reply_markup=cancel.cancel_keyboard)
	await ReklamaState.finish.set()

@dp.message_handler(state=ReklamaState.finish)
async def bot_reklama_finish(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		users = db.session.query(db.Users).all()
		inline_btn = data['reply_markup'] if data['reply_markup'] else None

		for user in users:
			try:
				if data.get('type'):
					if data['type'] == "photo":
						await bot.send_photo(chat_id=user.chat_id,
									photo=data['media'],
									caption=data['text'], reply_markup=inline_btn)
					if data['type'] == "video":
						await bot.send_video(chat_id=user.chat_id,
									video=data['media'],
									caption=data['text'], reply_markup=inline_btn)
					if data['type'] == "audio":
						await bot.send_audio(chat_id=user.chat_id,
									video=data['media'],
									caption=data['text'], reply_markup=inline_btn)
					if data['type'] == "document":
						await bot.send_document(chat_id=user.chat_id,
									document=data['media'],
									caption=data['text'], reply_markup=inline_btn)
				elif not data.get("media"):
					await bot.send_message(chat_id=user.chat_id, text=data['text'], reply_markup=inline_btn)
				else:
					await bot.send_media_group(
						chat_id=user.chat_id, 
						media=data['media'],
						reply_markup=inline_btn
					)
			except Exception as e: # Chat not found
				print(e, " ERROR")

			time.sleep(0.4)

	await message.answer(f"Reklama foydalanuvchilarga jo'natildi")
	await state.finish()


