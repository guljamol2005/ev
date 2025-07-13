import os
import polib


def compile_translations():
    """Compile .po files to .mo for all available locales."""
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

import asyncio
import logging
from aiogram import Bot

# Middlewares
from apps.middlewares.db_session import DbSessionMiddleware
from apps.middlewares.language import LanguageMiddleware

# Routers
from apps.routers import start, register, feedback, backs, user_menu
from apps.routers.admin import category, product

# Utils & config
from apps.utils.commands import set_my_commands
from core.config import DEVELOPER
from loader import bot, dp, i18n

# ────────────────────────────
# Web‑hook (disabled for now)
# ────────────────────────────
WEB_SERVER_HOST = "127.0.0.1"
WEB_SERVER_PORT = 8080
WEBHOOK_PATH = "/webhook"
WEBHOOK_SECRET = "SECRET"


async def startup(bot: Bot):
    """Actions to perform on bot startup."""
    await set_my_commands(bot)
    await bot.send_message(text="Bot start to work", chat_id=DEVELOPER)


async def shutdown(bot: Bot):
    """Actions to perform on bot shutdown."""
    await bot.send_message(text="Bot stopped", chat_id=DEVELOPER)


async def main():
    # ── Admin routers
    dp.include_router(backs.router)
    dp.include_router(category.router)
    dp.include_router(product.router)

    # ── User routers
    dp.include_router(start.router)
    dp.include_router(register.router)
    dp.include_router(feedback.router)
    dp.include_router(user_menu.router)

    # ── Global middlewares
    dp.message.middleware.register(DbSessionMiddleware())
    dp.callback_query.middleware.register(DbSessionMiddleware())
    dp.message.middleware.register(LanguageMiddleware(i18n=i18n))

    # ── Lifecycle handlers
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    # ── Start polling (web‑hook commented out)
    await dp.start_polling(bot, polling_timeout=0)


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.ERROR,
    )
    logging.getLogger("aiogram.event").setLevel(logging.ERROR)

    asyncio.run(main())
