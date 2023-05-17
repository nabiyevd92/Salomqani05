from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Kompyuterlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Asus'),
            KeyboardButton(text='Acer')
        ],
        [
            KeyboardButton(text='Hp'),
            KeyboardButton(text='Lenovo')
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)