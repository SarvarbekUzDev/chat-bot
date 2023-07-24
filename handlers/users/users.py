from sqlalchemy import func
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command("users"), is_member=True)
async def bot_users(message: types.Message):
	rows = db.session.query(func.count(db.Users.id)).scalar()
	# rows = db.session.query(db.Users).count()
	await message.answer(f"Bot foydalanuvchilar soni:  {rows}")