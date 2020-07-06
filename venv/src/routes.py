from flask import Flask, render_template, request
from jinja2 import Template
from flask.helpers import url_for
app = Flask(__name__)

# menu = ["<a href='about.html'>Установка</a> ", "Первое приложение ", "Обратая связь "]
menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]

@app.route("/")
@app.route("/index")
def index():
    # return "index"
    print("loaded" + url_for('index'))
    return render_template('index.html', title="Index page", menu=menu)


@app.route("/about")
def about():
    # return "<h1> About</h1>"
    return render_template('about.html')

@app.route("/mitl")
def mitl():
    # return "<h1> About</h1>"
    return render_template('mitl.html', title="The MIT License", menu=menu)
 

def page_not_found(e):
    return render_template('page404.html', title="404 page", menu=menu), 404

# @app.route("/contact", methods=["POST"])
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        print(request.form)
        print(request.form['username'])
    return render_template('contact.html', title="Contact to us", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Username: {username}"


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
