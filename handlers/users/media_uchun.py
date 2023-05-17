
from aiogram import types
from aiogram.types import ContentTypes, InputFile
from loader import dp,bot


# Echo bot
@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message):
    await  message.document.download()
    await message.answer("Dakument qabul qilindi")


@dp.message_handler(content_types=ContentTypes.VIDEO)
async def bot_echo(message: types.Message):
    await  message.video.download()
    await message.answer("Video qabul qilindi")


                                            # Telefonlar
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")


@dp.message_handler(text="Samsung")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_10.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- Samsung A31\n"
                                                                    "Xotira --- 3/32\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 1100.000"))



@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Redmi")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_11.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- Redmi 9T KA\n"
                                                                    "Xotira --- 3/32\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 1300.000"))

@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Iphone")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_12.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- Iphone 12 mini\n"
                                                                    "Xotira --- 6/128\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 340$"))

@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Vivo")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_13.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- Vivo Y31\n"
                                                                    "Xotira --- 4/64\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 1200.000"))

@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Huwavei")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_14.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- Huwavei Y5 2019\n"
                                                                    "Xotira --- 2/16\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 500.000"))


                                                    # Kompyuterlar
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")

@dp.message_handler(text="Asus")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_15.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- ASUS\n"
                                                                    "Xotira --- SSD:256GB\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 5000.000"))


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Acer")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_16.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- ACER\n"
                                                                    "Xotira --- HDD:1TB\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 130$"))


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Lenovo")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_17.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- LENOVO\n"
                                                                    "Xotira --- SSD:128,HDD:1TB\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 240$"))


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Hp")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_18.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- HP\n"
                                                                    "Xotira --- SSD:512\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 330$"))



                                            # Maishiy texnikalar
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")

@dp.message_handler(text="Muzlatgich")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_19.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- Artel\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 3000.000"))


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Kir yuvish mashinasi")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_20.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- LG\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 130$"))


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Changyutgich")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_21.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- Philips\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 700.000"))


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")

@dp.message_handler(text="Gaz plita")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_22.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption=("Nomi --- Elite\n"
                                                                        "Xolati --- Iddeal\n"
                                                                        "Narxi --- 2000.000"))





                                                # Aksessuarlar
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")

@dp.message_handler(text="Naushniklar")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_23.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- Airpods\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 300.000"))


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Chehollar")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_24.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- Matviy\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 20.000"))


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")



@dp.message_handler(text="Kalonkalar")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_25.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- Ailiang\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 1000.000"))


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")

@dp.message_handler(text="Zaryatniklar")
async def bot_echo(message: types.Message):
    rasm_manzili = InputFile(path_or_bytesio="photos/file_26.jpg")
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=("Nomi --- USB kabel\n"
                                                                    "Xolati --- Iddeal\n"
                                                                    "Narxi --- 10.000"))


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await  message.photo[-1].download()
    await message.answer("Rasm qabul qilindi")









