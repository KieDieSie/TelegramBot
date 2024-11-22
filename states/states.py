from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class DeckStates(StatesGroup):
    creating_deck = State()
    deleting_deck = State()
    selecting_deck = State()
    creating_card_front = State()
    creating_card_back = State()
    deleting_card = State()
    reviewing_cards = State()