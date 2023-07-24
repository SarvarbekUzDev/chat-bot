from bardapi import Bard
from typing import Union
import os

from loader import bot, db
from data.config import get_env, CHANNELS, ADMINS


def ai_response(text):
	os.environ['_BARD_API_KEY'] = get_env()['API_KEY']
	response = Bard().get_answer(text)['content']
	return response


def admins():
	admins_list = ADMINS.copy()
	is_admin_users = db.session.query(db.Users).filter(db.Users.is_admin==True).all()
	for admin in is_admin_users:
		admins_list.append(admin.chat_id)

	return admins_list


async def is_chat_member(user_id: [int, str]):
	# bot_  = bot.get_current()
	try:
		for channel in CHANNELS:
			member = await bot.get_chat_member(
				user_id=user_id, 
				chat_id=channel
			)
			if not member.is_chat_member():
				return None

		return True
	except Exception as e:
		print(e)
		return None

