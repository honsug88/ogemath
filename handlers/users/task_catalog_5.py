from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_5, task3_catalog_5, task4_catalog_5, task5_catalog_5, task6_catalog_5, \
    task7_catalog_5, task8_catalog_5, task9_catalog_5, task10_catalog_5, task11_catalog_5, task12_catalog_5


# ОГЭ №5 пример 1
@dp.message_handler(text="/task_catalog_5")
async def oge5_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 5:")
    await message.answer(
        f"Вы ищете квартиру для покупки. Вам предлагают два варианта: квартиру площадью 60 квадратных метров по цене 5 миллионов рублей и квартиру площадью 70 квадратных метров по цене 6 миллионов рублей. Для определения более выгодного варианта необходимо узнать стоимость одного квадратного метра жилья в каждом из вариантов. Какой вариант окажется более выгодным, если стоимость одного квадратного метра жилья в первом варианте составляет 100 тысяч рублей, а во втором варианте - 90 тысяч рублей?")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 5 пример 1 - [ответ]', \nнапример, 'Задание 5 пример 1 - 78' или 'Задание 5 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 2
@dp.callback_query_handler(text="t2c5")
async def oge5_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 5:")
    await call.message.answer(
        f"Вы планируете купить сарай для своего садового участка. У вас есть два варианта: первый сарай площадью 20 квадратных метров по цене 90 тысяч рублей и второй сарай площадью 25 квадратных метров по цене 110 тысяч рублей. Какой из вариантов окажется более выгодным, если стоимость одного квадратного метра строительства сарая составляет 4000 рублей?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 2 - [ответ]', например 'Задание 5 пример 2 - 78' или 'Задание 5 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 3
@dp.callback_query_handler(text="t3c5")
async def oge5_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 5:")
    await call.message.answer(
        f"Мужчина планирует совершить путешествие на машине из города A в город B, пройдя через города C и D. На карте расстояния между городами представлены в километрах: A-C: 120 км C-D: 80 км D-B: 150 км. При этом мужчина может выбрать два варианта маршрута:\n\nВариант 1: проехать от города A до города B на прямой, минуя города C и D. Вариант 2: проехать от города A до города B через город C и затем через город D.\nСтоимость топлива для автомобиля мужчины составляет 50 рублей за литр. Расход топлива автомобиля на 100 километров в зависимости от скорости движения представлен в таблице:\nСкорость, км/ч - Расход топлива, л/100 км\n60 - 5\n"
        f"80 - 7\n100 - 9\n\nКакой маршрут следует выбрать мужчине, чтобы затраты на топливо были минимальными?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 3 - [ответ]', например 'Задание 5 пример 3 - 78' или 'Задание 5 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 4
@dp.callback_query_handler(text="t4c5")
async def oge5_task4(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 5:")
    await call.message.answer(
        f"Выпускник занимается производством шин. Для каждого из товаров ему доступны два варианта производства с различными затратами на производство единицы товара. Для производства шин существуют два варианта:\n\nВариант 1 требует затрат 2 тонн резины и 100 рабочих часов на единицу товара.\nВариант 2 требует затрат 3 тонн резины и 80 рабочих часов на единицу товара. Цена продажи одной шины составляет 1500 рублей.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 4 - [ответ]', например 'Задание 5 пример 4 - 78' или 'Задание 5 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 5
@dp.callback_query_handler(text="t5c5")
async def oge5_task5(call: types.CallbackQuery):
    await call.message.answer(f"Пример 5 из задания 5:")
    await call.message.answer(
        f"В супермаркете доступны два варианта упаковок кетчупа: 1) большая упаковка за 200 рублей, содержащая 1 литр продукта; 2) маленькая упаковка за 100 рублей, содержащая 500 миллилитров продукта.\nКакой вариант покупки кетчупа будет оптимальным для покупателя, если стоимость одного литра в большой упаковке равна цене 500 миллилитров в маленькой упаковке?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 5 - [ответ]', например 'Задание 5 пример 5 - 78' или 'Задание 5 пример 5 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 6
@dp.callback_query_handler(text="t6c5")
async def oge5_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 6 из задания 5:")
    await call.message.answer(
        f"В супермаркете доступны три варианта упаковок йогурта: 1) маленькая упаковка за 20 рублей, содержащая 200 миллилитров продукта; 2) средняя упаковка за 50 рублей, содержащая 500 миллилитров продукта; 3) большая упаковка за 90 рублей, содержащая 1 литр продукта. Какой вариант покупки йогурта будет оптимальным для покупателя, если стоимость одного литра в большой упаковке равна цене 500 миллилитров в средней упаковке, а цена 200 миллилитров в маленькой упаковке составляет 25 рублей?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 6 - [ответ]', например 'Задание 5 пример 6 - 78' или 'Задание 5 пример 6 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 7
@dp.callback_query_handler(text="t7c5")
async def oge5_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 7 из задания 5:")
    await call.message.answer(
        f"Для производства мебели доступны четыре варианта дерева: сосна, береза, дуб и ясень. Стоимость единицы:  1) сосны составляет 500 рублей; 2) березы - 800 рублей; 3) дуба - 1200 рублей; 4) ясеня - 1800 рублей. Необходимо изготовить стол, для которого требуется использовать две единицы одного из видов дерева. Стоимость стола будет равна сумме стоимости двух единиц дерева плюс 1000 рублей за работу. Какой вариант дерева наиболее выгоден при условии, что стол будет продаваться за 5000 рублей?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 6 - [ответ]', например 'Задание 5 пример 7 - 78' или 'Задание 5 пример 6 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 8
@dp.callback_query_handler(text="t8c5")
async def oge5_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 8 из задания 5:")
    await call.message.answer(
        f"Вы планируете совершить путешествие на транспорте из города А в город В. Существует два варианта маршрута: первый проходит через города С и Д, а второй - через города Е и Ф. Стоимость билета на каждый участок маршрута указана в таблице:\n\nУчасток маршрута - Цена билета (в рублях)\nА-С: 500\nС-Д: 700\nД-В: 600\nА-Е: 900\nЕ-Ф: 800\nФ-В: 400\n\nКакой из двух вариантов маршрута является более выгодным с точки зрения стоимости проезда?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 8 - [ответ]', например 'Задание 5 пример 8 - 78' или 'Задание 5 пример 8 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 9
@dp.callback_query_handler(text="t9c5")
async def oge5_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 9 из задания 5:")
    await call.message.answer(
        f"В городском поселении 'Зеленый Лес' проводится акция по продаже квартир и садовых участков. Покупателю доступны три варианта покупки: 1) Квартира площадью 90 кв. метров за 4 500 000 рублей. 2) Садовый участок площадью 10 соток за 2 500 000 рублей. 3) Квартира площадью 60 кв. метров + садовый участок площадью 6 соток за 5 000 000 рублей.\nКакой из предложенных вариантов является наиболее выгодным для покупателя?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 9 - [ответ]', например 'Задание 5 пример 9 - 78' или 'Задание 5 пример 9 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 10
@dp.callback_query_handler(text="t10c5")
async def oge5_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 10 из задания 5:")
    await call.message.answer(
        f"Выбирая теплицу для выращивания овощей и фруктов, необходимо учитывать её размеры, материал и стоимость. Даны два варианта теплиц:")
    await call.message.answer_photo(
        photo="https://v1.padlet.pics/1/image.webp?t=c_limit%2Cdpr_1%2Ch_206%2Cw_491&url=https%3A%2F%2Fstorage.googleapis.com%2Fpadlet-uploads%2F1998435003%2Fff2bee620d4e58a8e35c1920dd8f2b25%2F5_10.png%3FExpires%3D1688327153%26GoogleAccessId%3D778043051564-q79bsd8mc40b0bl82ikkrtc3jdofe4dg%2540developer.gserviceaccount.com%26Signature%3DDo1OxfpJ7mr5m7xKmZ23nKWsiZr9LZfVnsA%252BiScgfKkdl3qN%252BcGNME6UyFAkYrgnyZvtwekGx8rqtB6geDPweCgzxZJ5vE%252Fmoq33c0atMqvtK%252B%252FkufAv7R27VtQCRM7g6gkYSL5E5c%252BhhQm6ANnUQc5v0i%252FHrgDhV694QKj9R1w%253D%26original-url%3Dhttps%253A%252F%252Fpadlet-uploads.storage.googleapis.com%252F1998435003%252Fff2bee620d4e58a8e35c1920dd8f2b25%252F5_10.png")
    await call.message.answer(
        f"Определите, какая теплица оптимальнее для выращивания овощей и фруктов с учётом размеров и стоимости.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 10 - [ответ]', например 'Задание 5 пример 10 - 78' или 'Задание 5 пример 10 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 11
@dp.callback_query_handler(text="t11c5")
async def oge5_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 11 из задания 5:")
    await call.message.answer(
        f"При выборе напитка в кафе необходимо учитывать его объём и стоимость. Даны два варианта напитка:")
    await call.message.answer_photo(
        photo="https://v1.padlet.pics/1/image.webp?t=c_limit%2Cdpr_1%2Ch_154%2Cw_472&url=https%3A%2F%2Fstorage.googleapis.com%2Fpadlet-uploads%2F1998435003%2F31c4b5ca41d69623c07667fd43fd4155%2F5_11.png%3FExpires%3D1688327159%26GoogleAccessId%3D778043051564-q79bsd8mc40b0bl82ikkrtc3jdofe4dg%2540developer.gserviceaccount.com%26Signature%3DR0Q2Zxth9MDFx2pYL5n4d6umzss%252Bcw2ZX%252Fumi6wQpm01oWfxAiW6Ey7yS6ZWJexSHs%252FtaqvBfZomWn7cxHQQJTWETkiK%252Bo%252BE%252Fc%252BMWDAMMfdrNBTHLJ%252FT8LfqWD9xMv1%252B2ytWgjMMVuSZO7lDQgg1SW6Lw2fcOuf5jq8aA72Gzfk%253D%26original-url%3Dhttps%253A%252F%252Fpadlet-uploads.storage.googleapis.com%252F1998435003%252F31c4b5ca41d69623c07667fd43fd4155%252F5_11.png")
    await call.message.answer(
        f"Определите, какой вариант напитка оптимальнее для туриста, которому нужно быстро перекусить перед продолжением путешествия при минимальных затратах.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 11 - [ответ]', например 'Задание 5 пример 11 - 78' или 'Задание 5 пример 11 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №5 пример 12
@dp.callback_query_handler(text="t12c5")
async def oge5_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 12 из задания 5:")
    await call.message.answer(
        f"При выборе подарка на день рождения друга необходимо учитывать его интересы, стоимость и практичность. Даны три варианта подарка:")
    await call.message.answer_photo(
        photo="https://v1.padlet.pics/1/image.webp?t=c_limit%2Cdpr_1%2Ch_198%2Cw_635&url=https%3A%2F%2Fstorage.googleapis.com%2Fpadlet-uploads%2F1998435003%2F4131c36de654437c4d79e03fd91caa17%2F5_12.png%3FExpires%3D1688327164%26GoogleAccessId%3D778043051564-q79bsd8mc40b0bl82ikkrtc3jdofe4dg%2540developer.gserviceaccount.com%26Signature%3D0xwXdOzA%252F2%252FifMbtdpeBfN4aKCvhExE%252F%252FsT9CM4uBf2B1mywcxqEIQYJi8o1vj%252Fne97z6Ps9mY8U%252FEl5WmaNbXJ%252ByrmWpdreWFabDAnZTY5gxhlMfEtnsk8ShE0JHK8LjMK7kS47PEH1u9eBZtr4uqZDXHUIar4nn0k%252FVefHjz0%253D%26original-url%3Dhttps%253A%252F%252Fpadlet-uploads.storage.googleapis.com%252F1998435003%252F4131c36de654437c4d79e03fd91caa17%252F5_12.png")
    await call.message.answer(
        f"Определите, какой вариант подарка оптимальнее для друга, который увлекается спортом, но также ценит практичность и интересуется книгами и путешествиями.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 5 пример 12 - [ответ]', например 'Задание 5 пример 12 - 78' или 'Задание 5 пример 12 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 5 пример 1
@dp.message_handler(text="Задание 5 пример 1 - 1")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_5)


# ответ на задание 5 пример 2
@dp.message_handler(text="Задание 5 пример 2 - 1")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_5)


# ответ на задание 5 пример 3
@dp.message_handler(text="Задание 5 пример 3 - 2")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task4_catalog_5)


# ответ на задание 5 пример 4
@dp.message_handler(text="Задание 5 пример 4 - 1")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task5_catalog_5)


# ответ на задание 5 пример 5
@dp.message_handler(text="Задание 5 пример 5 - 1")
async def answer_task5(message: types.Message):
    await message.answer(f"Верно!\n")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task6_catalog_5)


# ответ на задание 5 пример 6
@dp.message_handler(text="Задание 5 пример 6 - 3")
async def answer_task6(message: types.Message):
    await message.answer(f"Верно!\n")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task7_catalog_5)


# ответ на задание 5 пример 7
@dp.message_handler(text="Задание 5 пример 7  - 3")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task8_catalog_5)


# ответ на задание 5 пример 8
@dp.message_handler(text="Задание 5 пример 8 - 1")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task9_catalog_5)


# ответ на задание 5 пример 9
@dp.message_handler(text="Задание 5 пример 9 - 3")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task10_catalog_5)


# ответ на задание 5 пример 10
@dp.message_handler(text="Задание 5 пример 10 - А")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task11_catalog_5)


# ответ на задание 5 пример 11
@dp.message_handler(text="Задание 5 пример 11 - А")
async def answer_task5(message: types.Message):
    await message.answer(f"Верно!\n")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task11_catalog_5)


# ответ на задание 5 пример 12
@dp.message_handler(text="Задание 5 пример 12 - А")
async def answer_task6(message: types.Message):
    await message.answer(f"Верно!\n")
