from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_2, task3_catalog_2, task4_catalog_2, task5_catalog_2, task6_catalog_2, task7_catalog_2


# ОГЭ №2 пример 1
@dp.message_handler(text="/task_catalog_2")
async def oge2_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 2:")
    await message.answer(f"В одной квартире живут три семьи: Андреевы, Беловы и Васильевы. У Андреевых 2 комнаты, у Беловых - на 1 комната больше, чем у Андреевых, а у Васильевых на 1 комната меньше, чем у Беловых. Сколько комнат в квартире у каждой из этих семей, если всего в квартире есть 12 комнат?")
    await message.answer(f"Ответ написать в порядке 'Андреевых Беловых Васильевых' без пробелов и знаков препинания.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 2 пример 1 - [ответ]', \nнапример, 'Задание 2 пример 1 - 78' или 'Задание 2 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №2 пример 2
@dp.callback_query_handler(text="t2c2")
async def oge2_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 2:")
    await call.message.answer(f"В селе Поляна на продажу выставлены три участка земли: два садовых и один для строительства сарая. Первый садовый участок имеет площадь 0,6 гектара, а второй - на 20% больше первого. Участок для строительства сарая имеет длину 40 метров и ширину 25 метров. На каждом садовом участке саженцы размещены в рядах, расстояние между которыми составляет 1 метр. Какое количество саженцев нужно приобрести для посадки на обоих садовых участках, если на одном саженце занимается площадь 0,2 квадратного метра?")

    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 2 пример 2 - [ответ]', например 'Задание 2 пример 2 - 78' или 'Задание 2 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №2 пример 3
@dp.callback_query_handler(text="t3c2")
async def oge2_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 2:")
    await call.message.answer(f"Друзья решили отправиться в путешествие на автомобиле. Они проехали 150 км за первый час, затем скорость увеличили на 20% и проехали еще 180 км. Какое расстояние они проехали всего?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 2 пример 3 - [ответ]', например 'Задание 2 пример 3 - 78' или 'Задание 2 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №2 пример 4
@dp.callback_query_handler(text="t4c2")
async def oge2_task4(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 2:")
    await call.message.answer(f"В тепличном хозяйстве для выращивания овощей используются теплицы, которые изготавливаются из пластика или бумаги. Для изготовления одной бумажной теплицы нужно 5 рулонов бумаги размером 70 метров на 50 см. Сколько метров бумаги потребуется для изготовления 10 таких теплиц?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 2 пример 4 - [ответ]', например 'Задание 2 пример 4 - 78' или 'Задание 2 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №2 пример 5
@dp.callback_query_handler(text="t5c2")
async def oge2_task5(call: types.CallbackQuery):
    await call.message.answer(f"Пример 5 из задания 2:")
    await call.message.answer(f"Михаил отправился в путешествие на своем автомобиле. Он проехал первый день 200 км, затем каждый следующий день он проезжал на 10% больше, чем в предыдущий день. На сколько процентов дальше от стартовой точки оказался Михаил после третьего дня поездки?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 2 пример 5 - [ответ]', например 'Задание 2 пример 5 - 78' или 'Задание 2 пример 5 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №2 пример 6
@dp.callback_query_handler(text="t6c2")
async def oge2_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 6 из задания 2:")
    await call.message.answer(f"В одном доме 18 квартир. Если каждый житель затрачивает в день на коммунальные услуги в среднем 20 рублей, то сколько денег нужно выплатить за все квартиры за месяц, если месяц содержит 30 дней? Ответ округлите до целого числа.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 2 пример 6 - [ответ]', например 'Задание 2 пример 6 - 78' или 'Задание 2 пример 6 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №2 пример 7
@dp.callback_query_handler(text="t7c2")
async def oge2_task7(call: types.CallbackQuery):
    await call.message.answer(f"Пример 7 из задания 2:")
    await call.message.answer(f"В автобусной компании закупили новые шины для автобусов. Каждая шина имеет диаметр 70 см. Сколько оборотов сделает колесо автобуса, если оно проехало расстояние 5 км? Ответ округлите до целого числа.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 2 пример 7 - [ответ]', например 'Задание 2 пример 7 - 78' или 'Задание 2 пример 7 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 2 пример 1
@dp.message_handler(text="Задание 2 пример 1 - 232")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_2)


# ответ на задание 2 пример 2
@dp.message_handler(text="Задание 2 пример 2 - 66000")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_2)


# ответ на задание 2 пример 3
@dp.message_handler(text="Задание 2 пример 3 - 330")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task4_catalog_2)


# ответ на задание 2 пример 4
@dp.message_handler(text="Задание 2 пример 4 - 1750")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task5_catalog_2)


# ответ на задание 2 пример 5
@dp.message_handler(text="Задание 2 пример 5 - 231")
async def answer_task5(message: types.Message):
    await message.answer(f"Верно!\n")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task6_catalog_2)


# ответ на задание 2 пример 6
@dp.message_handler(text="Задание 2 пример 6 - 108000")
async def answer_task6(message: types.Message):
    await message.answer(f"Верно!\n")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task7_catalog_2)


# ответ на задание 2 пример 7
@dp.message_handler(text="Задание 2 пример 7 - 232")
async def answer_task6(message: types.Message):
    await message.answer(f"Верно!\n")
