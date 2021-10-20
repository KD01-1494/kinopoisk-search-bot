from aiohttp import ClientSession

import html5lib
from bs4 import BeautifulSoup

from requests.utils import quote
from parser_setting import ParserSetting


class ParseFilm:
	"""Класс для обработки и парсинга запросов на Кинопоиск"""
	def __init__(self, film_name):
		self.film_name = film_name
		self.film_query = f'https://www.kinopoisk.ru/index.php?kp_query={quote(film_name)}'
	

	async def load(self):
		html = await self.__film_request()

		try:
			film_url = await self.__parse_request_results(html)

			film_template = f'''
				<i>Скорее всего вы ищете -</i>
				{film_url}
			'''

		except Exception as e:
			film_template = f'''
				<i>Увы, результатов не найдено :(</i>
			'''

		return film_template


	async def __film_request(self):
		async with ClientSession() as session:
			resp = await session.get(self.film_query, headers=ParserSetting.search_film_headers)
			resp_text = await resp.text()
			await session.close()
		return resp_text


	async def __parse_request_results(self, html):
		soup = BeautifulSoup(html, 'html5lib')

		# Парсинг первого найденного фильма
		first_search_result = soup.find_all('div', class_='search_results')[0]
		film_block = first_search_result.find('div', class_='element most_wanted')
		film_block_info = film_block.find('div', class_='info')
		film_p_name = film_block_info.find('p', class_='name')

		film_p_name_children = film_p_name.findChildren()
		film_url = f'https://www.kinopoisk.ru' + film_p_name_children[0].get('href')

		return film_url