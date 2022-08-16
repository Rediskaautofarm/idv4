import aiogram
import threading
from amino import Client
import json
import os
import asyncio
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, Message
from aiogram.utils import executor
TOKEN_Telegram = "5566712021:AAF8-c_flY-Dx2p8_hwddtYYBG9UQR0z_E8"

class Form(StatesGroup):
  name = State()
  
clieent = Client()
client = Bot(TOKEN_Telegram, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(client, storage=storage)

profile = {
  "links": "none"
}

@dp.message_handler()
async def mess(message: Message):
  ct = message.text.lower()
  content = str(message.text).split(" ")
  user_Id = str(message.from_user.id)
  user_name = message.from_user['username']
  chat_Id = message.chat.id
  reg = os.listdir()
  mes = State()
  if (f"{user_Id}.json") not in reg:
    with open(f"{user_Id}.json", "w") as file:
      json.dump(profile, file)

  if content[0][0] == "/":
    if content[0][1:] == "id":
      await Form.name.set()
      await message.reply("скиньtе ссылку на соо: ")
      
@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_Id = str(message.from_user.id)
        with open(f"{user_Id}.json", "r") as file:
          profile_info = json.load(file)
        data['name'] = message.text
        link = data['name']
        profile_info["links"]=f"{link}"
        comid=profile_info["links"]
        with open(f"{user_Id}.json", "w") as file:
         json.dump(profile_info, file)
        await message.reply(f"{link}")
        id = clieent.get_from_code(comid)
        id = id.json["extensions"]["community"]["ndcId"]
        await message.reply(f"айди соo: {id}")
        
        
if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)