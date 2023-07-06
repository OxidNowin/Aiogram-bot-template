# - *- coding: utf- 8 - *-
import config
from dispatcher import dp
from keyboards import *


@dp.callback_query_handler(lambda call: call.data == 'good_type')
async def choose_type(call: types.CallbackQuery):
    media = types.InputMediaPhoto(media=types.InputFile(f"./media/command_images/image.png"),
                                  caption="Выберите тип товара:")
    await call.bot.edit_message_media(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      media=media,
                                      reply_markup=await get_inline_kb())
