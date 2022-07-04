import os

import psycopg2
import dj_database_url
from psycopg2.extras import Json


class DataBase:
    def __init__(self):
        self.db_from_env = dj_database_url.config()
        print(self.db_from_env)
        self.conn = psycopg2.connect(
            host=self.db_from_env['HOST'],
            database=self.db_from_env['NAME'],
            user=self.db_from_env['USER'],
            password=self.db_from_env['PASSWORD'],
            port=self.db_from_env['PORT']
        )

        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


class DBUser(DataBase):
    def __init__(self):
        super().__init__()

    def get_user(self, login):
        self.cur.execute(f"SELECT * FROM accounts_usermodel WHERE username='{login}' ")
        return self.cur.fetchone()

    def add_user(self, username: str, user_id: int, first_name: str, last_name: str, user_json: dict, time):
        self.cur.execute(
            "INSERT INTO accounts_usermodel "
            "(username, user_id, first_name, last_name, user_json, created_at, updated_at) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (username, user_id, first_name, last_name, Json(user_json), time, time)
        )
