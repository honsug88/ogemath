from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_12, task3_catalog_12


# ОГЭ №12 пример 1
@dp.message_handler(text="/task_catalog_12")
async def oge12_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 12:")
    await message.answer(f"Дано уравнение x² - 5x + 6 = 0.\nНайдите наибольный корень уравнения с помощью формулы:\nx = (5 ± √(5² - 4·1·6)) / (2·1)")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: 'Задание 12 пример 1 - [ответ]', например, 'Задание 12 пример 1 - 78' или 'Задание 12 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №12 пример 2
@dp.callback_query_handler(text="t2c12")
async def oge12_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 12:")
    await call.message.answer(
        f"Решите линейное уравнение: 3x+4=10−2x.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 12 пример 2 - [ответ]', например 'Задание 12 пример 2 - 78' или 'Задание 12 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №12 пример 3
@dp.callback_query_handler(text="t3c12")
async def oge12_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 12:")
    await call.message.answer(
        f"Известно, что площадь треугольника равна 24 квадратных см, а высота, проведенная к основанию треугольника, равна 6 см. Найдите длину этого основания.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 12 пример 3 - [ответ]', например 'Задание 12 пример 3 - 78' или 'Задание 12 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 12 пример 1
@dp.message_handler(text="Задание 12 пример 1 - 3")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_12)


# ответ на задание 12 пример 2
@dp.message_handler(text="Задание 12 пример 2 - 1,2")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_12)


# ответ на задание 12 пример 3
@dp.message_handler(text="Задание 12 пример 3 - 8")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
