from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('task_catalog_1', 'Задание 1. Сараи, шины, печки'),
        types.BotCommand('task_catalog_2', 'Задание 2. Простейшие текстовые задачи'),
        types.BotCommand('task_catalog_3', 'Задание 3. Прикладная геометрия: площадь'),
        types.BotCommand('task_catalog_4', 'Задание 4. Прикладная геометрия: расстояния'),
        types.BotCommand('task_catalog_5', 'Задание 5. Выбор оптимального варианта'),
        types.BotCommand('task_catalog_6', 'Задание 6. Числа и вычисления'),
        types.BotCommand('task_catalog_7', 'Задание 7. Числовые неравенства, координатная прямая'),
        types.BotCommand('task_catalog_8', 'Задание 8. Числа, вычисления и алгебраические выражения'),
        types.BotCommand('task_catalog_9', 'Задание 9. Уравнения, системы уравнений'),
        types.BotCommand('task_catalog_10', 'Задание 10. Статистика, вероятности'),
        types.BotCommand('task_catalog_11', 'Задание 11. Графики функций'),
        types.BotCommand('task_catalog_12', 'Задание 12.Расчеты по формулам'),
        types.BotCommand('task_catalog_13', 'Задание 13. Неравенства, системы неравенств'),
        types.BotCommand('task_catalog_14', 'Задание 14. Задачи на прогрессии'),
        types.BotCommand('task_catalog_15', 'Задание 15. Треугольники, четырёхугольники, многоугольники и их элементы'),
        types.BotCommand('task_catalog_16', 'Задание 16. Окружность, круг и их элементы'),
        types.BotCommand('task_catalog_17', 'Задание 17. Площади фигур'),
        types.BotCommand('task_catalog_18', 'Задание 18. Фигуры на квадратной решётке'),
        types.BotCommand('task_catalog_19', 'Задание 19. Анализ геометрических высказываний')
        # types.BotCommand('test_all','Все задания')
    ], scope=types.BotCommandScopeAllPrivateChats())
