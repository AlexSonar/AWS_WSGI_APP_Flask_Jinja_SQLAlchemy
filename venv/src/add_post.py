import sqlite3
import os
from flask import Flask, render_template, request, g
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


def create_db():
    # helper function for tables creating
    db = connect_db()
    # manager of context
    with app.open_resource('../sql/create_posts.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

# 

# create_db()
# or in Python console execute the: from dbc import create_db


def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db



@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    # print("test-2", dbase.getMenu())
    return render_template('index.html', menu = dbase.getMenu())
# def index():
#     db = get_db()
#     return render_template('index.html', menu = [])



@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    db = get_db()
    dbase = FDataBase(db)
 
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'])
            if not res:
                flash('Ошибка добавления статьи', category = 'error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')
 
    return render_template('add_post.html', menu = dbase.getMenu(), title="Добавление статьи")


if __name__ == "__main__":
    app.run(debug=True)