from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_11


# ОГЭ №11 пример 1
@dp.message_handler(text="/task_catalog_11")
async def oge11_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 11:")
    await message.answer(
        f"На рисунке изображен график функции y = x² - 4x + 5. Используя график, определите значение функции в точке x = 2.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 11 пример 1 - [ответ]', \nнапример, 'Задание 11 пример 1 - 78' или 'Задание 11 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №11 пример 2
@dp.callback_query_handler(text="t2c11")
async def oge11_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 11:")
    await message.answer(
        f"Дана функция y = 2x² - 4x. Постройте график данной функции на интервале от x = -2 до x = 4 с шагом 1.\nОтвет напишите в порядке xy.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 11 пример 2 - [ответ]', например 'Задание 11 пример 2 - 78' или 'Задание 11 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 11 пример 1
@dp.message_handler(text="Задание 11 пример 1 - 1")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_11)


# ответ на задание 11 пример 2
@dp.message_handler(text="Задание 11 пример 2 - 12")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
