import asyncio
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters.command import Command

bot = Bot('5802885074:AAGjrlErlUgpF57hD8iKQX777PKdpu99e28')
dp = Dispatcher()


@dp.message(F.text, Command("start"))
async def start(message: Message):
    print(message.from_user.id, message.from_user.username)
    kb = [
        [KeyboardButton(text="С пюрешкой", web_app=WebAppInfo(url='https://velobike.ru'))],

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
