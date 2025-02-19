import sqlite3
import re

class UserData:
    def __init__(self):
        self.conn = sqlite3.connect('art_database.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def validate_username(self, username):
        return re.match(r'^\w{3,20}$', username) is not None

    def validate_password(self, password):
        return re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$', password) is not None

    def add_user(self, username, password):
        try:
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # إذا كان اسم المستخدم موجودًا مسبقًا

    def verify_user(self, username, password):
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        return self.cursor.fetchone() is not None
