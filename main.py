import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random
import requests

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_weather(city):
    api_key = "bca1c0489a6a8bebf9a512c7411aa5c7"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()


@dp.message(Command('weather'))
async def weather(message: Message):
    await message.answer("Введите название города:")

    # Ожидаем следующего сообщения от пользователя
    @dp.message()
    async def get_city(city_message: Message):
        city_name = city_message.text
        weather_data = get_weather(city_name)

        if weather_data.get("cod") != 200:
            await message.answer("Не удалось получить данные о погоде. Проверьте правильность написания города.")
            return

        # Извлечение информации о погоде
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        weather_info = (f"Погода в городе {city_name}:\n"
                        f"Температура: {temperature}°C\n"
                        f"Описание: {weather_description}\n"
                        f"Влажность: {humidity}%\n"
                        f"Скорость ветра: {wind_speed} м/с")

        await message.answer(weather_info)

        # Удаляем обработчик, чтобы он не срабатывал на следующие сообщения
        dp.message.handlers.pop()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!")

@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, '
                         'которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://sotni.ru/wp-content/uploads/2023/08/korotko-o-pogode-4.webp',
            'https://sotni.ru/wp-content/uploads/2023/08/anekdoty-pro-kholodnoe-leto-3.webp',
            'https://sotni.ru/wp-content/uploads/2023/08/dozhd-karikatura-4.webp']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
