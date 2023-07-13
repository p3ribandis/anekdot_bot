from aiogram import Bot, Dispatcher, executor, types

bot = Bot("6064349247:AAG9ADR9dKiai4uIcknZhrPuY1PjqxWlUHQ")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Привет, кабанам. Пиши /anek чтобы получить свой прикол")
    
@dp.message_handler(commands=['anek'])
async def welcome(message: types.Message):
    await message.reply("Привет, кабанам. Пиши /anek чтобы получить свой прикол")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)