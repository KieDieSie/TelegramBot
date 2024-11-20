from aiogram import types



keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='/create_deck'),
        ],
        [
            types.KeyboardButton(text='/delete_deck')
        ],
        [
            types.KeyboardButton(text='/select_deck')
        ]
        
    ],
    resize_keyboard=True,
    input_field_placeholder='All commands'
)