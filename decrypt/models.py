import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_post(name,content,pan):
    con = sql.connect(path.join(ROOT,'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name,content,pan) values(?,?,?)',(name,content,pan))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT,'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts