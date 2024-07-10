from aiogram import types, Bot, Dispatcher, executor
import logging
from states import STATES
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from Keyboards.inline import *
from Keyboards.default import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.types import Contact

logging.basicConfig(level=logging.INFO)
API_TOKEN = "7382006281:AAEJk6Tq-Jxh-VVOZaADPzA4rBcgahMZa_w"
bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Buyurtmani birga joylashtiramizmi? 🤗")
    await message.answer("Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing\nShuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin\nOqtepa Lavash menu (https://telegra.ph/Taomnoma-09-30)", reply_markup=meny_py)




@dp.callback_query_handler(text='buyurtma')
async def buyurtmaa(call:types.CallbackQuery):
    await call.message.answer("Buyurtmani birga joylashtiramizmi? 🤗")

    await call.message.answer("Buyurtma turni tanlang:",reply_markup=turini_tanlang_btn)

from aiogram import types, Bot, Dispatcher, executor
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Keyboards.inline import *
from Keyboards.default import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.types import Contact

logging.basicConfig(level=logging.INFO)
API_TOKEN = "7382006281:AAEJk6Tq-Jxh-VVOZaADPzA4rBcgahMZa_w"
bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Buyurtmani birga joylashtiramizmi? 🤗")
    await message.answer("Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing\nShuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin\nOqtepa Lavash menu (https://telegra.ph/Taomnoma-09-30)", reply_markup=meny_py)




@dp.callback_query_handler(text='buyurtma')
async def buyurtmaa(call:types.CallbackQuery):
    await call.message.answer("Buyurtmani birga joylashtiramizmi? 🤗")

    await call.message.answer("Buyurtma turni tanlang:",reply_markup=turini_tanlang_btn)



@dp.message_handler(text='🛵 Eltib berish')
async def eltib_berishs(message: types.Message):
    await message.answer("<b>Eltib berish</b> uchun <b>geo-joylashuvni</b> jo'nating yoki manzilni tanlang",reply_markup=lokatsiya_btn)
    await STATES.location.set()

@dp.message_handler(state=STATES.location, content_types=types.ContentType.LOCATION)
async def locattion(message: types.Message, state: FSMContext):
    await message.answer("""
Buyurtma qilmoqchi bo'lgan manzilingiz: 
Ташкент, Юнусабадский район, массив Юнусабад, 4-й квартал, 69A
Ushbu manzilni tasdiqlaysizmi?    
""",reply_markup=ha_yoq_btn)
    await state.finish()

@dp.message_handler(text="❎ Yo'q")
async def ha_yoq(message: types.Message):
    await message.answer("Eltib berish uchun geo-joylashuvni jo'nating yoki manzilni tanlang", reply_markup=lokatsiya_btn )

@dp.message_handler(text="✅ Ha")
async def ha_yoq(message: types.Message):
    await message.answer("Buyurtmani birga joylashtiramizmi? 🤗")
    await message.answer(""" 
    <a href = "https://telegra.ph/Taomnoma-09-30">Kategoriyalardan birini tanlang.</a>""", reply_markup=snakes)








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


