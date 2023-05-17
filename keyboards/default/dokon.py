
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

dokon_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefonlar"),
            KeyboardButton(text="Kompyuterlar")
        ],
        [
            KeyboardButton(text="Maishiy texnikalar"),
            KeyboardButton(text="Aksessuarlar")
        ],
        [
            KeyboardButton(text='Adminga murojaat'),
        ]
    ],
    resize_keyboard=True
)