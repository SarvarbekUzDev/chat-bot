from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db
from functions import admins
from states.admin import AddAdminState, DeleteAdminState
from keyboards.inline import cancel


@dp.message_handler(Command("add_admin"), user_id=admins())
async def bot_addadmin(message: types.Message):
	msg = "Admin qo'shish uchun foydalanuvchi `chat_id` sini kriting: "
	await message.answer(msg, reply_markup=cancel.cancel_keyboard)

	await AddAdminState.chat_id.set()

@dp.message_handler(state=AddAdminState.chat_id)
async def bot_admincreate(message: types.Message, state: FSMContext):
	# async with state.proxy() as data:
	# 	data['chat_id'] = message.text
	instance = db.session.query(db.Users).filter_by(chat_id=message.text).first()
	if instance:
		instance.is_admin = True
		db.session.commit()
		await message.answer(f"Admin muvafaqiyatli qo'shildi, {message.text}")
		await state.finish()
	else:
		await message.answer("Bunday foydalanuvchi topilmadi\n\nQaytib kriting:")


# ---------------- ADMIN DELETE -----------------
@dp.message_handler(Command("del_admin"), user_id=admins())
async def bot_deletechannel(message: types.Message):
	admins =  db.session.query(db.Users).filter(db.Users.is_admin==True).all()
	msg = "Admin o'chirish uchun `chat_id`sini kiritng: \n\n"
	if admins:
		for admin in admins:
			msg += f"`{admin.chat_id}`\n"
		
		await message.answer(msg, reply_markup=cancel.cancel_keyboard)
		await DeleteAdminState.chat_id.set()
	else:
		await message.answer("2-darajali adminlar hali mavjud emas")


@dp.message_handler(state=DeleteAdminState.chat_id)
async def bot_channelchat_id(message: types.Message, state: FSMContext):
	instance = db.session.query(db.Users).filter_by(chat_id=message.text).first()
	if instance:
		instance.is_admin = False
		db.session.commit()
		await message.answer(f"Admin muvafaqiyatli o'chirildi, {message.text}")
		await state.finish()
	else:
		await message.answer("Bunday foydalanuvchi topilmadi\n\nQaytib kriting:")