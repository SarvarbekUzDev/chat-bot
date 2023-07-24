from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


channel_add = KeyboardButton(text="/add_channel")
channel_del = KeyboardButton(text="/del_channel")
admin_add = KeyboardButton(text="/add_admin")
admin_del = KeyboardButton(text="/del_admin")
reklama = KeyboardButton(text="/reklama")
token_add = KeyboardButton(text="/add_token")

admin_markup = ReplyKeyboardMarkup(resize_keyboard=True)
admin_markup.add(channel_add, channel_del)
admin_markup.add(admin_add, admin_del)
admin_markup.add(reklama)
admin_markup.add(token_add)