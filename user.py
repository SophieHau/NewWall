import sqlite3

class User():
	def __init__(self):
		self.connection = sqlite3.connect('thenewwall.db')
		self.cursor = self.connection.cursor()

	def add_user(self, username, password):
		query = "INSERT INTO users (username, password) VALUES (?, ?)"
		self.cursor.execute(query, (username, password))
		self.connection.commit()

	def get_user(self, username, password):
		query = "SELECT username, password FROM users WHERE username == ? AND password == ?"
		self.cursor.execute(query, (username, password))
		user = self.cursor.fetchone()
		if user is not None:
			return True
		else:
			return False