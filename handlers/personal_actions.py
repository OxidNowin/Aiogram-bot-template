# - *- coding: utf- 8 - *-
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink

from dispatcher import dp
from filters import IsAdmin
from keyboards import *
from config import BOT_ADMIN
from utils import is_user, add_user

import logging
import datetime


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ans = f"Привет, {message.from_user.first_name.title()}\n"
    if not await is_user(message.from_user.id):
        await add_user(message.from_user.id, message.from_user.username)
        ans += "Я бот!\n"
    else:
        ans += 'Рады снова тебя видеть!'

    if message.from_user.id in BOT_ADMIN:
        kb = admin_reply_kb
    else:
        kb = start_reply_kb

    await message.bot.send_message(message.chat.id, ans, reply_markup=kb)


@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    if message.from_user.id in BOT_ADMIN:
        kb = admin_reply_kb
    else:
        kb = start_reply_kb

    await message.bot.send_message(message.chat.id, "Главное меню:", reply_markup=kb)


@dp.message_handler(Text(equals='📖 Каталог'))
async def catalog(message: types.Message):
    photo = types.InputFile(f"./media/command_images/image.png")
    await message.bot.send_photo(message.chat.id,
                                 photo=photo,
                                 caption="Выберите тип товара:",
                                 reply_markup=await get_inline_kb())


@dp.message_handler(Text(equals='🚚 Доставка'))
async def delivery(message: types.Message):
    await message.bot.send_message(message.chat.id, "В разработке...", reply_markup=start_reply_kb)


@dp.message_handler(Text(equals='🧐 Гарантии'))
async def guarantees(message: types.Message):
    await message.bot.send_message(message.chat.id, "В разработке...", reply_markup=start_reply_kb)


@dp.message_handler(Text(equals='🔥 О нас'))
async def about(message: types.Message):
    await message.bot.send_message(message.chat.id, "В разработке...", reply_markup=start_reply_kb)


@dp.message_handler(Text(equals='🏠 НАШ КАНАЛ'))
async def about(message: types.Message):
    await message.bot.send_message(message.chat.id, "В разработке...", reply_markup=start_reply_kb)


@dp.message_handler(state='*', commands='⛔ Отмена')
@dp.message_handler(Text(equals='⛔ Отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info(f'From {message.from_user.id}\n'
                 f'Cancelling state {current_state}\n'
                 f'At {datetime.datetime.now()}\n\n')
    await state.finish()
    await message.reply('Отмена...', reply_markup=start_reply_kb)
