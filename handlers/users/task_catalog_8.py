from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_8, task3_catalog_8


# ОГЭ №8 пример 1
@dp.message_handler(text="/task_catalog_8")
async def oge8_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 8:")
    await message.answer(f"Дано целое алгебраическое выражение: A=(5x²−3xy+7y²)−(2x²+4xy−6y²).\nНайдите значение выражения A, если x=3 и y=−2.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 8 пример 1 - [ответ]', \nнапример, 'Задание 8 пример 1 - 78' или 'Задание 8 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №8 пример 2
@dp.callback_query_handler(text="t2c8")
async def oge8_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 8:")
    await call.message.answer(f"Дано рациональное алгебраическое выражение A= (x²−4)/(x−2). Найдите значение выражения A, если x=5.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 8 пример 2 - [ответ]', например 'Задание 8 пример 2 - 78' или 'Задание 8 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №8 пример 3
@dp.callback_query_handler(text="t3c8")
async def oge8_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 8:")
    await call.message.answer(f"Найдите значение выражения 2^10+3^4−(6+4²). В ответе запишите полученное число.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 8 пример 3 - [ответ]', например 'Задание 8 пример 3 - 78' или 'Задание 8 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 8 пример 1
@dp.message_handler(text="Задание 8 пример 1 - 121")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_8)


# ответ на задание 8 пример 2
@dp.message_handler(text="Задание 8 пример 2 - 7")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_8)


# ответ на задание 8 пример 3
@dp.message_handler(text="Задание 8 пример 3 - 1061")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
