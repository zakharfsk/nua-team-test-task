from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import hashlib


def register(data: dict) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text='Завершити реєстрацію',
            callback_data='register_user',
            url=f'http://127.0.0.1:8000/accounts/verify/?login={data["login"]}&password={data["password"]}',
        )
    )
    return keyboard
