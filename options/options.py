from aiogram.types import BotCommand


private = [
    BotCommand(command='create_deck', description='Створити нову колоду карт'),
    BotCommand(command='choose_deck', description='Вибрати колоду карт'),
    BotCommand(command='delete_deck', description='Видалити колоду кард')
]