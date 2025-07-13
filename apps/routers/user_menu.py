from aiogram import Router, F, types
from aiogram.types import FSInputFile
from apps.keyboards.default.user import *

router = Router()


@router.message(F.text.in_(["Menu 🍴", "Menyu 🍴"]))
async def user_menu_handler(message: types.Message):
    text = "User menu is tapped"
    await message.answer(text=text)


@router.message(F.text == "/start")
async def start_handler(message: types.Message):
    text = (
        f"\n\nAssalomu alaykum, "
        f"{message.from_user.mention_html(f'{message.from_user.full_name}')}!"
    )
    await message.answer(text=text, reply_markup=user_main_menu_keyboard)


@router.message(F.text == "Setlar 🍱")
async def set_handler(message: types.Message):
    photo = FSInputFile("media/setlar.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_setlar_keyboard)


@router.message(F.text == "Lavash 🌯")
async def lavash_handler(message: types.Message):
    photo = FSInputFile("media/lavash.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_lavash_keyboard)


@router.message(F.text == "Shaurma 🥙")
async def shaurma_handler(message: types.Message):
    photo = FSInputFile("media/shaurma.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_shaurma_keyboard)


@router.message(F.text == "Burger 🍔")
async def burger_handler(message: types.Message):
    photo = FSInputFile("media/burger.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_burger_keyboard)


@router.message(F.text == "Hotdog 🌭")
async def hotdog_handler(message: types.Message):
    photo = FSInputFile("media/hotdog.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_hotdog_keyboard)


@router.message(F.text == "Ichimliklar 🧃")
async def ichimlik_handler(message: types.Message):
    photo = FSInputFile("media/ichimliklar.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_ichimliklar_keyboard)


@router.message(F.text == "Shirinliklar 🍰")
async def shirinlik_handler(message: types.Message):
    photo = FSInputFile("media/shirinlik.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_shirinlik_keyboard)


@router.message(F.text == "Garnirlar 🥗")
async def garnir_handler(message: types.Message):
    photo = FSInputFile("media/garnir.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_garnirlar_keyboard)
