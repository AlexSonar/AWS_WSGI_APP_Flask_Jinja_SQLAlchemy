from flask import Flask, render_template, request, flash, session, redirect, abort
from jinja2 import Template
from flask.helpers import url_for
# from main_menu import mmenu
# from main_menu import mmenu

# import sys
# sys.path.append("venv/src/parts")
# from main_menu import *


# from venv.src.main_menu import mmenu
# from venv.src.main_menu import mmenu

# import venv.src.main_menu
# from venv.src import main_menu
# from venv.src.main_menu import mmenu
# import main_menu

# from parts import main_menu

import main_menu
from main_menu import mmenu


app = Flask(__name__)

app.config['SECRET_KEY'] = 'dxjq4flx39cndidgcailfgjdgs67ns'
menu = main_menu.mmenu()
# menu = mmenu
# menu = main_menu.mmenu
# menu = main_menu.mmenu()
# menu = ["<a href='about.html'>Установка</a> ", "Первое приложение ", "Обратая связь "]
# menu = [
#         {"name": "FLASK"
#         , "url": "flask"},
#         {"name": "JINJA", "url": "jinja"},
#         {"name": "install & irst-app", "url": "install-flask"},
#         {"name": "ABOUT", "url": "about"},
#         {"name": "CONTACT", "url": "contact"},
#         {"name": "lOGIN", "url": "login"}
#         ]



@app.route("/")
@app.route("/index")
def index():
    # return "index"
    print("loaded" + url_for('index'))
    return render_template('index.html', title="Index page", menu=menu)

@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "Alex" and request.form['psw'] == "secret":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
 
    return render_template('login.html', title="Авторизация", menu=menu)


@app.route("/about")
def about():
    # return "<h1> About</h1>"
    return render_template('about.html')

@app.route("/mitl")
def mitl():
    # return "<h1> About</h1>"
    return render_template('mitl.html', title="The MIT License", menu=menu)
 
# errorhandler decorator
# @app.errorhandler(404)
# def pageNotFount(error):
#     return render_template('page404.html', title="Страница не найдена", menu=menu)    
def page_not_found(e):
    return render_template('page404.html', title="404 page", menu=menu), 404

# @app.route("/contact", methods=["POST"])
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Thank you for your message!', category='success')
        else:
            flash('Sending error. the message was not sent', category='error')
        print(request.form)
        print(request.form['username'])
    return render_template('contact.html', title="Contact to us", menu=menu)


# @app.route("/profile/<username>")
# def profile(username):
#     return f"Username: {username}"

@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
        # return render_template('page404.html', title=abort(401), menu=menu), 404        
    return f"Пользователь: {username}"


@app.route("/profile/<int:userid>/<path>")
def profileid(userid, path):
    # print("loaded" + url_for('profile', userid="userid", path="path" ))
    # print("loaded" + "User ID: {userid}, {path}" )
    return f"User ID: {userid}, {path}"

# def create_app(config_filename):
#     app = Flask(__name__)
#     app.register_error_handler(404, page_not_found)
#     return app

if __name__ == "__main__":
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
