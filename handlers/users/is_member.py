from aiogram import types

from loader import dp
from keyboards.inline.channels import channelsbtns



@dp.message_handler(is_member=None)
async def join_channel(message: types.Message):
    await message.answer(
    	"Hurmatli foydalanuvchi agar kanalimizga a'zo bo'lmasangiz a'zo bo'lib qayta /start ni bosing",
    	reply_markup=await channelsbtns()
    )
