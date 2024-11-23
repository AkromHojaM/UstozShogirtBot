from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton


def phone():
    design = [[KeyboardButton(text="Telefon Raqamini Jonat📱",request_contact=True)]]
    markup = ReplyKeyboardMarkup(keyboard=design,one_time_keyboard=True,resize_keyboard=True)
    return markup