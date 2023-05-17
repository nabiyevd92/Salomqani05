from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Maishiy_texnikalar_uchun_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Muzlatgich'),
            KeyboardButton(text='Kir yuvish mashinasi')
        ],
        [
            KeyboardButton(text='Changyutgich'),
        ],
        [
            KeyboardButton(text='Gaz plita'),
            KeyboardButton(text='Ortga'),
        ]

    ],
    resize_keyboard=True
)