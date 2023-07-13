from aiogram import Bot, Dispatcher, executor, types, filters
from google_sheets_util.sheets import pygsheetsExt as sheet
bot = Bot("6064349247:AAG9ADR9dKiai4uIcknZhrPuY1PjqxWlUHQ")
dp = Dispatcher(bot)

if bot.set_chat_menu_button('hello'):
    print('changed')

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Привет, кабанам. Пиши /anek чтобы получить свой прикол")
    
@dp.message_handler(commands=['anekdot'])
async def solo_anek(message: types.Message):
    await message.reply(sheet.getData("Анекдоты категории Б"))

@dp.channel_post_handler(filters.Command(commands=['anekdot']))
async def group_anek(message: types.Message):
    await message.reply(sheet.getData("Анекдоты категории Б"))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)