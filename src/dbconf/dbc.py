import sqlite3
import os
from flask import Flask, request, g
from FDataBase import FDataBase

# configuration
DATABASE = 'venv/db/wsgiappdb.db'
DEBUG = True
SECRET_KEY = 'dhgkikh6fhfg8ghmh3fg87f'
USERNAME = 'admin'
PASSWORD = 'secret'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path,'../db/wsgiappdb.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if hasattr(g, 'link_db'):
        g.link_db.close()