from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup




def personel():
    design = [[InlineKeyboardButton(text="Ish Kerak👨‍💻",callback_data="ish"),
         InlineKeyboardButton(text="Hodim Kerak👤",callback_data="hodim")],
              [InlineKeyboardButton(text="Hamma Elonlar📢",callback_data="elonlar")]]
    markup = InlineKeyboardMarkup(inline_keyboard=design)
    return markup


def personel2():
    design = [[InlineKeyboardButton(text="Hodim Kerak👤",callback_data="hodim2"),
               InlineKeyboardButton(text="Malumotlarim🗂",callback_data="malumotim")],
              [InlineKeyboardButton(text="Hamma Elonlar📢",callback_data="elonlar2")]]
    markup = InlineKeyboardMarkup(inline_keyboard=design)
    return markup

def countrys():
    design = [[InlineKeyboardButton(text="Toshkent SH.",callback_data="Toshkent SH."),
               InlineKeyboardButton(text="Samarqand SH.",callback_data="Samarqand SH."),
               InlineKeyboardButton(text="Buxoro SH.",callback_data="Buxoro SH.")],
              [InlineKeyboardButton(text="Andijon SH.",callback_data="Andijon SH."),
               InlineKeyboardButton(text="Farg'ona SH.",callback_data="Farg'ona SH."),
               InlineKeyboardButton(text="Jizzax SH.",callback_data="Jizzax SH.")],
              [InlineKeyboardButton(text="Namangan SH.",callback_data="Namangan SH."),
               InlineKeyboardButton(text="Navoiy SH.",callback_data="Navoiy SH."),
               InlineKeyboardButton(text="Qashqadaryo SH.",callback_data="Qashqadaryo SH.")],
              [InlineKeyboardButton(text="Sirdaryo SH.",callback_data="Sirdaryo SH."),
               InlineKeyboardButton(text="Surxandaryo SH.",callback_data="Surxandaryo SH."),
               InlineKeyboardButton(text="Xorazm SH.",callback_data="Xorazm SH.")]]
    markup = InlineKeyboardMarkup(inline_keyboard = design)
    return markup


def generate_inline_keyboard():
    # Klavyeyi oluşturmak için liste
    keyboard = []
    # 14'ten 60'a kadar olan sayılarla bir düğme oluştur
    for i in range(14, 61):
        # Her 5 düğmede bir yeni bir satır ekle
        if (i - 14) % 5 == 0:
            keyboard.append([])
        keyboard[-1].append(InlineKeyboardButton(text=str(i), callback_data=f"{i}"))

    # InlineKeyboardMarkup'e ekle ve döndür
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def yes_or_no():
    design = [[InlineKeyboardButton(text="Ha✅",callback_data="ha"),
               InlineKeyboardButton(text="Yoq❌",callback_data="yoq")]]
    markup = InlineKeyboardMarkup(inline_keyboard = design)
    return markup

def yes_or_no2():
    design = [[InlineKeyboardButton(text="Ha✅",callback_data="ha2"),
               InlineKeyboardButton(text="Boshqattan Kirit❌",callback_data="yoq2")]]
    markup = InlineKeyboardMarkup(inline_keyboard = design)
    return markup


def yes_or_no3():
    design = [[InlineKeyboardButton(text="Ha✅",callback_data="ha3"),
               InlineKeyboardButton(text="Yoq❌",callback_data="yoq3")]]
    markup = InlineKeyboardMarkup(inline_keyboard = design)
    return markup

