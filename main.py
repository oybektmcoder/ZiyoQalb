from Checker import sura,oyat
from Name import reply_name
from Requsets import reply_answer

import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN="Ziyo Qalb"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Ассалому Алайкум!Илм улашиш учун Бот!\nШайх Муҳамадсодиқ Муҳамад Юсуф таржималаридан.\nСиздан дастуримизга 1:4 {1-сура 4-оят} каби киритишингизни сораб қоламиз.\nКаманда ҳақида:/Gorizont")


@dp.message_handler(commands=['Gorizont'])
async def send_welcome(message: types.Message):
    await message.reply("Дастуримизга Хуш келибсиз.\nБу дастур Горизонт жамоаси томонидан тузилган.\nКонтакт учун: https://t.me/GorizontTeamCreater.\nҚўшимча лойиҳалар:https://t.me/gorizont_portfolio")



@dp.message_handler()
async def Sura(message: types.Message):
    mg=message.text
    s=sura(mg)
    o=oyat(mg)
    try:
        an=reply_name(s)
        ans=reply_answer(s,o)
    except:
        ans='Бундай оят ёки сура мавжуд емас.Агар таклиф ва шикоятлар бўлса @GorizontTeamCreater\n'
        ans+='Эслатиб ўтамиз\n'
        ans+='Илтимос 1:1 шаклида матн киритинг.\n'
    await message.reply(an)
    await message.reply(ans)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
