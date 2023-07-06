from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_4, task3_catalog_4, task4_catalog_4, task5_catalog_4, task6_catalog_4, task7_catalog_4


# ОГЭ №4 пример 1
@dp.message_handler(text="/task_catalog_4")
async def oge4_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 4:")
    await message.answer(
        f"В новом жилом комплексе есть две квартиры, расположенные на разных этажах. Первая квартира имеет координаты (3, 2), а вторая квартира имеет координаты (7, 5). Найдите расстояние между квартирами, если один блок занимает 50 метров.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 4 пример 1 - [ответ]', \nнапример, 'Задание 4 пример 1 - 78' или 'Задание 4 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №4 пример 2
@dp.callback_query_handler(text="t2c4")
async def oge4_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 4:")
    await call.message.answer(
        f"На плоскости заданы координаты вершин сарая и садового участка в метрах. Найдите расстояние между ними в метрах. Ответ округлите до целого числа. Даны координаты вершин сарая: A(5,10), B(15,20), C(25,10), D(15,0). Даны координаты вершин садового участка: E(30,20), F(40,30), G(50,20), H(40,10).")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 4 пример 2 - [ответ]', например 'Задание 4 пример 2 - 78' или 'Задание 4 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №4 пример 3
@dp.callback_query_handler(text="t3c4")
async def oge4_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 4:")
    await call.message.answer(
        f"Два путника отправились в один день из одного города в другой по одному маршруту, но разными видами транспорта. Первый путник проехал на машине 240 км со скоростью 60 км/ч, а затем продолжил путь пешком со скоростью 6 км/ч и добрался до города за 10 часов. Второй путник прошел пешком на 4 км/ч больше первого путника и добрался до города за 12 часов. Найдите расстояние между городами.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 4 пример 3 - [ответ]', например 'Задание 4 пример 3 - 78' или 'Задание 4 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №4 пример 4
@dp.callback_query_handler(text="t4c4")
async def oge4_task4(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 4:")
    await call.message.answer(
        f"На заводе по производству шин ведутся работы по разработке новой модели шин с повышенной износостойкостью. Для испытаний была изготовлена макетная модель шины размером 120 см × 30 см. Модель должна проехать на специальном стенде расстояние 200 м. При этом скорость в начале движения составляет 10 м/с, а затем она постепенно увеличивается до 20 м/с. В первый момент времени центр модели находится на расстоянии 1 м от старта. На какое расстояние вдоль дорожки будет смещаться центр модели за время ее движения?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 4 пример 4 - [ответ]', например 'Задание 4 пример 4 - 78' или 'Задание 4 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №4 пример 5
@dp.callback_query_handler(text="t5c4")
async def oge4_task5(call: types.CallbackQuery):
    await call.message.answer(f"Пример 5 из задания 4:")
    await call.message.answer(
        f"Саша и Маша отправились в путешествие из Москвы до Петербурга. Саша поехал на автомобиле со скоростью 80 км/ч, а Маша - на поезде со скоростью 120 км/ч. Расстояние между городами составляет 650 км. В каком месте пути перегонятся Саша и Маша?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 4 пример 5 - [ответ]', например 'Задание 4 пример 5 - 78' или 'Задание 4 пример 5 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №4 пример 6
@dp.callback_query_handler(text="t6c4")
async def oge4_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 6 из задания 4:")
    await call.message.answer(
        f"На плоскости даны точки A(2, 7) и B(8, 1). На этой же плоскости расположены квартира и садовый участок. Квартира находится в точке С(5, 4), а садовый участок имеет форму прямоугольника ABCD, где точка D лежит на прямой AB, а точки C и D лежат на одной прямой, перпендикулярной прямой AB. Найдите площадь садового участка ABCD.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 4 пример 6 - [ответ]', например 'Задание 4 пример 6 - 78' или 'Задание 4 пример 6 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №4 пример 7
@dp.callback_query_handler(text="t7c4")
async def oge4_task7(call: types.CallbackQuery):
    await call.message.answer(f"Пример 7 из задания 4:")
    await call.message.answer(
        f"На фермерском хозяйстве есть теплица размером 10 метров на 30 метров. Необходимо провести новый водопровод к теплице из деревни, расположенной в 40 км от неё. Стоимость проведения водопровода через землю составляет 800 рублей за метр, а через воздух - 1200 рублей за метр. Цена одного метра трубы для прокладки воздушного водопровода в десять раз больше цены трубы для прокладки под землей. Какую минимальную сумму придется заплатить за проведение водопровода до теплицы, если трасса прокладки должна следовать по кратчайшему расстоянию?")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 4 пример 7 - [ответ]', например 'Задание 4 пример 7 - 78' или 'Задание 4 пример 7 - Смайл'!",
        disable_web_page_preview=False)


@dp.message_handler(text="Задание 4 пример 1 - 250")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_4)


@dp.message_handler(text="Задание 4 пример  2 - 14")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_4)


@dp.message_handler(text="Задание 4 пример 3 - 276")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task4_catalog_4)


@dp.message_handler(text="Задание 4 пример 4 - 204,2")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task5_catalog_4)


@dp.message_handler(text="Задание 4 пример 5 - 260")
async def answer_task5(message: types.Message):
    await message.answer(f"Верно!\n")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task6_catalog_4)


@dp.message_handler(text="Задание 4 пример 6 - 35,9")
async def answer_task6(message: types.Message):
    await message.answer(f"Верно!\n")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task7_catalog_4)


@dp.message_handler(text="Задание 4 пример 7 - 379")
async def answer_task7(message: types.Message):
    await message.answer(f"Верно!\n")
