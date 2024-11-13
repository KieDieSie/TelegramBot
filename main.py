import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from decouple import config

bot = Bot(token =config(TOKEN))

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.reply('Hello from my dev')

@dp.message()
async def echo(message: types.Message):
    msg = message.text
    if msg == 'abulday':
        await message.answer('dabulday')
    

async def main():
    await dp.start_polling(bot)
    

asyncio.run(main())