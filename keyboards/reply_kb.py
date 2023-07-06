# - *- coding: utf- 8 - *-
from aiogram import types


start_reply_kb = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                           input_field_placeholder='Выберите раздел на клавиатуре')
start_reply_kb.row('📖 Каталог')
start_reply_kb.row('🚚 Доставка', '🧐 Гарантии')
start_reply_kb.row('🔥 О нас', '🏠 НАШ КАНАЛ')

admin_reply_kb = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                           input_field_placeholder='Выберите раздел на клавиатуре')
admin_reply_kb.row('📖 Каталог')
admin_reply_kb.row('🚚 Доставка', '🧐 Гарантии')
admin_reply_kb.row('🔥 О нас')
admin_reply_kb.row('🖼️ Загрузить изображения')

cancel_reply_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
cancel_reply_kb.row('⛔ Отмена')
