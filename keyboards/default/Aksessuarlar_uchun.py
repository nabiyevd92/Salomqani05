from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Aksessuarlar_uchun_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Naushniklar'),
            KeyboardButton(text='Chehollar')
        ],
        [
            KeyboardButton(text='Kalonkalar'),
            KeyboardButton(text='Zaryatniklar')
        ],
        [
            KeyboardButton(text='Ortga')
        ]

    ],
    resize_keyboard=True
)