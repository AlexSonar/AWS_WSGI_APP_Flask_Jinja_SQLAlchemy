import sqlite3
import os
from flask import Flask, render_template, request, g
from FDataBase import FDataBase

from dbconf.dbc import connect_db, dbcconf
from dbc import connect_db, dbcconf


connect_db()


def create_db():
    # helper function for tables creating
    db = connect_db()
    # manager of context
    with app.open_resource('../sql/create_posts.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

# 


create_db()
# or in Python console execute the: from dbc import create_db


get_db()



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
    # Закрываем соединение с БД, если оно было установлено
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
