from aiogram import types

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='/new_deck'),
            types.KeyboardButton(text='/links'),
        ],
        [
            types.KeyboardButton(text='/about')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='All commands'
)