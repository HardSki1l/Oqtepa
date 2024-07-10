from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

meny_py = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒Buyurtma berish", callback_data="buyurtma"),
        ],
        [
            InlineKeyboardButton(text="ℹ️Biz haqimizda", callback_data="bizhaqimizda"),
            InlineKeyboardButton(text="🛍Buyurtmalarim", callback_data="buyurtmalarim"),
        ],
        [
            InlineKeyboardButton(text="🏘Filiallar", callback_data="filiallar"),
        ],
        [
            InlineKeyboardButton(text="✍️Fikr bildirish", callback_data="fikr_bildirish"),
            InlineKeyboardButton(text="⚙️Sozlamalar", callback_data="sozlamalar")  # Qo'shimcha qilindi
        ]
    ],
)

snakes = InlineKeyboardMarkup(
    inline_keyboard=[
       [
           InlineKeyboardButton(text="🎉Aksiyalar", callback_data="aksiyalar"),
           InlineKeyboardButton(text="Barakali setlar", callback_data="barakali"),
       ],
        [
            InlineKeyboardButton(text="🌯Lavashlar", callback_data="lavashlar"),
            InlineKeyboardButton(text="🧊Yaxna kofe", callback_data="yaxna"),
        ],
        [
            InlineKeyboardButton(text="🥤Ichimliklar",callback_data="ichimlik_cola"),
            InlineKeyboardButton(text="🍰Shirinliklar" ,callback_data="shirinliklar"),
        ],
        [
            InlineKeyboardButton(text="🍔Burger va hot doglar", callback_data="burger"),
            InlineKeyboardButton(text="🍕Pitsalar", callback_data="pitsalar"),
        ],
        [
            InlineKeyboardButton(text="🥗Salatlar", callback_data="salatlar"),
            InlineKeyboardButton(text="🥪Sendvich va Qarsildoq jo'jalar" ,callback_data="qarsildoq"),
        ],
        [
            InlineKeyboardButton(text="🥙Donerlar", callback_data="donerlar"),
            InlineKeyboardButton(text="🍟Sneklar" ,callback_data="sneklar"),
        ],
        [
            InlineKeyboardButton(text="🍅Souslar", callback_data="sousllar"),
        ],
        [
            InlineKeyboardButton(text="⬅️Asosiy menu", callback_data="asosiy"),
        ]

    ],

)