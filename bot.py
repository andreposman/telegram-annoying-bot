import os
import re
import telebot
import json
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

bot = telebot.TeleBot(os.environ["API_KEY"])

@bot.message_handler(commands=['startBot', 'helpBot'])
def reply(message):
  print(message)
  if message.from_user.username == 'andreposman':
    bot.reply_to(message, 'Oi Mestre, Avanti Palestra!')

  elif message.from_user.username == 'raafvargas':
    bot.reply_to(message, f'Eai {message.from_user.first_name}, Spec em PHP!')

  elif message.from_user.first_name == 'Matheus':
    bot.reply_to(message, f'Eai {message.from_user.first_name}, Rei do Spring!')

  else:
    bot.reply_to(message, f'Olá {message.from_user.first_name}, Vai Palmeiras!')
  
def extract_arg(arg):
  print(arg.split()[1:])
  return arg.split()[1:]


def findAwfulLang(message):
  result = re.search("(spring|java|jvm|kotlin|php)" , message.text.lower())
  return result.group(0)


def runBot(bot):
  @bot.message_handler(regexp="(spring|java|jvm|kotlin|php)")
  def preach(message):
    print(message)
    lang = findAwfulLang(message).capitalize()
    bot.reply_to(message, f"Oi {message.from_user.first_name}, tudo bem? Identifiquei que você mencionou essa m**** de {lang}. Fui criado para avisar que desenvolver em Go! é melhor.")


  bot.polling()

def main():
    while True:
        try:
            runBot(bot)
        except:
            pass
        else:
            break

if __name__ == "__main__":
  main()