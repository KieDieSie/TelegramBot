import asyncio
from aiogram import Bot, Dispatcher, types
from handlers.private import private_router
from options.options import private
from decouple import config
    
async def main():
    bot = Bot(token=config("TOKEN"))
    dp = Dispatcher()
    dp.include_routers(private_router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)
    

asyncio.run(main())