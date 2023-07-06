# - *- coding: utf- 8 - *-
import psycopg
from config import DB_NAME, HOST, PASSWORD, USER


def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            tg_id BIGINT UNIQUE NOT NULL,
            username VARCHAR(255)
        )
        """
    )
    conn = psycopg.connect(user=USER, password=PASSWORD, host=HOST, dbname=DB_NAME)
    cur = conn.cursor()
    for com in commands:
        cur.execute(com)
    conn.commit()
    cur.close()
    conn.close()
