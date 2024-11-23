from aiogram import Router,types
import asyncio

from database import insert_database, insert_database2, select, select2
from keyboard.button import phone
from aiogram.fsm.context import FSMContext

from keyboard.inline import personel2
from state.states import Personel, Hodim

router = Router()




@router.callback_query(lambda call: call.data == "ish")
async def ish_handler(call:types.CallbackQuery,state:FSMContext):
    await state.set_state(Personel.fullname)
    await call.message.answer(text="Ish Topish Uchun Arizani Toldiring\n"
                                   "Toliq Ism Familyengizni Yozing")
    await call.message.delete()


@router.callback_query(Personel.age)
async def age_handler(call:types.CallbackQuery,state:FSMContext):
    age = call.data
    await state.update_data(age=age)
    await state.set_state(Personel.phone_number)
    await call.message.answer(text="Telefon Raqamingizni Jonating",reply_markup=phone())
    await call.message.delete()


@router.callback_query(Personel.country)
async def country_handler(call: types.CallbackQuery,state:FSMContext):
    viloyat = call.data
    print(viloyat)
    await state.update_data(viloyat=viloyat)
    await state.set_state(Personel.texnologiya)
    await call.message.answer(text="Texnologiyalarni Yozing")
    await call.message.delete()


@router.callback_query(lambda call:call.data == "ha")
async def ha_handler(call:types.CallbackQuery,state:FSMContext):
    await state.set_state(Personel.kasbi)
    await call.message.answer(text="Kasbingizni Yozing")
    await call.message.delete()

@router.callback_query(lambda call:call.data == "yoq")
async def yoq_handler(call:types.CallbackQuery,state:FSMContext):
    await state.set_state(Personel.description)
    await call.message.answer(text="Maqsadingizni Yoki Shu ish Boyicha Tajribangizni Yozing")
    await call.message.delete()

@router.callback_query(lambda call:call.data == "yoq2")
async def yoq_handler(call:types.CallbackQuery,state:FSMContext):
    await state.set_state(Personel.fullname)
    await call.message.answer(text="Malumotlarignizni Boshqattan Kiriting Boshqattan Kiriting")
    await call.message.delete()


@router.callback_query(lambda call:call.data == "ha2")
async def ha2_handler(call:types.CallbackQuery,state:FSMContext):
    data = await state.get_data()
    fullname = data.get("fullname")
    age = data.get("age")
    contact = data.get("phone")
    country = data.get("viloyat")
    texnologiya = data.get("texnologiya")
    kasbi = data.get("kasbi")
    price = data.get("price")
    free_time = data.get("free_time")
    description = data.get("description")
    telegram_name = call.from_user.username
    user_id = call.from_user.id
    if kasbi != None:
        insert_database(user_id,fullname,contact,kasbi,texnologiya,age,description,price,free_time,country,telegram_name)
        await call.message.answer(text="Arizangiz Muvaffaqiyatli Topshirildi")
        await state.clear()
        await call.message.delete()

    else:
        insert_database(user_id,fullname,contact,None,texnologiya,age,description,price,free_time,country,telegram_name)
        await call.message.answer(text="Arizangiz Muvaffaqiyatli Topshirildi")
        await state.clear()
        await call.message.delete()


@router.callback_query(lambda call:call.data == "hodim")
async def hodim_handler(call:types.CallbackQuery,state:FSMContext):
    await state.set_state(Hodim.fullname)
    await call.message.answer(text="To'liq Ism Familyengizni Yozing")



@router.callback_query(Hodim.country)
async def countrys2_handler(call:types.CallbackQuery,state:FSMContext):
    country = call.data
    await state.update_data(country = country)
    await state.set_state(Hodim.texnologiya)
    await call.message.answer(text="Texnologiyalarni Yozing")
    await call.message.delete()\



@router.callback_query(lambda call:call.data == "ha3")
async def ha3_handler(call:types.CallbackQuery,state:FSMContext):
    data = await state.get_data()
    idora_name = data.get("idora_ismi")
    fullname = data.get("fullname")
    phone = data.get("phone")
    country = data.get("country")
    texnologiya = data.get("texnologiya")
    price = data.get("price")
    free_time = data.get("free_time")
    description = data.get("description")
    ish_vahti = data.get("ish_vahti")
    telegram_name = call.from_user.username
    user_id = call.from_user.id
    insert_database2(user_id,idora_name,fullname,phone,texnologiya,description,price,free_time,ish_vahti,country,telegram_name)
    await call.message.answer(text="Arizangiz Muvaffaqiyatli Topshirildi")
    await state.clear()
    await call.message.delete()


@router.callback_query(lambda call:call.data == "malumotim")
async def malumotim_handler(call:types.CallbackQuery,state:FSMContext):
    user_id = call.from_user.id
    data = select(user_id)
    if data[0][6] != None:
        await call.message.answer(text=f"👨‍💼Hodim: {data[0][2]}\n"
                                  f"🕑Yosh: {data[0][6]}\n"
                                  f"🇺🇿 Hudud: {data[0][10]}\n"
                                  f"📞Aloqa: {data[0][3]}\n"
                                  f"📚Texnologiya: {data[0][5]}\n"
                                  f"👨🏻‍💻Kasbi: {data[0][4]}\n"
                                  f"🇺🇿Telegram: @{data[0][11]}\n"
                                  f"🕰Murojaat Qilish Vaqti: {data[0][9]}\n"
                                  f"💰Narxi: {data[0][8]}\n"
                                  f"🔎Maqsad: {data[0][7]}\n",reply_markup=personel2())
    else:
        await call.message.answer(text=f"👨‍💼Hodim: {data[0][2]}\n"
                                  f"🕑Yosh: {data[0][6]}\n"
                                  f"🇺🇿 Hudud: {data[0][10]}\n"
                                  f"📞Aloqa: {data[0][3]}\n"
                                  f"📚Texnologiya: {data[0][5]}\n"
                                  f"🇺🇿Telegram: @{data[0][11]}\n"
                                  f"🕰Murojaat Qilish Vaqti: {data[0][9]}\n"
                                  f"💰Narxi: {data[0][8]}\n"
                                  f"🔎Maqsad: {data[0][7]}\n")

@router.callback_query(lambda call: call.data == "hodim2")
async def hodim2_handler(call:types.CallbackQuery,state:FSMContext):
    await state.set_state(Hodim.fullname)
    await call.message.answer(text="To'liq Ism Familyengizni Yozing")

@router.callback_query(lambda call: call.data == "yoq3")
async def yoq3_handler(call: types.CallbackQuery,state:FSMContext):
    await state.set_state(Hodim.fullname)
    await call.message.answer(text="Malumotlaringizni Boshqattan Kiriting\n"
                                   "To'liq Ismingizni Yozing")

@router.callback_query(lambda call:call.data == "elonlar2")
async def elonlar_handler(call:types.CallbackQuery):
    datas = select2()
    await call.message.answer(text=f"My Datas {datas}")
