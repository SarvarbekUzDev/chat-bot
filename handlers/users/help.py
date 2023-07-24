from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, db
from keyboards.default.admin import admin_markup



@dp.message_handler(CommandHelp(), is_member=True)
async def bot_help(message: types.Message):
	msg = "Bu telegramdagi chatbot🤖\n"
	msg += "Ushbu bot google bard orqali ishlaydi✅\n"
	msg += "\nVa turli savollarga javob olishingiz mumkin✅\n"
	msg += "Savol berish uchun yozing💬"
	msg += "\n\n/start\n/help\n/users"
    
	# Is Admin
	is_admin = db.session.query(db.Users).filter_by(chat_id=message.chat.id, is_admin=True).first()
	if is_admin:
		if is_admin.chat_id == message.chat.id:
			await message.answer("Admin", reply_markup=admin_markup)

	await message.answer(msg)


