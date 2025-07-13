import os
import asyncio
import logging
import polib
from aiogram import Bot

from loader import bot, dp, i18n

# Middlewares
from apps.middlewares.db_session import DbSessionMiddleware
from apps.middlewares.language import LanguageMiddleware
from aiogram import types, Router
from aiogram.filters import Command
from apps.keyboards.default.user import user_main_menu_keyboard

# Routers
from apps.routers import start, register, feedback, backs, user_menu
from apps.routers.admin import category, product

# Utils & config
from apps.utils.commands import set_my_commands
from core.config import DEVELOPER

# ────────────────────────
# .po → .mo kompilyatsiya
# ────────────────────────
def compile_translations():
    locales = ["en", "ru", "uz"]
    for loc in locales:
        po_path = f"locale/{loc}/LC_MESSAGES/lang.po"
        mo_path = f"locale/{loc}/LC_MESSAGES/lang.mo"
        if os.path.exists(po_path):
            polib.pofile(po_path).save_as_mofile(mo_path)
            print(f"✅ {loc} uchun .mo fayl yaratildi.")
        else:
            print(f"⚠️ {loc} uchun {po_path} topilmadi.")


compile_translations()

# ────────────────────────
# Web‑hook parametrlari (hozir ishlatilmayapti)
# ────────────────────────
WEB_SERVER_HOST = "127.0.0.1"
WEB_SERVER_PORT = 8080
WEBHOOK_PATH = "/webhook"
WEBHOOK_SECRET = "SECRET"


async def startup(bot: Bot):
    await set_my_commands(bot)
    await bot.send_message(chat_id=DEVELOPER, text="Bot start to work")


async def shutdown(bot: Bot):
    await bot.send_message(chat_id=DEVELOPER, text="Bot stopped")


async def main():
    # ── Admin routerlar
    dp.include_router(backs.router)
    dp.include_router(category.router)
    dp.include_router(product.router)

    # ── User routerlar
    dp.include_router(start.router)
    dp.include_router(register.router)
    dp.include_router(feedback.router)
    dp.include_router(user_menu.router)

    # ── Global middlewares
    dp.message.middleware.register(DbSessionMiddleware())
    dp.callback_query.middleware.register(DbSessionMiddleware())
    dp.message.middleware.register(LanguageMiddleware(i18n=i18n))

    # ── Lifecycle handlerlar
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    # ── Polling
    await dp.start_polling(bot, polling_timeout=0)


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.ERROR,
    )
    logging.getLogger("aiogram.event").setLevel(logging.ERROR)

    asyncio.run(main())
