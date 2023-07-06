from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_17, task3_catalog_17, task4_catalog_17, task5_catalog_17, task6_catalog_17, \
    task7_catalog_17, task8_catalog_17


# ОГЭ №17 пример 1
@dp.message_handler(text="/task_catalog_17")
async def oge17_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 17:")
    await message.answer(
        f"Возьмите квадрат со стороной 8 см. Разрежьте его на четыре одинаковых частей, проведя две параллельные линии, каждая из которых пересекает противоположные вершины. Какова площадь получившихся фигур? Ответ округлите до целого числа.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: 'Задание 17 пример 1 - [ответ]', например, 'Задание 17 пример 1 - 78' или 'Задание 17 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №17 пример 2
@dp.callback_query_handler(text="t2c17")
async def oge17_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 17:")
    await call.message.answer(
        f"В прямоугольнике со сторонами a и b вырезали отверстие размером c на d. Найдите площадь получившейся фигуры, если a = 12 см, b = 9 см, c = 3 см, d = 4 см.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 17 пример 2 - [ответ]', например 'Задание 17 пример 2 - 78' или 'Задание 17 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №17 пример 3
@dp.callback_query_handler(text="t3c17")
async def oge17_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 17:")
    await call.message.answer(
        f"В параллелограмме ABCD диагональ BD делит угол B на два равных угла, а BC = a см, CD = b см и AD = c см. Найдите площадь параллелограмма, если a = 6 см, b = 8 см и c = 10 см.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 17 пример 3 - [ответ]', например 'Задание 17 пример 3 - 78' или 'Задание 17 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №17 пример 4
@dp.callback_query_handler(text="t4c17")
async def oge17_task4(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 17:")
    await call.message.answer(
        f"В треугольнике ABC проведена высота AM на сторону BC. Известно, что AB = a см, AC = b см, BM = c см и CM = d см. Найдите площадь треугольника ABC, если a = 5 см, b = 8 см, c = 3 см и d = 4 см.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 17 пример 4 - [ответ]', например 'Задание 17 пример 4 - 78' или 'Задание 17 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №17 пример 5
@dp.callback_query_handler(text="t5c17")
async def oge17_task5(call: types.CallbackQuery):
    await call.message.answer(f"Пример 5 из задания 17:")
    await call.message.answer(
        f"Найдите площадь прямоугольного треугольника, если катеты этого треугольника равны a = 6 см и b = 8 см.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 17 пример 5 - [ответ]', например 'Задание 17 пример 5 - 78' или 'Задание 17 пример 5 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №17 пример 6
@dp.callback_query_handler(text="t6c17")
async def oge17_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 6 из задания 17:")
    await call.message.answer(
        f"В равнобедренном треугольнике ABC боковая сторона BC равна a см, а высота, проведенная к основанию AB, равна h см. Найдите площадь треугольника ABC, если a = 10 см и h = 8 см.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 17 пример 6 - [ответ]', например 'Задание 17 пример 6 - 78' или 'Задание 17 пример 6 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №17 пример 7
@dp.callback_query_handler(text="t7c17")
async def oge17_task7(call: types.CallbackQuery):
    await call.message.answer(f"Пример 7 из задания 17:")
    await call.message.answer(
        f"В трапеции ABCD боковая сторона AD равна a см, основания AB и CD равны b и c см соответственно, а высота, опущенная на основание AB, равна h см. Найдите площадь трапеции ABCD, если a = 5 см, b = 9 см, c = 7 см и h = 4 см.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 17 пример 7 - [ответ]', например 'Задание 17 пример 7 - 78' или 'Задание 17 пример 7 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №17 пример 8
@dp.callback_query_handler(text="t8c17")
async def oge17_task8(call: types.CallbackQuery):
    await call.message.answer(f"Пример 8 из задания 17:")
    await call.message.answer(
        f"Дана окружность радиуса R см. Найдите площадь сегмента круга, образованного хордой длины L см, если расстояние от центра окружности до хорды равно h см, а L = 8 см, R = 10 см и h = 6 см. Ответ округлите до десятков.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 17 пример 8 - [ответ]', например 'Задание 17 пример 8 - 78' или 'Задание 17 пример 8 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 17 пример 1
@dp.message_handler(text="Задание 17 пример 1 - 192")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_17)


# ответ на задание 17 пример 2
@dp.message_handler(text="Задание 17 пример 2 - 96")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_17)


# ответ на задание 17 пример 3
@dp.message_handler(text="Задание 17 пример 3 - 48")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_17)


# ответ на задание 17 пример 4
@dp.message_handler(text="Задание 17 пример 4 - 10")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task5_catalog_17)


# ответ на задание 17 пример 5
@dp.message_handler(text="Задание 17 пример 5 - 24")
async def answer_task5(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task6_catalog_17)


# ответ на задание 17 пример 6
@dp.message_handler(text="Задание 17 пример 6 - 40")
async def answer_task6(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task7_catalog_17)


# ответ на задание 17 пример 7
@dp.message_handler(text="Задание 17 пример 7 - 32")
async def answer_task7(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task8_catalog_17)


# ответ на задание 17 пример 8
@dp.message_handler(text="Задание 17 пример 8 - 14,7")
async def answer_task8(message: types.Message):
    await message.answer(f"Верно!")
