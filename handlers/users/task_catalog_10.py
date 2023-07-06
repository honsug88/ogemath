from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp
from keyboards.inline import task2_catalog_10


# ОГЭ №10 пример 1
@dp.message_handler(text="/task_catalog_10")
async def oge10_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 10:")
    await message.answer(f"Выбирают наугад букву из слова 'ВЕРОЯТНОСТЬ'. Какова вероятность того, что выбранная буква будет гласной?")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: \n'Задание 10 пример 1 - [ответ]', \nнапример, 'Задание 10 пример 1 - 78' или 'Задание 10 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ОГЭ №10 пример 2
@dp.callback_query_handler(text="t2c10")
async def oge10_task2(call: types.CallbackQuery):
    await call.message.answer(f"Пример 2 из задания 10:")
    await call.message.answer(f"В коробке лежат 7 белых и 5 черных шаров. Из этой коробки наудачу вынимают 2 шара. Найдите вероятность того, что эти шары будут разного цвета.\nОтвет должен округлен до двух знаков после запятой.")
    await call.message.answer(
        f"Напиши ответ и отправь его мне в формате 'Задание 10 пример 2 - [ответ]', например 'Задание 10 пример 2 - 78' или 'Задание 10 пример 2 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 10 пример 1
@dp.message_handler(text="Задание 10 пример 1 - 0,5")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
    await message.answer(f"Можешь приступить к следующему примеру.",
                         reply_markup=task2_catalog_10)


# ответ на задание 10 пример 2
@dp.message_handler(text="Задание 10 пример 2 - 1,06")
async def answer_task2(message: types.Message):
    await message.answer(f"Верно!")
