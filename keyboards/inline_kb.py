# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


good_cd = CallbackData("good", "good_type", "brand", "model", "index", "photo_index")


# Клавиатура для типа товара
async def get_inline_kb():
    buttons = []
    groups = ['1', '2', '3']

    for g in groups:
        buttons.append(InlineKeyboardButton(g, callback_data=good_cd.new(good_type='',
                                                                         brand='',
                                                                         model='',
                                                                         index=0,
                                                                         photo_index=0)))
    good_type_kb = InlineKeyboardMarkup(row_width=2)
    good_type_kb.add(*buttons)

    return good_type_kb
