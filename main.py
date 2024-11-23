import os
import logging
import asyncio
from order  import *
from dotenv import load_dotenv
from aiogram import Dispatcher,Bot

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)

async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
