from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет!"), KeyboardButton(text="Пока!")],
   [KeyboardButton(text="/links")]], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://ria.ru/')],
   [InlineKeyboardButton(text="Музыка", url='https://www.youtube.com/watch?v=8VbvcZfeAWA')],
   [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/watch?v=zkqMK6sDJeY')]
])

inline_keyboard_dynamic = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше!", callback_data='show')]
])

list1 = ["Опция 1", "Опция 2"]
async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in list1:
       keyboard.add(InlineKeyboardButton(text=key, callback_data=key))
   return keyboard.adjust(2).as_markup()