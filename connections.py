import logging
import tracemalloc

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


tracemalloc.start()
API_TOKEN = '1349211620:AAGx1YxDHvNL7Sbg8D8PkinVZso1sfP4Hb0'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())
