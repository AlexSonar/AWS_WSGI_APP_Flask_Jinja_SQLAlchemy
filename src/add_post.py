import sqlite3
import os
from flask import Flask, render_template, request, g, abort
from FDataBase import FDataBase
from flask.helpers import flash


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
@app.route("/index")
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
    '''Close connection to DB'''
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    db = get_db()
    dbase = FDataBase(db)
    # msg_suc = '''<strong><i class="fa fa-thumbs-o-up"></i> tttttttu</strong>Post aded sucsesfuly!'''
    # file:///home/alex/Documents/ENV_App_Front_End/A_aThemeForestSourse/shortcodes-alerts.html
    msg_suc = '''Post aded sucsesfuly!'''
 
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Error post adition!', category = 'alert alert-danger')
            else:
                flash(msg_suc, category='alert alert-success')
        else:
            flash('Post error!', category='alert alert-danger')
 
    return render_template('add_post.html', menu = dbase.getMenu(), title="Adding new posts", posts=dbase.getPostsAnonce())


# Show the post 
# http://127.0.0.1:5000/post/1 /post/<int:id_post>
# def showPost(id_post):
# title, post = dbase.getPost(id_post)
@app.route("/post/<alias_post>")
def showPost(alias_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.getPost(alias_post)
    if not title:
        abort(404)
 
    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post, posts=dbase.getPostsAnonce())



if __name__ == "__main__":
    app.run(debug=True)
