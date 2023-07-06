from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_16, task3_catalog_16


# ОГЭ №16 пример 1
@dp.message_handler(text="/task_catalog_16")
async def oge16_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 16:")
    await message.answer(
        f"На окружности с центром O и радиусом 10 см выбраны две точки A и B так, что угол AOB равен 60°. Найдите длину дуги между точками A и B.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: 'Задание 16 пример 1 - [ответ]', например, 'Задание 16 пример 1 - 78' или 'Задание 16 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №16 пример 2
@dp.callback_query_handler(text="t2c16")
async def oge16_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 16:")
    await call.message.answer(
        f"Дана окружность с центром O и радиусом 4 см, точки A, B, C такие, что AB является диаметром, а AC - касательной к окружности в точке A. Найдите длину отрезка BC.\nКонечный результат умножить на 1².")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 16 пример 2 - [ответ]', например 'Задание 16 пример 2 - 78' или 'Задание 16 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №16 пример 3
@dp.callback_query_handler(text="t3c16")
async def oge16_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 16:")
    await call.message.answer(
        f"В многоугольнике ABCDEFGH окружность описана таким образом, что касается всех его сторон. Известно, что сторона AB равна 10 см, а диагональ BF равна 14 см. Найдите площадь многоугольника ABCDEFGH (ответ дайте в см^2).")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 16 пример 3 - [ответ]', например 'Задание 16 пример 3 - 78' или 'Задание 16 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 16 пример 1
@dp.message_handler(text="Задание 16 пример 1 - 20,9")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_16)


# ответ на задание 16 пример 2
@dp.message_handler(text="Задание 16 пример 2 - 7")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_16)


# ответ на задание 16 пример 3
@dp.message_handler(text="Задание 16 пример 3 - 424")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")

