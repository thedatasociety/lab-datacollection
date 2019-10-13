import sqlite3

conn = sqlite3.connect('../database.db')

curr = conn.cursor()

curr.execute("""CREATE TABLE IF NOT EXISTS scrapy_tb(
                title text,
                author text,
                tag text)""")
conn.commit()
conn.close()
