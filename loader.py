from aiogram import Bot, Dispatcher, executor
from setting import BotSetting

bot = Bot(BotSetting.BOT_TOKEN)
dp = Dispatcher(bot)

# Commands handling start
from commands import search