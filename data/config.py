import os
from dotenv import load_dotenv, find_dotenv, set_key, dotenv_values


dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

# Read .env
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS").split(",")
IP = os.getenv("ip")

CHANNELS = os.getenv("CHANNELS").split(",") 
CHANNELS = CHANNELS if "" not in CHANNELS  else []





def get_env():
	data = {
		"API_KEY":os.getenv("API_KEY")
	}
	return data


def edit_channels(chat_id: [int, str], action: str):
	if action.lower() == "add":
		CHANNELS.append(chat_id)
	elif action.lower() == "del":
		CHANNELS.remove(chat_id)
	else:
		raise TypeError("No such type exists, species: ['add', 'del']")

	os.environ['CHANNELS'] =  ','.join(map(str, CHANNELS))
	set_key(dotenv_file, "CHANNELS", os.environ["CHANNELS"])
	return True


def edit_apitoken(token):
	os.environ['API_KEY'] =  token
	set_key(dotenv_file, "API_KEY", os.environ["API_KEY"])
	return True