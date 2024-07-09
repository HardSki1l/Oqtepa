from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

turini_tanlang_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛵 Eltib berish"),
            KeyboardButton(text="🚶 Borib olish")
        ],
        [
            KeyboardButton(text="⬅ Ortga")
        ]
    ],
    resize_keyboard=True
)


lokatsiya_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍Geo-joylashuvni yuboring",request_location=True)
        ],
        [
            KeyboardButton(text="⬅ Ortga"),
        ],
    ],
    resize_keyboard=True
)
ha_yoq_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❎ Yo'q"),
            KeyboardButton(text="✅ Ha")
        ],
    ],
    resize_keyboard=True
)