from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_15, task3_catalog_15, task4_catalog_15, task5_catalog_15, task6_catalog_15, \
    task7_catalog_15, task8_catalog_15


# ОГЭ №15 пример 1
@dp.message_handler(text="/task_catalog_15")
async def oge15_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 15:")
    await message.answer(
        f"Изображен треугольник ABC. Известно, что угол BAC равен 60°, AB = AC и BD - биссектриса угла ABC. Найдите угол ADB.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: 'Задание 15 пример 1 - [ответ]', например, 'Задание 15 пример 1 - 78' или 'Задание 15 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №15 пример 2
@dp.callback_query_handler(text="t2c15")
async def oge15_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 15:")
    await call.message.answer(
        f"Изображен треугольник ABC. Известно, что угол BAC равен 45°, AB = 6 см и AC = 8 см. Найдите длину биссектрисы угла BAC. Ответ округлить до сотых.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 15 пример 2 - [ответ]', например 'Задание 15 пример 2 - 78' или 'Задание 15 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №15 пример 3
@dp.callback_query_handler(text="t3c15")
async def oge15_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 15:")
    await call.message.answer(
        f"Изображен треугольник ABC, в котором AB = AC. Известно, что угол BAC равен 100°. Найдите угол ABC.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 15 пример 3 - [ответ]', например 'Задание 15 пример 3 - 78' или 'Задание 15 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №15 пример 4
@dp.callback_query_handler(text="t4c15")
async def oge15_task4(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 15:")
    await call.message.answer(
        f"Изображен прямоугольный треугольник ABC, в котором угол BAC равен 90°. Известно, что AB = 6 см и BC = 8 см. Найдите длину гипотенузы AC.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 15 пример 4 - [ответ]', например 'Задание 15 пример 4 - 78' или 'Задание 15 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №15 пример 5
@dp.callback_query_handler(text="t5c15")
async def oge15_task5(call: types.CallbackQuery):
    await call.message.answer(f"Пример 5 из задания 15:")
    await call.message.answer(
        f"Изображен параллелограмм ABCD. Известно, что сторона AB равна 6 см, а высота, опущенная на сторону AB, равна 4 см. Найдите площадь параллелограмма ABCD.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 15 пример 5 - [ответ]', например 'Задание 15 пример 5 - 78' или 'Задание 15 пример 5 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №15 пример 6
@dp.callback_query_handler(text="t6c15")
async def oge15_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 6 из задания 15:")
    await call.message.answer(
        f"Дан ромб ABCD со стороной a = 12 см. Найдите площадь ромба, если высота опущена из вершины A на сторону CD, а диагональ BD равна b = 20 см.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 15 пример 6 - [ответ]', например 'Задание 15 пример 6 - 78' или 'Задание 15 пример 6 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №15 пример 7
@dp.callback_query_handler(text="t7c15")
async def oge15_task7(call: types.CallbackQuery):
    await call.message.answer(f"Пример 7 из задания 15:")
    await call.message.answer(
        f"Дана трапеция ABCD, в которой сторона AB параллельна стороне CD. Известно, что AB = 8 см, BC = 12 см, а диагональ BD является высотой трапеции. Найдите площадь трапеции.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 15 пример 7 - [ответ]', например 'Задание 15 пример 7 - 78' или 'Задание 15 пример 7 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №15 пример 8
@dp.callback_query_handler(text="t8c15")
async def oge15_task8(call: types.CallbackQuery):
    await call.message.answer(f"Пример 8 из задания 15:")
    await call.message.answer(
        f"В многоугольнике ABCDEFGH длины сторон равны соответственно: AB = 5 см, BC = 8 см, CD = 6 см, DE = 4 см, EF = 6 см, FG = 7 см, GH = 9 см и HA = 10 см. Найдите периметр многоугольника.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 15 пример 8 - [ответ]', например 'Задание 15 пример 8 - 78' или 'Задание 15 пример 8 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 15 пример 1
@dp.message_handler(text="Задание 15 пример 1 - 60")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_15)


# ответ на задание 15 пример 2
@dp.message_handler(text="Задание 15 пример 2 - 13,33")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_15)


# ответ на задание 15 пример 3
@dp.message_handler(text="Задание 15 пример 3 - 40")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_15)


# ответ на задание 15 пример 4
@dp.message_handler(text="Задание 15 пример 4 - 10")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task5_catalog_15)


# ответ на задание 15 пример 5
@dp.message_handler(text="Задание 15 пример 5 - 24")
async def answer_task5(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task6_catalog_15)


# ответ на задание 15 пример 6
@dp.message_handler(text="Задание 15 пример 6 - 60")
async def answer_task6(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task7_catalog_15)


# ответ на задание 15 пример 7
@dp.message_handler(text="Задание 15 пример 7 - 94,44 ")
async def answer_task7(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task8_catalog_15)


# ответ на задание 15 пример 8
@dp.message_handler(text="Задание 15 пример 8 - 55")
async def answer_task8(message: types.Message):
    await message.answer(f"Верно!")
