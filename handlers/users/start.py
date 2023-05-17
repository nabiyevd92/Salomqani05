from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.dokon import dokon_buttons
from keyboards.default.Telefonlar_uchun import Telefonlar_buttons
from keyboards.default.Kompyuterlar_uchun import Kompyuterlar_buttons
from keyboards.default.Maishiy_texnikalar_uchun import Maishiy_texnikalar_uchun_buttons
from keyboards.default.Aksessuarlar_uchun import Aksessuarlar_uchun_buttons
from loader import dp
from keyboards.inline.tillar_uchun import tillar_butttons
from filters import Shaxsiy


@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=dokon_buttons)


@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_butttons)

@dp.callback_query_handler(Shaxsiy(),text='til1')
async def bot_start(xabar:CallbackQuery):
    await xabar.message.answer(text=f"Salom mijoz, menyuni tanlang!",reply_markup=dokon_buttons)

@dp.callback_query_handler(Shaxsiy(),text='til2')
async def bot_start(xabar:CallbackQuery):
    await xabar.message.answer(text=f"Здравствуйте клиент, выберите меню!",reply_markup=dokon_buttons)

@dp.callback_query_handler(Shaxsiy(),text='til3')
async def bot_start(xabar:CallbackQuery):
    await xabar.message.answer(Shaxsiy(),text=f"Hello customer, select menu!",reply_markup=dokon_buttons)



@dp.message_handler(Shaxsiy(),text='Telefonlar')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=Telefonlar_buttons)

@dp.message_handler(text='Kompyuterlar')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=Kompyuterlar_buttons)

@dp.message_handler(Shaxsiy(),text='Maishiy texnikalar')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=Maishiy_texnikalar_uchun_buttons)


@dp.message_handler(Shaxsiy(),text='Aksessuarlar')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=Aksessuarlar_uchun_buttons)

@dp.message_handler(Shaxsiy(),commands="boshlash")
async def bot_start(message: types.Message):
    await message.answer("Salom, botga hush kelibsiz!")

