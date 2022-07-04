from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import hashlib


def register(data: dict) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text='Завершити реєстрацію',
            callback_data='register_user',
            url=f'https://nua-team-test-task.herokuapp.com/accounts/verify/?'
                f'login={data["login"]}&password={data["password"]}',
        )
    )
    return keyboard
