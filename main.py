import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.environ['BOT_TOKEN']

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
menu.add("Свет есть ✅", "Свет пропал 🛑", "Статус смены")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Привет, Виктор! ⚡️\nЯ теперь живу в облаке и никогда не выключаюсь!\nСвет на станции есть?",
        reply_markup=menu
    )

@dp.message_handler(lambda m: "есть" in m.text.lower() or m.text == "Свет есть ✅")
async def on(message: types.Message):
    await message.answer("✅ Свет есть! Молодец, держишь станцию на плаву!")

@dp.message_handler(lambda m: "пропал" in m.text.lower() or m.text == "Свет пропал 🛑")
async def off(message: types.Message):
    await message.answer("🛑 СВЕТ ПРОПАЛ!\nБеги чинить, я с тобой!")

@dp.message_handler(lambda m: m.text == "Статус смены")
async def status(message: types.Message):
    await message.answer("Ты — начальник смены. Всё под контролем? 😏")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Записал: {message.text}")

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
