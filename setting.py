import os


class BotSetting:
	BOT_TOKEN = os.environ.get('TOKEN')
	bot_commans = {
		'search': ['s', 'search', 'search_film']
	}