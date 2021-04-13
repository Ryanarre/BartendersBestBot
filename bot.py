from bot_manager import BotManager
import telebot
from telebot import types

TOKEN = '1745473892:AAF80DExRgyHzXjA3K0m8D-oorTpo9C3iYA'
ADD_TEXT = 'Добавить ингредиент'
SUGGEST_TEXT = 'Предложить коктейль'

bot = telebot.TeleBot(TOKEN)
bot_manager = BotManager()

@bot.message_handler(commands=['start'])
def start_action(message):
	start_menu = types.ReplyKeyboardMarkup(True, True)
	start_menu.row(ADD_TEXT)
	start_menu.row(SUGGEST_TEXT)
	
	bot.send_message(message.chat.id, 'Выбери действие', reply_markup=start_menu)
	
@bot.message_handler(content_types=['text'])
def main_action(message):
	stage = bot_manager.get_stage()
	if stage == 0:
		if message.text == ADD_TEXT:
			bot_manager.set_stage(1)
			bot.send_message(message.chat.id, 'Введи название ингредиента или его часть')
		elif message.text == SUGGEST_TEXT:
			bot.send_message(message.chat.id, 'Mojito')
		else:
			bot.send_message(message.chat.id, 'Прости, но я не понимаю твою комманду :(')
	elif stage == 1:
		suggestion_menu = types.ReplyKeyboardMarkup(True, True)
		for ingr in bot_manager.ingr_search(message.text):
			suggestion_menu.row(ingr)
			
		bot_manager.set_stage(2)
		bot.send_message(message.chat.id, 'Выбери один из вариантов', reply_markup=suggestion_menu)
	elif stage == 2:
		bot_manager.add_ingredient(message.text)
		bot_manager.set_stage(0)
		start_action(message)

bot.polling();