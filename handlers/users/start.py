import sqlalchemy
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart(), is_member=True)
async def bot_start(message: types.Message):
	msg = f"Assalomu alaykum {message.from_user.first_name}👋\n"
	msg += "\nBu Telegram-dagi chat bot. Savol berish uchun yozing."

	await message.answer(msg)

	# Create user
	try:
		db().insert(
			db.Users(chat_id=message.chat.id, fullname=message.chat.full_name)
		)
	except sqlalchemy.exc.PendingRollbackError as e:
		pass


