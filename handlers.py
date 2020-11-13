from aiogram import types
from connections import *


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # await message.answer(text='Чаты: '
    #                           '\n<a href="https://t.me/dzerzjnskiy_nsk">Дзержинский</a>'
    #                           '\n<a href="https://t.me/zeleznodorojniy_nsk">Железнодорождный</a>'
    #                           '\n<a href="https://t.me/zaelzovskiy_nsk">Заельцовский</a>'
    #                           '\n<a href="https://t.me/kaliniskiy_nsk">Калининский</a>'
    #                           '\n<a href="https://t.me/kirovskiy_nsk">Кировский</a>'
    #                           '\n<a href="https://t.me/leninskiy_nsk">Ленинский</a>'
    #                           '\n<a href="https://t.me/oktabrskiy_nsk">Октябрський</a>'
    #                           '\n<a href="https://t.me/pervomaiskiy_nsk">Первомайский</a>'
    #                           '\n<a href="https://t.me/sovetskiy_nsk">Советский</a>'
    #                           '\n<a href="https://t.me/zentralniy_nsk">Центральный</a>',
    #                      parse_mode='HTML',
    #                      disable_web_page_preview=True)
    await message.answer(text='Чаты: ')
    await message.answer(text='\U000025FD <a href="https://t.me/dzerzjnskiy_nsk">Дзержинский</a>', parse_mode='HTML',disable_web_page_preview=True)
    await message.answer(text='\U000025FE <a href="https://t.me/zeleznodorojniy_nsk">Железнодорожный</a>', parse_mode='HTML',disable_web_page_preview=True)
    await message.answer(text='\U000025FD <a href="https://t.me/zaelzovskiy_nsk">Заельцовский</a>', parse_mode='HTML',disable_web_page_preview=True)
    await message.answer(text='\U000025FE<a href="https://t.me/kaliniskiy_nsk">Калининский</a>', parse_mode='HTML',disable_web_page_preview=True)
    await message.answer(text='\U000025FD <a href="https://t.me/kirovskiy_nsk">Кировский</a>', parse_mode='HTML',disable_web_page_preview=True)
    await message.answer(text='\U000025FE<a href="https://t.me/leninskiy_nsk">Ленинский</a>', parse_mode='HTML',disable_web_page_preview=True)
    await message.answer(text='\U000025FD <a href="https://t.me/oktabrskiy_nsk">Октябрьский</a>', parse_mode='HTML',disable_web_page_preview=True)
    await message.answer(text='\U000025FE<a href="https://t.me/pervomaiskiy_nsk">Первомайский</a>', parse_mode='HTML',disable_web_page_preview=True)
    await message.answer(text='\U000025FD <a href="https://t.me/sovetskiy_nsk">Советский</a>', parse_mode='HTML',disable_web_page_preview=True)
    await message.answer(text='\U000025FE<a href="https://t.me/zentralniy_nsk">Центральный</a>',
                         parse_mode='HTML',
                         disable_web_page_preview=True)
