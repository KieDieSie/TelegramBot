from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class DeckStates(StatesGroup):
    creating_deck = State()
    creating_card_front = State()
    creating_card_back = State()
    reviewing_cards = State()