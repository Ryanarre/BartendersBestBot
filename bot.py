import telebot
import sqlite3
from telebot import types

TOKEN = '1745473892:AAF80DExRgyHzXjA3K0m8D-oorTpo9C3iYA'
ADD_TEXT = 'Добавить ингредиент'
SUGGEST_TEXT = 'Предложить коктейль'

ingredients = []

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_action(message):
	start_menu = types.ReplyKeyboardMarkup(True, True)
	start_menu.row(ADD_TEXT)
	start_menu.row(SUGGEST_TEXT)
	
	bot.send_message(message.chat.id, 'Выбери действие', reply_markup=start_menu)
	
@bot.message_handler(content_types=['text'])
def main_action(message):
	if message.text == ADD_TEXT:
		bot.send_message(message.chat.id, 'Введи название ингредиента или его часть')
	else:
		bot.send_message(message.chat.id, 'Mojito')
		start_action(message)
	
def main():
	conn_bar = sqlite3.connect("bar.db")
	cursor_bar = conn_bar.cursor()
	try:
		cursor_bar.execute("CREATE TABLE ingredients(id integer)")
	except:
		cursor_bar.execute("SELECT * FROM ingredients")
		rows = cursor_bar.fetchall()
		for row in rows:
			ingredients.append(row[0])
		cursor_bar.close()
	finally:
		if conn_bar:
			conn_bar.close()

if __name__ == "__main__":
    main()
	
bot.polling();