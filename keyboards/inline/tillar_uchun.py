from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

tillar_butttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili",callback_data='til1'),
            InlineKeyboardButton(text="Rus tili",callback_data='til2'),
        ],
        [
            InlineKeyboardButton(text="Ingliz tili", callback_data='til3')
        ],
        [
            InlineKeyboardButton(text="Ulashish",switch_inline_query="Zo'r bot ekan"),
            InlineKeyboardButton(text="Hamkorlarimiz",url="https://t.me/Jx_uzb")
        ]
    ]
)