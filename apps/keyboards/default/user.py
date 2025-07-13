from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _

phone_number_share = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Share phone number ☎️", request_contact=True)
    ]], resize_keyboard=True, one_time_keyboard=True
)

location_share = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Share location 🌏", request_location=True)
    ]], resize_keyboard=True, one_time_keyboard=True
)


async def user_main_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Menu 🍴"))
            ],
            [
                KeyboardButton(text=_("Basket 🛒")),
                KeyboardButton(text=_("My orders 📝"))
            ],
            [
                KeyboardButton(text=_("Send feedback ✍️")),
                KeyboardButton(text=_("Settings ⚙️")),
            ]
        ], resize_keyboard=True
    )


async def back_user_main_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=_("Back ⬅️"))
        ]], resize_keyboard=True
    )




async def user_menu_keyboard():
    return ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Setlar(8)")],
        [KeyboardButton(text="Lavash(9)"), KeyboardButton(text="Shaurma")],
        [KeyboardButton(text="Burger(4)"), KeyboardButton(text="Hot-Dog(8)")],
        [KeyboardButton(text="Ichimliklar(11)")],
        [KeyboardButton(text="Shirinlik va disertlar(4)")],
        [KeyboardButton(text="Garnirlar(10)")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

async def user_menu_setlar_keyboard():
    return ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Combo Plus Isituvchan(Qora choy)"), KeyboardButton(text="FitCombo")],
        [KeyboardButton(text="Iftar kofte grill mol go'shtidan"), KeyboardButton(text="Donar boks mol go'shtidan")],
        [KeyboardButton(text="Donar boks tovuq go'shtidan"), KeyboardButton(text="COMBO+")],
        [KeyboardButton(text="Iftar strips tovuq go'shtidan"), KeyboardButton(text="Kids COMBO")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)
async def user_menu_lavash_keyboard():
    return ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Mol go'shtidan qalampir lavash"), KeyboardButton(text="Tovuq go'shtidan qalampir lavash")],
        [KeyboardButton(text="Mol go'shtidan pishloqli lavash"), KeyboardButton(text="Tovuq go'shtidan pishloqli lavash")],
        [KeyboardButton(text="FITTER"), KeyboardButton(text="Lavash tovuq go'sht")],
        [KeyboardButton(text="Lavash mol go'sht")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

async def user_menu_shaurma_keyboard():
    return ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Shaurma qalampir mol go'sht"), KeyboardButton(text="Shaurma tovuq go'sht")],
        [KeyboardButton(text="Shaurma qalampir tovuq go'sht"), KeyboardButton(text="Shaurma mol go'sht")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)
async def user_menu_burger_keyboard():
    return ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Gamburger"), KeyboardButton(text="Double burger")],
        [KeyboardButton(text="Cheese burger"), KeyboardButton(text="Double cheese")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

async def user_menu_hotdog_keyboard():
    return ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Hot-dog baguette"), KeyboardButton(text="Sub tovuq cheese")],
        [KeyboardButton(text="Sub tovuq"), KeyboardButton(text="Hot-dog baguette double")],
        [KeyboardButton(text="Hot-dog kids"), KeyboardButton(text="Sub go'sht cheese")],
        [KeyboardButton(text="Hot-dog classic"), KeyboardButton(text="Sub go'sht")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

async def user_menu_ichimliklar_keyboard():
    return ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sok dena 0,33l"), KeyboardButton(text="Suv 0,5")],
        [KeyboardButton(text="Pepsi 0,5l"), KeyboardButton(text="Pepsi 1,5")],
        [KeyboardButton(text="Quyib beriladigan pepsi"), KeyboardButton(text="Bliss sharbati")],
        [KeyboardButton(text="Americano"), KeyboardButton(text="Latte")],
        [KeyboardButton(text="Ko'k choy"), KeyboardButton(text="Qora choy")],
        [KeyboardButton(text="Limonli ko'k choy")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

async def user_menu_shirinlik_keyboard():
    return ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Medovik Asalim"), KeyboardButton(text="Chizkeyk")],
        [KeyboardButton(text="Donut karameli"), KeyboardButton(text="Donut mevali")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

async def user_menu_garnirlar_keyboard():
    return ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ketchup"), KeyboardButton(text="Guruch")],
        [KeyboardButton(text="Pro-devevenski"), KeyboardButton(text="Sarimchoqli qayla")],
        [KeyboardButton(text="Chili qaylasi"), KeyboardButton(text="Mayonez")],
        [KeyboardButton(text="Salat"), KeyboardButton(text="Sir qaylasi")],
        [KeyboardButton(text="Tovuq strips"), KeyboardButton(text="Fri")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

