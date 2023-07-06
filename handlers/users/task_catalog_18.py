from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_18, task3_catalog_18, task4_catalog_18, task5_catalog_18, task6_catalog_18, \
    task7_catalog_18, task8_catalog_18


# ОГЭ №18 пример 1
@dp.message_handler(text="/task_catalog_18")
async def oge18_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 18:")
    await message.answer(
        f"На квадратной клетчатой бумаге размером 6х6 нарисован прямоугольник ABCD. Найдите угол между диагоналями прямоугольника, если вершины A, B, C и D лежат в точках с координатами (1,1), (5,1), (5,4) и (1,4) соответственно.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: 'Задание 18 пример 1 - [ответ]', например, 'Задание 18 пример 1 - 78' или 'Задание 18 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №18 пример 2
@dp.callback_query_handler(text="t2c18")
async def oge18_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 18:")
    await call.message.answer(
        f"На квадратной клетчатой бумаге нарисована прямая AB, проходящая через точки с координатами A(2,3) и B(7,8). Найдите расстояние от точки С(4,1) до прямой AB. Ответ округлите до сотых.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 18 пример 2 - [ответ]', например 'Задание 18 пример 2 - 78' или 'Задание 18 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №18 пример 3
@dp.callback_query_handler(text="t3c18")
async def oge18_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 18:")
    await call.message.answer(
        f"На квадратной клетчатой бумаге нарисован треугольник ABC с вершинами A(1,4), B(4,2) и C(6,7). Найдите длину высоты, проведенных из вершины C. Ответ округлите до сотых.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 18 пример 3 - [ответ]', например 'Задание 18 пример 3 - 78' или 'Задание 18 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №18 пример 4
@dp.callback_query_handler(text="t4c18")
async def oge18_task4(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 18:")
    await call.message.answer(
        f"На квадратной клетчатой бумаге нарисован прямоугольный треугольник ABC, прямой угол которого расположен в вершине С. Вершины A и B этого треугольника лежат на сторонах с координатами x=1 и y=6. Найдите площадь треугольника.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 18 пример 4 - [ответ]', например 'Задание 18 пример 4 - 78' или 'Задание 18 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №18 пример 5
@dp.callback_query_handler(text="t5c18")
async def oge18_task5(call: types.CallbackQuery):
    await call.message.answer(f"Пример 5 из задания 18:")
    await call.message.answer(
        f"На квадратной клетчатой бумаге нарисован параллелограмм ABCD с вершинами A(1,2), B(5,6), C(4,9) и D(0,5). Найдите площадь этого параллелограмма.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 18 пример 5 - [ответ]', например 'Задание 18 пример 5 - 78' или 'Задание 18 пример 5 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №18 пример 6
@dp.callback_query_handler(text="t6c18")
async def oge18_task6(call: types.CallbackQuery):
    await call.message.answer(f"Пример 6 из задания 18:")
    await call.message.answer(
        f"На квадратной клетчатой бумаге нарисован ромб ABCD с вершинами A(2,5), B(6,9), C(10,5) и D(6,1). Найдите периметр этого ромба. Ответ округлите до сотых.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 18 пример 6 - [ответ]', например 'Задание 18 пример 6 - 78' или 'Задание 18 пример 6 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №18 пример 7
@dp.callback_query_handler(text="t7c18")
async def oge18_task7(call: types.CallbackQuery):
    await call.message.answer(f"Пример 7 из задания 18:")
    await call.message.answer(
        f"На квадратной решетке отмечены точки A(2;3), B(6;5), C(8;1) и D(4;-1). Постройте на координатной плоскости фигуру ABCD и найдите её периметр. Известно, что стороны AB и CD параллельны оси абсцисс, а стороны BC и AD — оси ординат.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 18 пример 7 - [ответ]', например 'Задание 18 пример 7 - 78' или 'Задание 18 пример 7 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №18 пример 8
@dp.callback_query_handler(text="t8c18")
async def oge18_task8(call: types.CallbackQuery):
    await call.message.answer(f"Пример 8 из задания 18:")
    await call.message.answer(
        f"На квадратной решетке отмечены точки A(1;2), B(4;5), C(7;2) и D(4;-1). Постройте на координатной плоскости многоугольник ABCD. Вычислите его периметр и площадь.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 18 пример 8 - [ответ]', например 'Задание 18 пример 8 - 78' или 'Задание 18 пример 8 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 18 пример 1
@dp.message_handler(text="Задание 18 пример 1 - 131,8")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_18)


# ответ на задание 18 пример 2
@dp.message_handler(text="Задание 18 пример 2 - 2,83")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_18)


# ответ на задание 18 пример 3
@dp.message_handler(text="Задание 18 пример 3 - 1,09")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_18)


# ответ на задание 18 пример 4
@dp.message_handler(text="Задание 18 пример 4 - 3")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task5_catalog_18)


# ответ на задание 18 пример 5
@dp.message_handler(text="Задание 18 пример 5 - 16")
async def answer_task5(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task6_catalog_18)


# ответ на задание 18 пример 6
@dp.message_handler(text="Задание 18 пример 6 - 18,06")
async def answer_task6(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task7_catalog_18)


# ответ на задание 18 пример 7
@dp.message_handler(text="Задание 18 пример 7 - 12")
async def answer_task7(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task8_catalog_18)


# ответ на задание 18 пример 8
@dp.message_handler(text="Задание 18 пример 8 - 9")
async def answer_task8(message: types.Message):
    await message.answer(f"Верно!")
