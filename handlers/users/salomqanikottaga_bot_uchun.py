from aiogram import types
from googletrans import Translator
from loader import dp

tarjimon = Translator()

# Echo bot
@dp.message_handler()
async def bot_echo(message: types.Message):

    til = tarjimon.detect(text=message.text).lang
    if til=='uz':
        eng = tarjimon.translate(text=message.text,dest='en',src='uz').text
        await message.answer(text=eng)
    elif til=='en':
        uzb = tarjimon.translate(text=message.text, dest='uz', src='en').text
        await message.answer(text=uzb)
    elif til=='uz':
        rus = tarjimon.translate(text=message.text, dest='ru', src='uz').text
        await message.answer(text=rus)
    elif til == 'ru':
        uzb = tarjimon.translate(text=message.text, dest='uz', src='ru').text
        await message.answer(text=uzb)


