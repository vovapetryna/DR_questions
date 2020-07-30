import config as cfg
import sqlite3
import sys


class DataBase:
    def __init__(self):
        self.con = None
        self.db_connect()

    def add_user(self, user, module=0, *args, **kwargs):
        cur = self.con.cursor()
        sql = 'INSERT INTO users (user, module)'\
              'SELECT ?, ?'\
              'WHERE NOT EXISTS(SELECT 1 FROM users WHERE user = ?)'
        cur.execute(sql, (user,
                          module,
                          user,
                          ))

    def update_module(self, user, module=0, *args, **kwargs):
        """Update or Insert user with module info [used with module's buttons]"""
        cur = self.con.cursor()
        sql = 'INSERT OR REPLACE INTO users (id, user, module, points) VALUES'\
              '((select id from users where user = ?), ?, ?,' \
              ' (select points from users where user = ?))'
        cur.execute(sql, (user,
                          user,
                          module,
                          user,
                          ))

    def update_points(self, user, *args, **kwargs):
        cur = self.con.cursor()
        sql = 'INSERT OR REPLACE INTO users (id, user, module, points) VALUES '\
              '((select id from users where user = ?),' \
              ' ?, (select module from users where user = ?),' \
              ' (select points from users where user = ?) + 1)'

        cur.execute(sql, (user,
                          user,
                          user,
                          user,
                          ))

    def get_lead_user(self, user, *args, **kwargs):
        """randomly get user_id with module > user.module
           return -> str (user_id)"""
        cur = self.con.cursor()
        sql = 'SELECT * FROM users WHERE user != ? AND '\
              'module > (SELECT module FROM users WHERE user = ?) ORDER BY RANDOM() LIMIT 1'

        cur.execute(sql, (user,
                          user,
                          ))
        data = cur.fetchone()

        if data is not None:
            return data[1]

    def db_connect(self):
        try:
            self.con = sqlite3.connect(cfg.db_name)
        except:
            print(f'Unexpected error {sys.exc_info()[0]}')

    def end_work(self):
        self.con.commit()
        self.con.close()
