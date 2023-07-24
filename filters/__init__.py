from aiogram import Dispatcher

from loader import dp
from .is_chat_member import IsMember


if __name__ == "filters":
    dp.filters_factory.bind(IsMember)
