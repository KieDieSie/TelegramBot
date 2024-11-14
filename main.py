import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from decouple import config

bot = Bot(token=config("TOKEN"))

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    while True:
        await message.answer('Введіть перший ланцюг ДНК в такому вигляді: ААА-ААА-ААА-ААА-ААА... (якщо не відомо, введіть 0)')
        firstDNK = message.text
        await message.answer('Введіть другий ланцюг ДНК в такому вигляді: ААА-ААА-ААА-ААА-ААА... (якщо не відомо, введіть 0)')
        secondDNK = message.text
        await message.answer('Введіть ланцюг іРНК в такому вигляді: ААА-ААА-ААА-ААА-ААА... (якщо не відомо, введіть 0)')
        rnk = message.text
        await message.answer('Введіть масу гену (якщо не відомо, введіть 0)')
        gen_mass = message.text
        await message.answer('Введіть масу іРНК (якщо не відомо, введіть 0)')
        RNK_mass = message.text
        await message.answer('Введіть довжину гену(ДНК) (якщо не відомо, введіть 0)')
        gen_len = message.text
        await message.answer('Введіть масу білка (якщо не відомо, введіть 0)')
        albumen_mass = message.text
        await message.answer('Введіть кількість амінокислот (якщо не відомо, введіть 0)')
        amino_amount = message.text
        await message.answer('Введіть кількість інторонів(в кінці напишіть % якщо дано у відсодках, якщо дана маса інторонів - напишіть лише число) (якщо не відомо, введіть 0)')
        intorns = message.text
        
        break
    await message.answer(firstDNK)
    await message.answer(secondDNK)
    await message.answer(rnk)
    await message.answer(gen_mass)
    await message.answer(RNK_mass)
    await message.answer(gen_len)
    await message.answer(albumen_mass)
    await message.answer(amino_amount)
    await message.answer(intorns)

# @dp.message()
# async def echo(message: types.Message):
#     msg = message.text
#     if msg == 'abulday':
#         await message.answer('dabulday')
    

async def main():
    await dp.start_polling(bot)
    

asyncio.run(main())