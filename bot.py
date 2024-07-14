from aiogram import types, Bot, Dispatcher, executor
import logging
from states import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import *



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
    await Kategoriyalar.kategory.set()

@dp.callback_query_handler(state=Kategoriyalar.kategory)
async def kategory(call: types.CallbackQuery):

    if call.data == "aksiyalar":
        a = cursor.execute("SELECT * FROM product")
        txt = ""
        product_image = ""
        for i in a:
            txt += f"<b>{i[1]}</b>\n<b>Narxi:<i>{i[3]}</i></b>\n<b>Tavsif:{i[4]}</b>"
            product_image += f"{i[2]}"
            print(i)
        await call.bot.send_photo(call.from_user.id , photo=(open(product_image, "rb")),caption=txt, reply_markup=product_inline)
        await For_update_inine.btn_inline.set()

@dp.callback_query_handler(text="menu")
async def me(call: types.CallbackQuery):
    await call.message.answer("Siz asosiy menudasiz", reply_markup=meny_py)


@dp.callback_query_handler(text="bizhaqimizda")
async def bizhaqimizda(call: types.CallbackQuery):
    await call.message.answer("""Biz O‘zbekiston bozorida 12 yildan beri faoliyat yuritamiz va bugungi kunda butun mamlakat bo‘ylab 50 dan ortiq filiallarimiz mavjud. Mazali va to‘yimli taomlar, qulay narxlar, tez yetkazib berish xizmatidan mamnun mijozlar yana va yana bizni tanlamoqda.

Qaynoqqina va mazali lavashlarimiz, shaurmayu donerlarimiz, gamburger va pitsalarimizdan albatta tatib ko'rishingizni tavsiya qilamiz va buyurtmangizga tovuq go'shtidan yangiliklarimizni qo'shishni unutmang!

Yetkazib berish xizmati:  +998781500030
Sayt (https://oqtepalavash.uz/) | Facebook (http://fb.me/oqtepalavash.official) | Instagram (https://www.instagram.com/oqtepalavash.official)""",
                              reply_markup=orqaga)

def create_product_inline(count):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="-", callback_data="minus"),
                InlineKeyboardButton(text=f"{count}", callback_data="default"),
                InlineKeyboardButton(text="+", callback_data="plus"),
            ],
            [
                InlineKeyboardButton(text="Savatchaga qo'shish📥", callback_data="karzinka"),
            ],
            [
                InlineKeyboardButton(text="⬅️Asosiy menu", callback_data="asosiy"),
            ]
        ]
    )

@dp.callback_query_handler(state=For_update_inine.btn_inline)
async def plus_upate(call:types.CallbackQuery):
    user_id = call.message.chat.id
    result = cursor.execute('SELECT * FROM counts WHERE user_id=?', (user_id,)).fetchone()

    if not result:
        await check_count(user_id)
        result = cursor.execute('SELECT * FROM counts WHERE user_id=?', (user_id,)).fetchone()

    count = result[2]

    if call.data == "plus":
        count += 1
    elif call.data == "minus" and count > 0:
        count -= 1
    elif call.data == "karzinka":
        user_id = call.message.from_user.id
        a = cursor.execute("SELECT * FROM product")
        product_name = ""
        for i in a:
            product_name+=i[1]


        add_in_savat(user_id, product_name, count)
        await call.answer("buyurtmangiz savatchaga🤵‍♂️' \nTuwdi uni qabul qilib oling✅/❌")
    cursor.execute('UPDATE counts SET count_1=? WHERE user_id=?', (count, user_id))
    connect.commit()

    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=create_product_inline(count))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


