from aiogram.dispatcher.filters.state import State, StatesGroup



class AddAdminState(StatesGroup):
	""" Admin add state """
	chat_id = State()


class DeleteAdminState(StatesGroup):
	""" Admin delete state """
	chat_id = State()




class ReklamaState(StatesGroup):
	""" Bot users reklama """
	text = State()
	media = State()
	button = State()
	finish = State()




class AddChannelState(StatesGroup):
	""""""
	chat_id = State()

class DeleteChannelState(StatesGroup):
	""""""
	chat_id = State()




class AddToken(StatesGroup):
	"""  """
	token = State()