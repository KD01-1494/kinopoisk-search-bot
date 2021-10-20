from loader import bot, dp
from tools.search import ParseFilm

from aiogram import types
from aiogram.types.message import ParseMode
from setting import BotSetting


@dp.message_handler(commands=BotSetting.bot_commans['search'])
async def search(message: types.Message):
	film_query = ' '.join(message.text.split(' ')[1:])
	if not film_query:
		return await message.answer('Напишите фильм для поиска!')

	f = ParseFilm(film_query)
	template = await f.load()

	await bot.send_message(message.chat.id, template, parse_mode=ParseMode.HTML)