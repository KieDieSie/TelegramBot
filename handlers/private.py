from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, StateFilter
from keyboards.for_navigate import main_menu, deck_menu
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from states.states import DeckStates


private_router = Router()

user_data = {}

#START

@private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    user_data[message.from_user.id] = {'decks': {}, 'current_deck': None}
    await message.answer('Welcome! Choose your action:', reply_markup=main_menu)
 
#CREATING DECK 
    
@private_router.message(StateFilter(None), F.text('Create deck'))
async def create_deck(message: types.Message, state: FSMContext):
    await message.answer('Enter new deck`s name')
    await state.set_state(DeckStates.creating_deck)

@private_router.message(DeckStates.creating_deck, F.text)
async def save_deck_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    deck_name = message.text
    user_decks = user_data[user_id]['decks']

    if deck_name in user_decks:
        await message.answer(f"THe deck '{deck_name}' already exists. Try another one")
    else:
        user_decks[deck_name] = {}
        user_data[user_id]["current_deck"] = deck_name
        await message.answer(f"Deck '{deck_name}' created and selected.", reply_markup=deck_menu)
        
