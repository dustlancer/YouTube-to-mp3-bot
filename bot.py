from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from yt import get_audio
from aiogram.types import InputFile
import os

import time

token=os.getenv('TOKEN')




bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
  
    await bot.send_message(message.from_user.id, 'Отправь мне ссылку на YouTube видео и я отправлю тебе mp3')
    # await bot.send_message(message.from_user.id, 'ютубе')


@dp.message_handler()
async def saveau(message):
	try:
		f = get_audio(message.text)
		file = InputFile(f)
		await bot.send_audio(message.from_user.id, file)
		print(str(f) + " was sent to " + message.from_user.username) 

		os.remove(f)
	except:
		await bot.send_message(message.from_user.id, "Неправильный адрес")


executor.start_polling(dp, skip_updates=True)