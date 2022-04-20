from config import TG_TOKEN
from aiogram import Bot, types, Dispatcher, executor
from services import get_weather

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Hi! Write the city and I will send you the current weather.')


@dp.message_handler()
async def send_weather(message: types.Message):
    await message.answer(get_weather(message.text))

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
