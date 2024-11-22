import asyncio
from aiogram import Bot, Dispatcher, types
from handlers.private import private_router
from decouple import config
    
async def main():
    bot = Bot(token=config("TOKEN"))
    dp = Dispatcher()
    dp.include_routers(private_router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

asyncio.run(main())