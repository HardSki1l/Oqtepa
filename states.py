from aiogram.dispatcher.filters.state import State, StatesGroup


class STATES(StatesGroup):
    location = State()


class Kategoriyalar(StatesGroup):
    kategory = State()

class ProductStates(StatesGroup):
    product = State()

class For_update_inine(StatesGroup):
    btn_inline = State()