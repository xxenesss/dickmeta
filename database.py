import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''ALTER TABLE users RENAME TO users_old''')
    c.execute('''CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    telegram_id TEXT NOT NULL,
                    username TEXT,  -- Allow NULL values for username
                    nickname TEXT,
                    sm: NOT NULL,
                    last_click: TIMESTAMP
                )''')
    c.execute('''INSERT INTO users (id, telegram_id, username, nickname, sm, last_click)
                 SELECT id, telegram_id, username, nickname, sm FROM users_old''')
    c.execute('''DROP TABLE users_old''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()