import asyncio
from aiogram import Router,types

from database import select
from state.states import Personel, Hodim
from keyboard.button import phone
from keyboard.inline import personel, countrys, generate_inline_keyboard, yes_or_no, yes_or_no2, personel2, yes_or_no3
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(CommandStart())
async def start(message:types.Message):
    user_id = message.from_user.id
    if not select(user_id):
        first_name = message.from_user.first_name
        await message.answer(text=f"Ish Topish Yoki Hodim Topish Botiga Hush Kelibsiz {first_name} 🤗\n"
                                  f"Bizning Bot Sizga Qanday Yordam Bera Oladi ?.",reply_markup=personel())
    else:return await message.answer(text="Siz Ariza Topshirbogansiz",reply_markup=personel2())

@router.message(Personel.fullname)
async def fullname_handler(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(fullname=fullname)
    await state.set_state(Personel.age)
    await message.answer(text="Yoshingizni Tanlang",reply_markup=generate_inline_keyboard())
    await message.delete()



@router.message(Personel.phone_number)
async def phone_handler(message:  types.Message,  state:FSMContext):
    if message.contact:
        contact = message.contact.phone_number
        await state.update_data(phone=contact)
        await state.set_state(Personel.country)
        await message.answer(text="Viloyatingizni Tanlang",reply_markup=countrys())
        await message.delete()
    else:
        await message.answer(text="Iltimos Faqat Tilifon Raqamingizni Jonating",reply_markup=phone())


@router.message(Personel.texnologiya)
async def texnologiya_handler(message: types.Message,state:FSMContext):
    texnologiya = message.text
    await state.update_data(texnologiya=texnologiya)
    await message.answer(text="Kasbingiz Ni Ham Qoshasizmi ?",reply_markup=yes_or_no())
    await message.delete()

@router.message(Personel.kasbi)
async def kasbi_handler(message:types.Message,state:FSMContext):
    kasbi = message.text
    await state.update_data(kasbi=kasbi)
    await state.set_state(Personel.description)
    await message.answer(text="Maqsadingiz Yoki Ish Boyicha Tajribangizni Yozing")

@router.message(Personel.description)
async def description_handler(message:types.Message,state:FSMContext):
    description = message.text
    await state.update_data(description=description)
    await state.set_state(Personel.price)
    await message.answer(text="Ish Boyicha Maoshingizni yozing")

@router.message(Personel.price)
async def price_handler(message:types.Message,state:FSMContext):
    price = message.text
    await state.update_data(price=price)
    await state.set_state(Personel.free_time)
    await message.answer(text="Murojaat Qilish Vaqtingizni Yozing")


@router.message(Personel.free_time)
async  def free_time_handler(message:types.Message,state:FSMContext):
    free_time = message.text
    await state.update_data(free_time=free_time)
    data = await state.get_data()
    fullname = data.get("fullname")
    age = data.get("age")
    contact = data.get("phone")
    country = data.get("viloyat")
    texnologiya = data.get("texnologiya")
    kasbi = data.get("kasbi")
    description = data.get("description")
    free_time = data.get("free_time")
    price = data.get("price")
    telegram_name = message.from_user.username
    if kasbi != None:
        await message.answer(text=f"Bu Malumotlaringizni Tasdiqlaysizmi ?\n"
                                  f"👨‍💼Hodim: {fullname}\n"
                                  f"🕑Yosh: {age}\n"
                                  f"🇺🇿 Hudud: {country}\n"
                                  f"📞Aloqa: {contact}\n"
                                  f"📚Texnologiya: {texnologiya}\n"
                                  f"👨🏻‍💻Kasbi: {kasbi}\n"
                                  f"🇺🇿Telegram: @{telegram_name}\n"
                                  f"🕰Murojaat Qilish Vaqti: {free_time}\n"
                                  f"💰Narxi: {price}\n"
                                  f"🔎Maqsad: {description}\n",reply_markup=yes_or_no2())
    else:
        await message.answer(text=f"Bu Malumotlaringizni Tasdiqlaysizmi ?\n"
                                  f"👨‍💼Hodim: {fullname}\n"
                                  f"🕑Yosh: {age}\n"
                                  f"🌐Hudud: {country}\n"
                                  f"📞Aloqa: {contact}\n"
                                  f"📚Texnologiya: {texnologiya}\n"
                                  f"🇺🇿Telegram: @{telegram_name}\n"
                                  f"🕰Murojaat Qilish Vaqti: {free_time}\n"
                                  f"💰Narxi: {price}\n"
                                  f"🔎Maqsad: {description}\n"
                                  ,reply_markup=yes_or_no2())


@router.message(Hodim.fullname)
async def fullname(message:types.Message,state:FSMContext):
    fullname = message.text
    await state.update_data(fullname=fullname)
    await state.set_state(Hodim.idora_name)
    await message.answer(text="Idorani ismini Yozing")

@router.message(Hodim.idora_name)
async def idora_name_handler(message:types.Message,state:FSMContext):
    idora_ismi = message.text
    await state.update_data(idora_ismi = idora_ismi)
    await state.set_state(Hodim.country)
    await message.answer(text="Hududni Tanlang",reply_markup=countrys())


@router.message(Hodim.texnologiya)
async def texnologiya2_handler(message:types.Message,state:FSMContext):
    texnologiya = message.text
    await state.update_data(texnologiya = texnologiya)
    await state.set_state(Hodim.ish_vaqti)
    await message.answer(text="Ish Vahtini Yozing")


@router.message(Hodim.ish_vaqti)
async def ish_vahti_handler(message:types.Message,state:FSMContext):
    ish_vahti = message.text
    await state.update_data(ish_vahti=ish_vahti)
    await state.set_state(Hodim.price)
    await message.answer(text="Maoshni Yozing")


@router.message(Hodim.price)
async def price2_handler(message:types.Message,state:FSMContext):
    price = message.text
    await state.update_data(price = price)
    await state.set_state(Hodim.description)
    await message.answer(text="Ish Haqida Qo'shimcha Narsa Yozing")

@router.message(Hodim.description)
async def description2_handler(message:types.Message,state:FSMContext):
    description = message.text
    await state.update_data(description = description)
    await state.set_state(Hodim.free_time)
    await message.answer(text="Bosh Vahtingizni Yozing")

@router.message(Hodim.free_time)
async def free_time2_handler(message:types.Message,state:FSMContext):
    free_time = message.text
    await state.update_data(free_time = free_time)
    await state.set_state(Hodim.phone_number)
    await message.answer(text="Telefon Raqamingizni Jonating",reply_markup=phone())

@router.message(Hodim.phone_number)
async def phone_handler(message:  types.Message,  state:FSMContext):
    if message.contact:
        contact = message.contact.phone_number
        await state.update_data(phone=contact)
        data = await state.get_data()
        idora_ismi = data.get("idora_ismi")
        fullname = data.get("fullname")
        contact = data.get("phone")
        country = data.get("country")
        texnologiya = data.get("texnologiya")
        price = data.get("price")
        free_time = data.get("free_time")
        ish_vahti = data.get("ish_vahti")
        description = data.get("description")
        telegram_name = message.from_user.username

        await message.answer(text="Malumotlaringizni Tasdiqlaysizmi ?\n"
                                  f"🏢Idora: {idora_ismi}\n"
                                  f"📚Texnologiya: {texnologiya}\n"
                                  f"🇺🇿Telegram: @{telegram_name}\n"
                                  f"📞Aloqa: {contact}\n"
                                  f"🌐 Hudud: {country}\n"
                                  f"✍️Ma'sul: {fullname}\n"
                                  f"🕰Murojaat Vaqti: {free_time}\n"
                                  f"🕰Ish Vaqti: {ish_vahti}\n"
                                  f"💰Maosh: {price}\n"
                                  f"‼️Qo'shimcha: {description}",reply_markup=yes_or_no3())
        await message.delete()
    else:
        await message.answer(text="Iltimos Faqat Tilifon Raqamingizni Jonating",reply_markup=phone())
