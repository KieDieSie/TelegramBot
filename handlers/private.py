from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f
from keyboards.for_navigate import keyboard

private_router = Router()


@private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.reply('Hello', reply_markup=keyboard)

@private_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('im dibidibidu')
    
@private_router.message(or_f(Command('options'), F.text.lower() == 'options'))
async def options(message: types.Message):
    await message.answer('My options are..')

@private_router.message(Command('links'))
async def links(message: types.Message):
    await message.answer('links')