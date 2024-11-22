from aiogram import types



main_menu = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='Create deck'),
            types.KeyboardButton(text='Delete deck')
        ],
        [
            types.KeyboardButton(text='Select deck')
    ]
        
    ],
    resize_keyboard=True
)

deck_menu = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='Create card'), 
            types.KeyboardButton(text='Delete card')
        ],
        [
            types.KeyboardButton(text='Review cards')
        ],
        [
            types.KeyboardButton(text='Main menu')
        ]
    ]
)