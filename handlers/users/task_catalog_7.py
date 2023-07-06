from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_7, task3_catalog_7, task4_catalog_7


# ОГЭ №7 пример 1
@dp.message_handler(text="/task_catalog_7")
async def oge7_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 7:")
    await message.answer(
        f"Найдите все значения x, при которых выполняется неравенство: x² - 6x + 8 ≤ 0. Ответ представьте в виде интервала.\n\nВарианты ответа:\n1) x > 4;\n2) [0,8];\n3) [6,8];\n4) [2, 4].")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 7 пример 1 - [ответ]', \nнапример, 'Задание 7 пример 1 - 78' или 'Задание 7 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №7 пример 2
@dp.callback_query_handler(text="t2c7")
async def oge7_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 7:")
    await call.message.answer(
        f"На координатной прямой даны точки A, B и C с координатами (-5; 2), (1; -1) и (4; 3) соответственно. Определите наибольшую и наименьшую из этих точек.\nОтвет напишите буквы точек в порядке возрастания.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 7 пример 2 - [ответ]', например 'Задание 7 пример 2 - 78' или 'Задание 7 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №7 пример 3
@dp.callback_query_handler(text="t3c7")
async def oge7_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 7:")
    await call.message.answer(
        f"На числовой прямой отмечены точки А(1), В(3), С(5) и D(7). Найдите координату точки Середина(АD).")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 7 пример 3 - [ответ]', например 'Задание 7 пример 3 - 78' или 'Задание 7 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №7 пример 4
@dp.callback_query_handler(text="t4c7")
async def oge7_task4(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 7:")
    await call.message.answer(
        f"Даны утверждения о координатах точек на числовой прямой. Определите и напишите, какое утверждение неверное.\n\n1) Координата точки M между точками А и В равна половине суммы координат точек А и В.\n2) Координата точки N между точками А и В равна половине разности координат точек А и В.\n3) На отрезке CD лежит точка E, тогда координата точки Е больше координаты точки С и меньше координаты точки D.\n4) Точка F находится слева от точки G на числовой прямой, то есть координата точки F меньше координаты точки G.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 7 пример 4 - [ответ]', например 'Задание 7 пример 4 - 78' или 'Задание 7 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 7 пример 1
@dp.message_handler(text="Задание 7 пример 1 - 4")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_7)


# ответ на задание 7 пример 2
@dp.message_handler(text="Задание 7 пример 2 - АС")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_7)


# ответ на задание 7 пример 3
@dp.message_handler(text="Задание 7 пример 3 - 4")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task4_catalog_7)


# ответ на задание 7 пример 4
@dp.message_handler(text="Задание 7 пример 4 - 2")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
