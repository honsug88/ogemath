from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_3, task3_catalog_3, task4_catalog_3, task5_catalog_3, task6_catalog_3, task7_catalog_3


# ОГЭ №3 пример 1
@dp.message_handler(text="/task_catalog_3")
async def oge3_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 3:")
    await message.answer(
        f"Квартира имеет форму прямоугольника со сторонами 6 м и 8 м. На полу квартиры лежит ковер, площадь которого равна 24 квадратных метра. Какая часть пола не покрыта ковром? Ответ округлите до одного знака после запятой.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 3 пример 1 - [ответ]', \nнапример, 'Задание 3 пример 1 - 78' или 'Задание 3 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №3 пример 2
@dp.callback_query_handler(text="t2c3")
async def oge3_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 3:")
    await call.message.answer(
        f"В провинциальном городе на окраине была проведена заброшенная территория, на которой были расположены несколько сараев и садовых участков. Площадь каждого сарая составляет 400 квадратных метров, а площадь каждого садового участка - 225 квадратных метров. На этой территории также находится улица, ширина которой равна 8 метрам. Известно, что сараи расположены с периодичностью в 20 метров, а садовые участки - в 10 метров относительно друг друга и сараев. Найдите площадь земельного участка, ограниченного одним сараем, двумя соседними садовыми участками и улицей.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 3 пример 2 - [ответ]', например 'Задание 3 пример 2 - 78' или 'Задание 3 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №3 пример 3
@dp.callback_query_handler(text="t3c3")
async def oge3_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 3:")
    await call.message.answer(
        f"Вы отправляетесь в путешествие на автомобиле, которое начинается в городе А и заканчивается в городе В. На карте вы замечаете, что ваш маршрут проходит через ряд деревень, расположенных на разных расстояниях друг от друга. Найти общую площадь земли, которую вы проезжаете на пути от города А до города В, если известно, что каждая деревня находится на расстоянии 20 км от предыдущей и следующей деревни, а ширина дороги равна 8 метрам.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 3 пример 3 - [ответ]', например 'Задание 3 пример 3 - 78' или 'Задание 3 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №3 пример 4
@dp.callback_query_handler(text="t4c3")
async def oge3_task4(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 3:")
    await call.message.answer(
        f"В автомастерской имеется необходимость заменить шину на одном из автомобилей. Для этого необходимо выбрать подходящую шину, площадь поверхности контакта которой с дорогой будет равна 300 квадратных сантиметров. Но в автомастерской нет соответствующих шин. Вместо этого механик предлагает использовать теплицы, которые у него есть в наличии. Известно, что площадь одной теплицы равна 24 квадратным метрам, а размеры теплицы составляют 6 метров в длину и 4 метра в ширину. Сколько минимум теплиц понадобится для замены шины, при условии, что контактная площадь между каждой теплицей и дорогой равна 100% и площадь одного слоя бумаги, используемой для защиты диска от краски, равна 50 квадратным сантиметрам?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 3 пример 4 - [ответ]', например 'Задание 3 пример 4 - 78' или 'Задание 3 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №3 пример 5
@dp.callback_query_handler(text="t5c3")
async def oge3_task5(call: types.CallbackQuery):
    await call.message.answer(f"Пример 5 из задания 3:")
    await call.message.answer(
        f"На карте местности точки А(2;5) и В(8;9) соединены прямой линией. Найдите площадь четырехугольника, образованного отрезком АВ, осью ординат и прямыми x=2 и x=8.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 3 пример 5 - [ответ]', например 'Задание 3 пример 5 - 78' или 'Задание 3 пример 5 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №3 пример 6
@dp.callback_query_handler(text="t6c3")
async def oge3_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 6 из задания 3:")
    await call.message.answer(
        f"На плане квартиры и садового участка, изображенных на рисунке, известны следующие размеры: AB = 6 м, BC = 4 м, CD = 7 м, DE = 5 м, EF = 8 м, FG = 3 м, GH = 9 м, HI = 7 м, IJ = 6 м, JK = 5 м, KL = 10 м, LM = 7 м. Квартира занимает часть площади ABED, а садовый участок – часть площади CDFG. Найдите отношение площади квартиры к площади садового участка.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 3 пример 6 - [ответ]', например 'Задание 3 пример 6 - 78' или 'Задание 3 пример 6 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №3 пример 7
@dp.callback_query_handler(text="t7c3")
async def oge3_task7(call: types.CallbackQuery):
    await call.message.answer(f"Пример 7 из задания 3:")
    await call.message.answer(
        f"На месте старого автобусного парка планируется построить теплицы площадью 1 гектар. Требуется узнать, какую минимальную длину стороны ограждающего забора нужно приобрести для строительства этих теплиц.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 3 пример 7 - [ответ]', например 'Задание 3 пример 7 - 78' или 'Задание 3 пример 7 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 3 пример 1
@dp.message_handler(text="Задание 3 пример 1 - 0,5")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_3)


# ответ на задание 3 пример 2
@dp.message_handler(text="Задание 3 пример 2 - 5,2")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_3)


# ответ на задание 3 пример 3
@dp.message_handler(text="Задание 3 пример 3 - 0,32")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task4_catalog_3)


# ответ на задание 3 пример 4
@dp.message_handler(text="Задание 3 пример 4 - 2")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task5_catalog_3)


# ответ на задание 3 пример 5
@dp.message_handler(text="Задание 3 пример 5 - 23")
async def answer_task5(message: types.Message):
    await message.answer(f"Верно!\n")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task6_catalog_3)


# ответ на задание 3 пример 6
@dp.message_handler(text="Задание 3 пример 6 - 1,125")
async def answer_task6(message: types.Message):
    await message.answer(f"Верно!\n")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task7_catalog_3)


# ответ на задание 3 пример 7
@dp.message_handler(text="Задание 3 пример 7 - 400")
async def answer_task7(message: types.Message):
    await message.answer(f"Верно!\n")
