from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_6, task3_catalog_6, task4_catalog_6


# ОГЭ №6 пример 1
@dp.message_handler(text="/task_catalog_6")
async def oge6_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 6:")
    await message.answer(f"Дана обыкновенная дробь 7/9. Выполните следующие действия:\n\n1) Умножьте эту дробь на 2.\n2) Разделите полученный результат на 3.\n3) Вычтите из результата число 1.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 6 пример 1 - [ответ]', \nнапример, 'Задание 6 пример 1 - 78' или 'Задание 6 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №6 пример 2
@dp.callback_query_handler(text="t2c6")
async def oge6_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 6:")
    await call.message.answer(f"Найдите значение выражения:")
    await call.message.answer_photo(
        photo="https://v1.padlet.pics/1/image.webp?t=c_limit%2Cdpr_1%2Ch_65%2Cw_143&url=https%3A%2F%2Fstorage.googleapis.com%2Fpadlet-uploads%2F1998435003%2F73d731fb6f54c356343ea24ba397db1c%2F6_2.png%3FExpires%3D1688327187%26GoogleAccessId%3D778043051564-q79bsd8mc40b0bl82ikkrtc3jdofe4dg%2540developer.gserviceaccount.com%26Signature%3D4MPuutpySVT%252FR8%252FLyzgbkGKd0mX%252B51Ajz7mIcChd6dH0FqDHHAutJmcGEVzRNcROqw%252BF0sR1myUgXfDnVOYc2YImbvJSAjJOwzeNGVCZiMcr5azWm%252F4INZSmhLrW6nMJk1RO%252BebPJ24pKjseGBCAWx%252BPtNjftO%252FaYHC507tB8oY%253D%26original-url%3Dhttps%253A%252F%252Fpadlet-uploads.storage.googleapis.com%252F1998435003%252F73d731fb6f54c356343ea24ba397db1c%252F6_2.png")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 6 пример 2 - [ответ]', например 'Задание 6 пример 2 - 78' или 'Задание 6 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №6 пример 3
@dp.callback_query_handler(text="t3c6")
async def oge6_task3(call: types.CallbackQuery):
    await call.message.answer(f"Пример 3 из задания 6:")
    await call.message.answer(f"Выполните умножение:")
    await call.message.answer_photo(
        photo="https://v1.padlet.pics/1/image.webp?t=c_limit%2Cdpr_1%2Ch_58%2Cw_157&url=https%3A%2F%2Fstorage.googleapis.com%2Fpadlet-uploads%2F1998435003%2F620f705ec2c64e35acba79c4e4f30971%2F6_3.png%3FExpires%3D1688327195%26GoogleAccessId%3D778043051564-q79bsd8mc40b0bl82ikkrtc3jdofe4dg%2540developer.gserviceaccount.com%26Signature%3DZlImFgOLKv6AvplTpW0FIFFwfOqJyvHSFb3%252FAHzyzNytVWm%252B4Bi7CWTbIvQKRef2jHhtkl7QfSfalhzZpv9fT5cSAcOqRGhz7qsHR%252BMVPVDaJQx0Qx9BDMS8vmTt0LcO6Y1HtMcgxCOVt71mJ94nh%252FhEROZSP3dyyd8Df5aCs3E%253D%26original-url%3Dhttps%253A%252F%252Fpadlet-uploads.storage.googleapis.com%252F1998435003%252F620f705ec2c64e35acba79c4e4f30971%252F6_3.png")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 6 пример 3 - [ответ]', например 'Задание 6 пример 3 - 78' или 'Задание 6 пример 3 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №6 пример 1
@dp.callback_query_handler(text="t4c6")
async def oge6_task4(call: types.CallbackQuery):
    await call.message.answer(f"Пример 4 из задания 6:")
    await call.message.answer(f"Найдите значение выражения:")
    await call.message.answer_photo(
        photo="https://v1.padlet.pics/1/image.webp?t=c_limit%2Cdpr_1%2Ch_40%2Cw_337&url=https%3A%2F%2Fstorage.googleapis.com%2Fpadlet-uploads%2F1998435003%2F28aa74d39e888c8d425e907e86748b72%2F6_4.png%3FExpires%3D1688327204%26GoogleAccessId%3D778043051564-q79bsd8mc40b0bl82ikkrtc3jdofe4dg%2540developer.gserviceaccount.com%26Signature%3DZLofsA2juYmb4TuwHWFqVXcPBBUPnIFw6eYsJ5fz4urSeohs6JQUw0VcM9sFHXmaogQ%252Fw1ibZuaNu3GaSLABR4tSGyOEDPWbYr0S4Xk4P0VYVjoWzUb0%252F3undGLb9yZrCJhcD3IMJZQ6QH0VYMclxfx7DaRay6irm%252F5XQRfVvGc%253D%26original-url%3Dhttps%253A%252F%252Fpadlet-uploads.storage.googleapis.com%252F1998435003%252F28aa74d39e888c8d425e907e86748b72%252F6_4.png")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 6 пример 4 - [ответ]', например 'Задание 6 пример 4 - 78' или 'Задание 6 пример 4 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 6 пример 1
@dp.message_handler(text="Задание 6 пример 1 - -0,48")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_6)


# ответ на задание 6 пример 2
@dp.message_handler(text="Задание 6 пример 2 - 37")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task3_catalog_6)


# ответ на задание 6 пример 3
@dp.message_handler(text="Задание 6 пример 3  -8,4375")
async def answer_task3(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task4_catalog_6)


# ответ на задание 6 пример 4
@dp.message_handler(text="Задание 6 пример 4  - 90400")
async def answer_task4(message: types.Message):
    await message.answer(f"Верно!")
