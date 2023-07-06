from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_9, task3_catalog_9, task4_catalog_9


# ОГЭ №9 пример 1
@dp.message_handler(text="/task_catalog_9")
async def oge9_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 9:")
    await message.answer(f"Дано линейное уравнение: 2x+5=3x−1. Решите уравнение и запишите ответ в виде числа.\nЕсли корней несколько, запишите их в ответ без пробелов в порядке возрастания.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 9 пример 1 - [ответ]', \nнапример, 'Задание 9 пример 1 - 78' или 'Задание 9 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №9 пример 2
@dp.callback_query_handler(text="t2c9")
async def oge9_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 9:")
    await call.message.answer(f"Решите квадратное уравнение: x²−5x+6=0.\nЕсли корней несколько, запишите их в ответ без пробелов в порядке возрастания.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 9 пример 2 - [ответ]', например 'Задание 9 пример 2 - 78' или 'Задание 9 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №9 пример 3
@dp.callback_query_handler(text="t3c9")
async def oge9_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 9:")
    await call.message.answer(f"Дано рациональное уравнение:\n3/(x−2) - 5/(x+1) = 4/(x−4)\nРешите уравнение и запишите ответ в виде целого числа или десятичной дроби. Если корней несколько, запишите наибольший.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 9 пример 3 - [ответ]', например 'Задание 9 пример 3 - 78' или 'Задание 9 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №9 пример 4
@dp.callback_query_handler(text="t4c9")
async def oge9_task4(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 9:")
    await call.message.answer(f"Даны два линейных уравнения:\n2x+5y=11\nx−2y=3\nРешите систему линейных уравнений методом вычитания.\nПроверьте, является ли найденное решение системы линейных уравнений корректным.\nВ ответ запишите результат сложения х и у.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 9 пример 4 - [ответ]', например 'Задание 9 пример 4 - 78' или 'Задание 9 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 9 пример 1
@dp.message_handler(text="Задание 9 пример 1 - −6")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_9)


# ответ на задание 9 пример 2
@dp.message_handler(text="Задание 9 пример 2 - 32")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_9)


# ответ на задание 9 пример 3
@dp.message_handler(text="Задание 9 пример 3 - 5,5")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task4_catalog_9)


# ответ на задание 9 пример 4
@dp.message_handler(text="Задание 9 пример 4 - 5")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
