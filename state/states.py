from aiogram.filters.state import State,StatesGroup


class Personel(StatesGroup):
    fullname = State()
    phone_number = State()
    age = State()
    kasbi = State()
    description = State()
    country = State()
    texnologiya = State()
    price = State()
    free_time = State()


class Hodim(StatesGroup):
    idora_name = State()
    phone_number = State()
    texnologiya = State()
    price = State()
    free_time = State()
    country = State()
    description = State()
    fullname = State()
    ish_vaqti = State()