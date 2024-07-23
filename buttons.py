import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN

import sqlite3
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import aiohttp

import keyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer('Выбери и нажми на кнопку!', reply_markup=kb.main)

@dp.message(F.text == "Привет!")
async def test_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == "Пока!")
async def test_button(message: Message):
   await message.answer(f'Пока, {message.from_user.first_name}!')

@dp.message(Command('links'))
async def start(message: Message):
   await message.answer('Выбери контент:', reply_markup=kb.inline_keyboard_test)

@dp.message(Command('dynamic'))
async def start(message: Message):
   await message.answer('Выбери опцию:', reply_markup=kb.inline_keyboard_dynamic)

@dp.callback_query(F.data == 'show')
async def show(callback: CallbackQuery):
   await callback.answer("Список опций")
   await callback.message.edit_text('Список опций', reply_markup=await kb.test_keyboard())

@dp.callback_query(lambda c: True)
async def process_callback(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)  # Подтверждаем нажатие кнопки
    await bot.send_message(callback_query.from_user.id, f"Вы нажали: {callback_query.data}")  # Отправляем текст

async def main():
   await dp.start_polling(bot)


if __name__ == "__main__":
   asyncio.run(main())