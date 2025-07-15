import os
import asyncio
import logging
import polib

# --------------------------------------
# 1) Compile .po ➜ .mo before anything
# --------------------------------------

def compile_translations() -> None:
    """Compile all .po files (en/ru/uz) into .mo so aiogram I18n can load them."""
    for loc in ("en", "ru", "uz"):
        po_path = os.path.join("locale", loc, "LC_MESSAGES", "lang.po")
        mo_path = os.path.join("locale", loc, "LC_MESSAGES", "lang.mo")
        if os.path.exists(po_path):
            polib.pofile(po_path).save_as_mofile(mo_path)
            print(f"✅ {loc} ➜ .mo created")
        else:
            print(f"⚠️  {loc} ➜ .po not found, skipping")

compile_translations()

# --------------------------------------
# 2) Now import loader (bot / dp / i18n)
# --------------------------------------
from loader import bot, dp, i18n

from aiogram import Bot
from apps.middlewares.db_session import DbSessionMiddleware
from apps.middlewares.language import LanguageMiddleware

# Routers
from apps.routers import backs, start, register, feedback, user_menu
from apps.routers.admin import category, product

from apps.utils.commands import set_my_commands
from core.config import DEVELOPER

# --------------------------------------
# 3) Lifecycle callbacks
# --------------------------------------
async def on_startup(bot: Bot):
    await set_my_commands(bot)
    await bot.send_message(chat_id=DEVELOPER, text="✅ Bot ishga tushdi")

async def on_shutdown(bot: Bot):
    await bot.send_message(chat_id=DEVELOPER, text="🛑 Bot to'xtadi")

# --------------------------------------
# 4) Main polling loop
# --------------------------------------
async def main() -> None:
    # Routers (admin ➜ user)
    dp.include_router(backs.router)
    dp.include_router(category.router)
    dp.include_router(product.router)

    dp.include_router(start.router)
    dp.include_router(register.router)
    dp.include_router(feedback.router)
    dp.include_router(user_menu.router)

    # Middlewares
    db_mw = DbSessionMiddleware()
    dp.message.middleware.register(db_mw)
    dp.callback_query.middleware.register(db_mw)
    dp.message.middleware.register(LanguageMiddleware(i18n=i18n))

    # Lifecycle hooks
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # Start polling
    await dp.start_polling(bot)

# --------------------------------------
# 5) Entrypoint
# --------------------------------------
if __name__ == "__main__":
    logging.basicConfig(
        format="[%(asctime)s] %(levelname)s | %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi")
