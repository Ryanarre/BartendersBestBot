import sqlite3

class BotManager:
	def ingr_search(self, name):
		all_found = []
		for ingr in self.all_ingredients:
			if name.lower() in ingr.lower():
				all_found.append(ingr)
		return all_found
		
	def get_stage(self):
		return self.stage
		
	def set_stage(self, stage):
		self.stage = stage
		
	def add_ingredient(self, name):
		if name in self.all_ingredients:
			self.ingredients.append(name)
			
			conn_bar = sqlite3.connect("bar.db")
			cursor_bar = conn_bar.cursor()
			try:
				cursor_bar.execute("INSERT INTO ingredients VALUES ('" + name + "')")
				conn_bar.commit()
				cursor_bar.close()
			except:
				print('Что-то пошло не так. Обратись к разработчику или попробуй ещё раз')
			finally:
				if conn_bar:
					conn_bar.close()
		else: 
			print('Что-то пошло не так. Обратись к разработчику или попробуй ещё раз')
		
	def __init__(self):
		conn_bar = sqlite3.connect("bar.db")
		cursor_bar = conn_bar.cursor()
		try:
			cursor_bar.execute("CREATE TABLE ingredients(id integer)")
		except:
			cursor_bar.execute("SELECT * FROM ingredients")
			rows = cursor_bar.fetchall()
			for row in rows:
				self.ingredients.append(row[0])
			cursor_bar.close()
		finally:
			if conn_bar:
				conn_bar.close()
				
		conn_data = sqlite3.connect("data.db")
		cursor_data = conn_data.cursor()
		try:
			cursor_data.execute("SELECT * FROM ingredients")
			rows = cursor_data.fetchall()
			for row in rows:
				self.all_ingredients.append(row[0])
			cursor_data.close()
		except:
			print("Extraction from data.db failed")
		finally:
			if conn_data:
				conn_data.close()
	
	all_ingredients = []
	ingredients = []
	
	stage = 0
	