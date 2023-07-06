from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.types import Message
from loader import dp
from keyboards.inline import ib_start

from aiogram.dispatcher.filters import CommandStart
from utils.db_api import quick_commands as commands


@dp.message_handler(text='/start')
async def command_start(message: Message):
    await message.answer(f'Ты можешь узнать информацию об экзамене:',
                         reply_markup=ib_start)
    await message.answer(f'Чтобы начать выполнять задания, нажми на "Меню".')
    await message.delete()


@dp.callback_query_handler(text="information")
async def send(call: CallbackQuery):
    await call.message.answer(
        f"Экзамен состоит из двух разделов: задания с коротким и развернутым ответами.\n\nЧасть 1: Задания с коротким ответом\n     Задачи 1-5: Реальная математика, требует нахождения конечных ответов на основе данных в длинном тексте. Проверяет навыки применения математических знаний в реальной жизни.\n     Задачи 6-15: Алгебра.\n     Задачи 16-20: Геометрия, фокусирующаяся на плоских геометрических фигурах.\n\nЧасть 2: Задания с развернутым ответом\n     Задачи 21-23: Сложные задачи по алгебре.\n     Задачи 24-26: Сложные задачи по геометрии.\n\nВ части 2 проверяющий эксперт будет внимательно анализировать каждую деталь вашего решения, которое необходимо подробно расписать на бланках.")
