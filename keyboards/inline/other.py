from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def create_button(text_url: str):
	markup = InlineKeyboardMarkup()
	split_text = text_url.split(",")

	for i in range(0, len(split_text), 2):
		markup.add(
			InlineKeyboardButton(
				text=split_text[i+1],
				url=split_text[i].replace(" ","")
			)
		)
	return markup