from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Telefonlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Samsung'),
            KeyboardButton(text='Redmi')
        ],
        [
            KeyboardButton(text='Iphone'),
            KeyboardButton(text='Vivo')
        ],
        [
            KeyboardButton(text='Huwavei'),
            KeyboardButton(text='Ortga'),

        ]

    ],

     resize_keyboard=True



)