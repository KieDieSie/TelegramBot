from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, StateFilter
from keyboards.for_navigate import keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from states.states import AddDeck

private_router = Router()


decks = {}
isOnDeck = False
currentDeck = None

@private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.reply('Choose your option:', reply_markup=keyboard)
 
 
    
@private_router.message(StateFilter(None), Command('create_deck'))
async def new_deck(message: types.Message, state: FSMContext):
    await message.answer('Введіть назву колоди')
    await state.set_state(AddDeck.name)
    await state.update_data(name=message.text)
    name = state.get_data()
    await state.clear()
    await message.answer(f'Колода {str(name)} була успішно додана!')
    decks[name] = {}


@private_router.message(Command('delete_deck'))
async def links(message: types.Message):
    await message.answer('Enter deck name')
    



@private_router.message(Command('choose_deck'))
async def links(message: types.Message):
    await message.answer('Enter deck name')
    