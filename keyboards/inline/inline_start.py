from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ib_start = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Информация', callback_data='information'),
                                        # InlineKeyboardButton(text='Сайт', url="")
                                    ],
                                ])
