from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from states.holatlar import Murojaat
from loader import dp,bot
from keyboards.default.tasdiqlash import tasdiqlash_buttons
from keyboards.default.dokon import dokon_buttons


# Echo bot
@dp.message_handler(text='Adminga murojaat')
async def bot_echo(message: types.Message):
    await message.answer(text='Ismni kiriting',reply_markup=ReplyKeyboardRemove())
    await Murojaat.ism_qabul_qilish.set()

@dp.message_handler(state=Murojaat.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"ism":matn})
    await message.answer(text='Familiyani kiriting')
    await Murojaat.familiya_qabul_qilish.set()

@dp.message_handler(state=Murojaat.familiya_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"familiya":matn})
    await message.answer(text='Yoshingizni kiriting')
    await Murojaat.tel_qabul_qilish.set()

@dp.message_handler(state=Murojaat.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"yosh":matn})
    await message.answer(text='Telefon raqamni kiriting')
    await Murojaat.manzil_qabul_qilish.set()

@dp.message_handler(state=Murojaat.tel_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"raqam":matn})
    await message.answer(text='Yashash manzilingizni kiriting')
    await Murojaat.manzil_qabul_qilish.set()

@dp.message_handler(state=Murojaat.manzil_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"manzil":matn})
    malumot = await state.get_data()
    ismi = malumot.get("ism")
    familiya = malumot.get("familiya")
    yosh = malumot.get("yosh")
    tel = malumot.get("raqam")
    manzil = malumot.get("manzil")


    textcha= f"Ism :{ismi}\n" \
            f"Familiya :{familiya}\n" \
            f"Yosh :{yosh}\n" \
            f"Tel :{tel}\n" \
            f"Manzil :{manzil}\n"

    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text=textcha,reply_markup=tasdiqlash_buttons)
    await Murojaat.tasdiqlash_holati.set()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="Bekor qilish")
async def bot_echo(message: types.Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="Bekor qilindi",reply_markup=tasdiqlash_buttons)
    await  state.finish()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="Tasdiqlash")
async def bot_echo(message: types.Message,state:FSMContext):
    malumot = await state.get_data()
    ismi = malumot.get("ism")
    familiya = malumot.get("familiya")
    yosh = malumot.get("yosh")
    tel = malumot.get("raqam")
    manzil = malumot.get("manzil")

    textcha = f"Ism :{ismi}\n" \
              f"Familiya :{familiya}\n" \
              f"Yosh :{yosh}\n" \
              f"Tel :{tel}\n" \
              f"Manzil :{manzil}\n"

    await bot.send_message(chat_id='5888565967',text=textcha)
    await bot.send_message(chat_id=message.from_user.id,text="Adminga yuborildi")
    await state.finish()