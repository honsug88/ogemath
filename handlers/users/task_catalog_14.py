from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_14, task3_catalog_14


# ОГЭ №14 пример 1
@dp.message_handler(text="/task_catalog_14")
async def oge14_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 14:")
    await message.answer(
        f"В конце каждого дня на счету одного человека лежит некоторая сумма денег. В первый день, когда он начал работать, на его счету не было ни копейки. Во второй день он заработал 10 рублей, а затем каждый следующий день он зарабатывал на 2 рубля больше, чем в предыдущий день. Найдите суммарный доход этого человека за первые 20 дней работы.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: 'Задание 14 пример 1 - [ответ]', например, 'Задание 14 пример 1 - 78' или 'Задание 14 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №14 пример 2
@dp.callback_query_handler(text="t2c14")
async def oge14_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 14:")
    await call.message.answer(
        f"В арифметической прогрессии первый член равен -2, а разность равна 4. Найдите 15-й член этой прогрессии.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 14 пример 2 - [ответ]', например 'Задание 14 пример 2 - 78' или 'Задание 14 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №14 пример 3
@dp.callback_query_handler(text="t3c14")
async def oge14_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 14:")
    await call.message.answer(
        f"В геометрической прогрессии первый член равен 3, а знаменатель равен 2. Найдите сумму первых 6 членов этой прогрессии.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 14 пример 3 - [ответ]', например 'Задание 14 пример 3 - 78' или 'Задание 14 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 14 пример 1
@dp.message_handler(text="Задание 14 пример 1 - 300")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_14)


# ответ на задание 14 пример 2
@dp.message_handler(text="Задание 14 пример 2 - 58")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_14)


# ответ на задание 14 пример 3
@dp.message_handler(text="Задание 14 пример 3 - 189")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
