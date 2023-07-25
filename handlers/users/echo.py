from aiogram import types

from loader import dp, bot
from data.config  import get_env
from functions import ai_response


# Echo bot
@dp.message_handler(is_member=True)
async def bot_echo(message: types.Message):
	wait_message = await message.answer("⏳Iltimos biroz kuting...")
	try:
		response = ai_response(text=message.text)
	except Exception as e:
		response = "Qandaydir xatolik❌\n\nAdminlarga murojat qiling"
	# We delete the word wait
	await bot.delete_message(chat_id=message.chat.id, message_id=wait_message.message_id)
	await message.answer(response)




