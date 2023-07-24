from aiogram import types
from aiogram.dispatcher.filters import BoundFilter, Filter

from functions import is_chat_member
from loader import dp
from keyboards.inline.channels import channelsbtns


class IsMember(BoundFilter):
	key = 'is_member'

	def __init__(self, is_member):
		self.is_member = is_member

	async def check(self, message: types.Message):
		member = await is_chat_member(message.from_user.id)
		# print(member, f" IS CHAT MEMBER\n\n\n")
		return member

