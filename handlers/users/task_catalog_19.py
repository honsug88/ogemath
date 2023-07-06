from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp


# ОГЭ №19 пример 1
@dp.message_handler(text="/task_catalog_19")
async def oge19_task1(message: types.Message):
    await message.answer(f"Пример 1 из задания 19:")
    await message.answer(f"Дан треугольник ABC. На стороне AC выбрана точка D так, что AD = DC. На стороне AB выбрана точка E так, что AE = EB. Докажите, что периметр треугольника ABE равен периметру треугольника BDC.\nВ ответ укажите верный вариант ответа:\n1) Периметры треугольников ABE и BDC равны.\n2) Площади треугольников ABE и BDC равны.\n"
                         f"3) Один из углов треугольника ABE прямой, поэтому периметр этого треугольника больше периметра треугольника BDC.\n4) Нельзя доказать, что периметры треугольников ABE и BDC равны, так как не дана достаточная информация о длинах сторон треугольника ABC.")
    await message.answer(
        f"Напиши ответ и отправь его мне в формате: 'Задание 19 пример 1 - [ответ]', например, 'Задание 19 пример 1 - 78' или 'Задание 19 пример 1 - Смайл'!",
        disable_web_page_preview=False)


# ответ на задание 19 пример 1
@dp.message_handler(text="Задание 19 пример 1 - 1")
async def answer_task1(message: types.Message):
    await message.answer(f"Верно!")
