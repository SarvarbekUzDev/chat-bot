from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.admin import ReklamaState


cancel = InlineKeyboardButton(text="Cancel🛑", callback_data="cancel_state")
cancel_keyboard = InlineKeyboardMarkup().add(cancel)

next_btn = InlineKeyboardButton(text="Next", callback_data="next_state")
next_keyboard = InlineKeyboardMarkup().add(cancel).add(next_btn)



@dp.callback_query_handler(state='*', text=['cancel_state'])
async def cancel_state(call: types.Message, state: FSMContext):
	await call.message.answer("To'xtatildi🛑")
	await state.finish()



@dp.callback_query_handler(state=ReklamaState, text=["next_state"])
async def next_reklama_state(call: types.Message, state: FSMContext):
	get_state_ = await state.get_state()
	if get_state_ == "ReklamaState:text":
		await call.message.answer("Media jo'nating: ", reply_markup=next_keyboard)
	elif get_state_ == "ReklamaState:media":
		await call.message.answer("Reklama uchun tugma jo'nating: \n\nlink, yozuv", 
							reply_markup=next_keyboard)
	elif get_state_ == "ReklamaState:button":
		await call.message.answer("Reklama jo'natilishini tasdiqlang: \n\nIstalgan yozuv yozing")
	else:
		return

	await ReklamaState.next()