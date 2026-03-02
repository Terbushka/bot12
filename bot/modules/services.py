from time import time

from ..helper.ext_utils.bot_utils import new_task
from ..helper.telegram_helper.button_build import ButtonMaker
from ..helper.telegram_helper.message_utils import send_message, edit_message, send_file
from ..helper.telegram_helper.filters import CustomFilters
from ..helper.telegram_helper.bot_commands import BotCommands


@new_task
async def start(_, message):
    if await CustomFilters.authorized(_, message):
        # Авторизовані користувачі: кнопки "Канал" і "Помощь"
        buttons = ButtonMaker()
        buttons.url_button("Канал", "https://t.me/+q2PQ1K33xm0xOTE0")
        buttons.url_button("Помощь", "https://t.me/ksi_fbot")
        reply_markup = buttons.build_menu(2)
        start_string = (
            "\nСпасибо за подписку! ❤️.\n"
            "Бот готов к работе.\n"
            "Данный бот умеет скачивать торренты/прямые линки, умеет скачивать "
            "с YouTube/VK/OK и многих-многих других ресурсов. \n"
            "Пропишите /help чтобы получить список всех доступных команд.\n"
        )
        await send_message(message, start_string, reply_markup)
    else:
        # Неавторизовані користувачі: кнопки "Подписка" і "Помощь"
        buttons = ButtonMaker()
        buttons.url_button("Подписка", "https://t.me/tribute/app?startapp=sMms")
        buttons.url_button("Помощь", "https://t.me/ksi_fbot")
        reply_markup = buttons.build_menu(2)
        await send_message(
            message,
            "Данный бот умеет скачивать торренты/прямые линки, умеет скачивать "
            "с YouTube/VK/OK и многих-многих других ресурсов.\n\n"
            "⚠️ ⚠️ Если хотите получить доступ к боту — оформите, пожалуйста, подписку.\n"
            "Подписка: https://t.me/tribute/app?startapp=sMms",
            reply_markup,
        )


@new_task
async def ping(_, message):
    start_time = int(round(time() * 1000))
    reply = await send_message(message, "Starting Ping")
    end_time = int(round(time() * 1000))
    await edit_message(reply, f"{end_time - start_time} ms")


@new_task
async def log(_, message):
    await send_file(message, "log.txt")
