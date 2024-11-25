from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, StateFilter
from keyboards.for_navigate import main_menu, deck_menu
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from states.states import DeckStates
from random import choice


private_router = Router()

user_data = {}

#START

@private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    user_data[message.from_user.id] = {'decks': {}, 'current_deck': None}
    await message.answer('Welcome! Choose your action:', reply_markup=main_menu)
 
#CREATING DECK 
    
@private_router.message((F.text == 'Create deck'), StateFilter(None))
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
    await state.clear()

#DELETING DECK

@private_router.message((F.text=='Delete deck'), StateFilter(None))
async def getting_name_to_delete_deck(message: types.Message, state: FSMContext):
    decks = user_data[message.from_user.id]['decks'].keys()
    await message.answer(str(decks))
    await message.answer('Enter name of the deck you want to delete(Including cases):')
    await state.set_state(DeckStates.deleting_deck)

@private_router.message(DeckStates.deleting_deck, F.text)
async def delete_deck(message: types.Message, state: FSMContext):          
    decks = user_data[message.from_user.id]['decks'].keys()
    deck_name = message.text
    
    if deck_name not in decks:
        await message.answer('There is no deck with this name')
    else:
        user_data[message.from_user.id]['decks'].pop(deck_name)
        await message.answer(f'Deck {deck_name} was deleted!')
    await state.clear()

#SELECTING DECK

@private_router.message((F.text=='Select deck'), StateFilter(None))
async def getting_name_to_select_deck(message: types.Message, state: FSMContext):
    decks = user_data[message.from_user.id]['decks'].keys()
    await message.answer(str(decks))
    await message.answer('Enter name of the deck you want select(Including cases):')
    await state.set_state(DeckStates.selecting_deck)

@private_router.message(DeckStates.deleting_deck, F.text)
async def select_deck(message: types.Message, state: FSMContext):          
    decks = user_data[message.from_user.id]['decks'].keys()
    deck_name = message.text
    
    if deck_name not in decks:
        await message.answer('There is no deck with this name')
    else:
        user_data[message.from_user.id]['current_deck'] = deck_name
        await message.answer(f'Deck {deck_name} was selected!')
    await state.clear()
        
# #CREATING CARDS

@private_router.message(F.text=='Create card')
async def create_card(message: types.Message, state: FSMContext):
    current_deck = user_data[message.from_user.id]["current_deck"]
    if not current_deck:
        await message.answer("No deck selected. Choose deck first.")
    else:
        await state.set_state(DeckStates.creating_card_front)
        await message.answer("Enter the front side of the card:")
        
@private_router.message(DeckStates.creating_card_front)
async def save_card_front(message: types.Message, state: FSMContext):
    current_deck = user_data[message.from_user.id]['current_deck']
    if message.text in user_data[message.from_user.id]['decks'][current_deck].keys():
        await message.answer('Card with such front side is already exists')
    else:
        await state.update_data(front=message.text)
        await state.set_state(DeckStates.creating_card_back)
        await message.answer("Enter the back side of the card:")
    
@private_router.message(DeckStates.creating_card_back)
async def save_card_back(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    current_deck = user_data[user_id]["current_deck"]
    back = message.text
    front = (await state.get_data())["front"]

    user_data[user_id]["decks"][current_deck][front] = [back]
    await state.clear()
    await message.answer(f"Card '{front}' added to the deck '{current_deck}'.", reply_markup=deck_menu)
    
# #DELETING CARDS

@private_router.message((F.text==("Delete card")))
async def getting_name_to_delete_card(message: types.Message, state: FSMContext):
    current_deck = user_data[message.from_user.id]['current_deck']
    if not current_deck:
        await message.answer('No deck selected. Select deck first')
    else:
        current_deck = user_data[message.from_user.id]['current_deck']
        cards = user_data[message.from_user.id]['decks'][current_deck]
        await message.answer(str(cards.keys()))
        await message.answer('Enter front value of card you want to delete')
        await state.set_state(DeckStates.deleting_card)
    
@private_router.message(DeckStates.deleting_card, F.text)
async def delete_card(message: types.Message, state: FSMContext):
    current_deck = user_data[message.from_user.id]['current_deck']
    cards = user_data[message.from_user.id]['decks'][current_deck].keys()
    card_to_del = message.text
    if card_to_del not in cards:
        await message.answer('There is no such card')
    else:
        user_data[message.from_user.id]['decks'][current_deck].pop(card_to_del)
        await message.answer(f'Card {card_to_del} was deleted!')
    await state.clear()
        
# #REVIEWING CARDS

@private_router.message((F.text=="Review cards"))
async def review_cards(message: types.Message, state: FSMContext):
    current_deck = user_data[message.from_user.id]["current_deck"]
    if not current_deck:
        await message.answer("No deck selected. Choose deck first.")
        return

    cards = user_data[message.from_user.id]['decks'][current_deck]
    if not cards:
        await message.answer("No cards in the selected deck.")
        return

    card = choice(list(cards))
    await state.set_state(DeckStates.reviewing_cards)
    await state.update_data(current_card=card)
    await message.answer(f"Front: {card}\nWhat is on the back?")

@private_router.message(DeckStates.reviewing_cards)
async def check_card_answer(message: types.Message, state: FSMContext):
    current_deck = user_data[message.from_user.id]["current_deck"]
    cards = user_data[message.from_user.id]['decks'][current_deck]
    card_back = cards[(await state.get_data())]
    if message.text == card_back:
        await state.clear()
        await message.answer("Correct!", reply_markup=deck_menu)
    else:
        await message.answer(f"Incorrect. The correct answer was: {card_back}.\nTry another card?")
        
        await state.set_state(DeckStates.reviewing_cards)
        
# #MEIN_MENU

@private_router.message((F.text=="Main menu"))
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await state.clear()
    user_data[message.from_user.id]["current_deck"] = None
    await message.answer("Returned to main menu.", reply_markup=main_menu)