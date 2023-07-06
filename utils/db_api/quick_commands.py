from collections import Counter
from operator import itemgetter

from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(user_id: int, first_name: str, last_name: str, username: str):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()


async def count_refs(user_id):
    refs = await User.query.where(User.referral_id == user_id).gino.all()
    return len(refs)


# Функция для проверки аргументов переданных при регистрации
async def check_args(args, user_id: int):
    # Если в аргумент передана пустая строка
    if args == '':
        args = '0'
        return args
    # Если в аргумент переданы не только числа, а и буквы
    elif not args.isnumeric():
        args = '0'
        return args
    # Если в агрумент переданы ТОЛЬКО числа
    elif args.isnumeric():
        # Если аргумент такой-же как и айди пользователя
        if int(args) == user_id:
            args = '0'
            return args
        # Получаем из базы данных пользователя у которого user_id такой-же как и переданный аргумент
        elif await select_user(user_id=int(args)) is None:
            args = '0'
            return args
        # Если наш аргумент прошёл все проверки, то возвращяем его
        else:
            args = str(args)
            return args
    # Если что-то пошло не так
    else:
        args = '0'
        return args
