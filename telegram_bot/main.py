import os

import aiogram

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from dotenv import load_dotenv

from keyboards import register
from db import DBUser

load_dotenv()

storage = MemoryStorage()

bot: Bot = Bot(os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
dp: Dispatcher = Dispatcher(bot, storage=storage)


class RegisterSteps(StatesGroup):
    get_password = State()


@dp.message_handler(commands=['start'], state=None)
async def cmd_start(message: types.Message):
    args = message.get_args()
    if args == 'register_user':
        await message.answer(
            'Привіт!\n'
            'Для завершення реєстрації заповніть анкету.',
        )
        await message.answer('Введіть пароль')
        await RegisterSteps.get_password.set()
    elif args.isnumeric():
        user = await bot.get_chat(int(args))
        await message.answer(
            f'Профіль користувача з ідентифікатором {args} знайдено\n'
            f'<a href="tg://user?id={args}">{user.full_name}</a>',
        )
    else:
        await message.answer(
            'Привіт.\n'
            'Цей бот створений для реєстації користувачів.\n'
            'Якщо ви хочете зареєструватися перейдіть на сайт ...'
        )


@dp.message_handler(state=RegisterSteps.get_password)
async def get_password(message: types.Message, state: FSMContext):
    username = message.from_user.username if message.from_user.username else message.from_user.id
    await state.update_data(password=message.text, login=username)

    data = await state.get_data()
    db = DBUser()
    user = db.get_user(data['login'])

    if not user:
        db.add_user(
            data['login'],
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.last_name,
            message.to_python(),
            message.date
        )
        await message.answer(
            'Чудово!\n'
            f'Login: {data["login"]}\n'
            f'Password: {data["password"]}\n\n'
            'Завершіть реєстрацію',
            reply_markup=register(data)
        )
        await state.finish()
    else:
        await message.answer(
            'Такий користувач вже існує\n'
            'Спробуйте ще раз'
        )
        await state.finish()

    del db


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
