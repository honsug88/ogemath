from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_1, task3_catalog_1, task4_catalog_1, task5_catalog_1, task6_catalog_1, \
    task7_catalog_1


# ОГЭ №1 Пример 1
@dp.message_handler(text="/task_catalog_1")
async def oge1_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 1:")
    await message.answer(
        f"В новом доме построили два корпуса с квартирами. В первом корпусе 5 подъездов, в каждом подъезде 10 этажей, на каждом этаже по 8 квартир. Во втором корпусе 3 подъезда, в каждом подъезде 15 этажей, на каждом этаже по 12 квартир. Сколько всего квартир в новом доме?")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 1 пример 1 - [ответ]', \nнапример, 'Задание 1 пример 1 - 78' или 'Задание 1 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №1 Пример 2
@dp.callback_query_handler(text="t2c1")
async def oge1_task2(call: CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 1:")
    await call.message.answer(
        f"На садовом участке площадью 25 соток необходимо построить сарай. Сарай должен иметь форму прямоугольника со сторонами a и b (в метрах) и занимать не более 20% площади садового участка. Какие максимальные значения могут быть у длин сторон a и b?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 1 пример 2 - [ответ]', \nнапример, 'Задание 1 пример 2 - 78' или 'Задание 1 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №1 Пример 3
@dp.callback_query_handler(text="t3c1")
async def oge1_task3(call: CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 1:")
    await call.message.answer(
        f"Для станций, указанных в таблице, определите, какими цифрами они обозначены на схеме. Заполните таблицу, в ответ запишите последовательность четырёх цифр.")
    await call.message.answer_photo(
        photo="https://v1.padlet.pics/1/image.webp?t=c_limit%2Cdpr_1%2Ch_684%2Cw_858&url=https%3A%2F%2Fstorage.googleapis.com%2Fpadlet-uploads%2F1998435003%2Fa06363397e7d6b0948752abd74d43283%2F13.png%3FExpires%3D1688294934%26GoogleAccessId%3D778043051564-q79bsd8mc40b0bl82ikkrtc3jdofe4dg%2540developer.gserviceaccount.com%26Signature%3Dn4drDwc%252BMvcvnXDF%252FZNXPVBseVQQN3Y%252F21CB7UHKqz%252F55NR8QhInSvozBQq85gdtGb0YscoW1rRQPt9VClqRfNO6bG5c54ucILg8%252FVqijHqToThuTBZcU9bqlqRrZGlsOPiArEY0cDx0FMZy%252Bj7JWciXBZFDk55mib%252BTShvXZAo%253D%26original-url%3Dhttps%253A%252F%252Fpadlet-uploads.storage.googleapis.com%252F1998435003%252Fa06363397e7d6b0948752abd74d43283%252F13.png")
    await call.message.answer(
        f"На рисунке изображена схема метро города N. Станция Кировская Синей ветки расположена между станциями Яблочная и Заводская. Если ехать по кольцевой линии (она имеет форму окружности), то можно последовательно попасть на станции Яблочная, Восточная, Летняя, Площадь победы, Морская. Красная ветка включает в себя станции Балтийская, Банковская, Морская, Восточная и Нарвская.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 1 пример 3 - [ответ]', \nнапример, 'Задание 1 пример 3 - 78' или 'Задание 1 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №1 Пример 4
@dp.callback_query_handler(text="t4c1")
async def oge1_task4(call: CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 1:")
    await call.message.answer(
        f"На фабрике бумажные изделия производятся на двух станках: первый станок работает 6 часов в день, а второй - 8 часов в день. Одинаковое количество изделий производится на каждом станке за час, а все изделия имеют одинаковый размер. За 12 рабочих дней произведено 7200 изделий. Сколько изделий производится за час на одном станке?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 1 пример 4 - [ответ]', \nнапример, 'Задание 1 пример 4 - 78' или 'Задание 1 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №1 Пример 5
@dp.callback_query_handler(text="t5c1")
async def oge1_task5(call: CallbackQuery):
    await call.message.answer(f"Пример 5 из задания 1:")
    await call.message.answer(
        f"Пользуясь описанием, определите, какими цифрами на плане обозначены деревни. В ответ запишите последовательность четырёх цифр без пробелов, запятых и других дополнительных символов.")
    await call.message.answer_photo(
        photo="https://v1.padlet.pics/1/image.webp?t=c_limit%2Cdpr_1%2Ch_165%2Cw_890&url=https%3A%2F%2Fstorage.googleapis.com%2Fpadlet-uploads%2F1998435003%2F130a66191071daba701d2bfd462784b3%2F1_15.png%3FExpires%3D1688294952%26GoogleAccessId%3D778043051564-q79bsd8mc40b0bl82ikkrtc3jdofe4dg%2540developer.gserviceaccount.com%26Signature%3Dv%252FC2YdahbrJCqRnKBSSPfH6F%252Bn9fSHmdmv1PZ1lKs1j0W6X8ieiDw7uwM6LVddT92wgpERSrdYCxFny91b4kiK1anNRCKWQeMjXvlTRQMDeLUjDMSu%252B%252FqNMnbwytVdSBGdVeMXVtOusOZkrsHnr6Q34Jq7nL2uqaun4tA0iNIc0%253D%26original-url%3Dhttps%253A%252F%252Fpadlet-uploads.storage.googleapis.com%252F1998435003%252F130a66191071daba701d2bfd462784b3%252F1_15.png")
    await call.message.answer(
        f"На рисунке изображён план сельской местности. Таня на летних каникулах приезжает в гости к дедушке в деревню Антоновка (на плане обозначена цифрой 1). В конце каникул дедушка на машине собирается отвезти Таню на автобусную станцию, которая находится в деревне Богданово. Из Антоновки в Богданово можно проехать по просёлочной дороге мимо реки. Есть другой путь — по шоссе до деревни Ванютино, где нужно повернуть под прямым углом налево на другое шоссе, ведущее в Богданово. Третий маршрут проходит по просёлочной дороге мимо пруда до деревни Горюново, где можно свернуть на шоссе до Богданово. Четвёртый маршрут пролегает по шоссе до деревни Доломино, от Доломино до Горюново по просёлочной дороге мимо конюшни и от Горюново до Богданово по шоссе. Ещё один маршрут проходит по шоссе до деревни Егорка, по просёлочной дороге мимо конюшни от Егорки до Жилино и по шоссе от Жилино до Богданово. Шоссе и просёлочные дороги образуют прямоугольные треугольники.")
    await call.message.answer_photo(
        photo="https://v1.padlet.pics/1/image.webp?t=c_limit%2Cdpr_1%2Ch_740%2Cw_1005&url=https%3A%2F%2Fstorage.googleapis.com%2Fpadlet-uploads%2F1998435003%2F9d4f47a70647dc7cefca1339902a3e1b%2F2_15.png%3FExpires%3D1688294961%26GoogleAccessId%3D778043051564-q79bsd8mc40b0bl82ikkrtc3jdofe4dg%2540developer.gserviceaccount.com%26Signature%3Dwfa6%252BuDzb7lFA6QEpvGw4BqZQwiwh4tMvSwq8H6EUB4gRdS%252FLq%252FneK0GWkQJ8vwnfCWudACAvmzh7Kg2R18WyIHUOFR9asAoaua6hufRBOf3arJLl7Of8nhBUe8UTSuMZXQSolQxSPRS1zQe0cZGrnHxw1buWoFu9cVaCkSoy0Y%253D%26original-url%3Dhttps%253A%252F%252Fpadlet-uploads.storage.googleapis.com%252F1998435003%252F9d4f47a70647dc7cefca1339902a3e1b%252F2_15.png")
    await call.message.answer(
        f"По шоссе Таня с дедушкой едут со скоростью 50 км/ч, а по просёлочным дорогам — со скоростью 30 км/ч. Расстояние от Антоновки до Доломино равно 12 км, от Доломино до Егорки — 4 км, от Егорки до Ванютино — 12 км, от Горюново до Ванютино — 15 км, от Ванютино до Жилино — 9 км, а от Жилино до Богданово — 12 км.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 1 пример 5 - [ответ]', \nнапример, 'Задание 1 пример 5 - 78' или 'Задание 1 пример 5 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №1 Пример 6
@dp.callback_query_handler(text="t6c1")
async def oge1_task6(call: CallbackQuery):
    await call.message.answer(f"Пример 6 из задания 1:")
    await call.message.answer(
        f"В жилом доме 9 этажей, на каждом этаже - по 4 квартиры. Каково минимальное число подъездов в доме, если в каждом подъезде должно быть не менее 14 квартир?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 1 пример 6 - [ответ]', \nнапример, 'Задание 1 пример 6 - 78' или 'Задание 1 пример 6 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №1 Пример 7
@dp.callback_query_handler(text="t7c1")
async def oge1_task7(call: CallbackQuery):
    await call.message.answer(f"Пример 7 из задания 1:")
    await call.message.answer(
        f"На производственном участке стоит 12 сараев, каждый из которых занимает 225 квадратных метров. Для перевозки материалов на участок использовались шины, каждая из которых имеет диаметр 80 сантиметров и может пройти расстояние 13 километров до следующей замены. Какое минимальное число шин необходимо для того, чтобы обеспечить доставку материалов на участок в течение месяца, если каждый сарай требует ежедневно доставки материалов массой 1 тонна?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 1 пример 7 - [ответ]', \nнапример, 'Задание 1 пример 7 - 78' или 'Задание 1 пример 7 - Смайл'!",
        disable_web_page_preview=False)


# ответ задание 1 пример 1
@dp.message_handler(text="Задание 1 пример 1  - 980")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_1)


# ответ задание 1 пример 2
@dp.message_handler(text="Задание 1 пример 2 - 15,81")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_1)


# ответ задание 1 пример 3
@dp.message_handler(text="Задание 1 пример 3 - 3251")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task4_catalog_1)


# ответ задание 1 пример 4
@dp.message_handler(text="Задание 1 пример 4 - 514")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task5_catalog_1)


# ответ задание 1 пример 5
@dp.message_handler(text="Задание 1 пример 5 - 4625")
async def answer_task5(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task6_catalog_1)


# ответ задание 1 пример 6
@dp.message_handler(text="Задание 1 пример 6 - 1")
async def answer_task6(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task7_catalog_1)


# ответ задание 1 пример 7
@dp.message_handler(text="Задание 1 пример 7 - 13846")
async def answer_task7(message: types.Message):
    await message.answer(f"Верно!")
