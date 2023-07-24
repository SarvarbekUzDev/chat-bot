from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import bot
from data.config import CHANNELS


async def channelsbtns():
	markup = InlineKeyboardMarkup()
	for channel_id in CHANNELS:
		try:
			get_chat_data = await bot.get_chat(chat_id=channel_id)
			markup.add(
				InlineKeyboardButton(text=get_chat_data['username'], url=f"t.me/{get_chat_data['username']}")
			)
		except Exception as e: # Chat not found
			print(e)

	return markup