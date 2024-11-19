from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f
from keyboards.for_navigate import keyboard

private_router = Router()


decks = {}
isOnDeck = False
currentDeck = None

@private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.reply('Hello', reply_markup=keyboard)

@private_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('im dibidibidu')
    
@private_router.message(or_f(Command('new_deck'), F.text.lower() == 'new_deck'))
async def new_deck(message: types.Message):
    await message.answer('Введіть назву колоди')

    async def get_deck_name(next_message: types.Message):  
            deck_name = next_message.text
            decks[deck_name] = {} 
            await next_message.answer(f"Колода '{deck_name}' успішно створена")

@private_router.message(Command('choose_deck'))
async def links(message: types.Message):
    await message.answer('Enter card`s front side')
    
    await message.answer('Enter card`s back side')