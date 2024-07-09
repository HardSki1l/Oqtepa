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
