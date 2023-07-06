from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_13, task3_catalog_13, task4_catalog_13


# ОГЭ №13 пример 1
@dp.message_handler(text="/task_catalog_13")
async def oge13_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 13:")
    await message.answer(
        f"Решите линейное неравенство: 4x - 7 > 5x + 2\nВ ответ укажите верный вариант ответа:\n1) x > -5\n2) x ⟨ -9\n3) x = -1\n4) x ⟨ 4")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: 'Задание 13 пример 1 - [ответ]', например, 'Задание 13 пример 1 - 78' или 'Задание 13 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №13 пример 2
@dp.callback_query_handler(text="t2c13")
async def oge13_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 13:")
    await call.message.answer(
        f"Решите квадратное неравенство: x² −4<0.\nВ ответ укажите верный вариант ответа:\n1) x∈(−2,2).\n2) x∈(−∞,−2)∪(2,∞).\n3) x<−2.\n4) x>2.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 13 пример 2 - [ответ]', например 'Задание 13 пример 2 - 78' или 'Задание 13 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №13 пример 3
@dp.callback_query_handler(text="t3c13")
async def oge13_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 13:")
    await call.message.answer(
        f"Решить рациональное неравенство:\n(x/(x+2)) <= (3/4)\nВ ответ укажите верный вариант ответа:\n1) x > 6\n2) x = -2\n3) x < -2\n4) -2 < x ≤ 6")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 13 пример 3 - [ответ]', например 'Задание 13 пример 3 - 78' или 'Задание 13 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №13 пример 4
@dp.callback_query_handler(text="t4c13")
async def oge13_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 13:")
    await call.message.answer(
        f"Решить систему неравенств:\n3x - 2y ≤ 12\nx + y > 4\nx ≥ 0\ny ≥ 0\nВ ответ укажите верный вариант ответа:\n1) x > 2, y > 2\n2) x ≥ 0, y < 0\n3) 0 ≤ x, 0 ≤ y ≤ 4 - x\n4) x ≤ 0, y > 4")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 13 пример 4 - [ответ]', например 'Задание 13 пример 4 - 78' или 'Задание 13 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 13 пример 1
@dp.message_handler(text="Задание 13 пример 1 - 2")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_13)


# ответ на задание 13 пример 2
@dp.message_handler(text="Задание 13 пример 2 - 1")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_13)


# ответ на задание 13 пример 3
@dp.message_handler(text="Задание 13 пример 3 - 4")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task4_catalog_13)


# ответ на задание 13 пример 4
@dp.message_handler(text="Задание 13 пример 4 - 3")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
