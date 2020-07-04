from flask import Flask, render_template
from jinja2 import Template
app = Flask(__name__)

menu = ["<a href='about.html'>Установка</a> ", "Первое приложение ", "Обратая связь "]


@app.route("/")
@app.route("/index")
def index():
    # return "index"
    return render_template('index.html', title="Index page", menu=menu)


@app.route("/about")
def about():
    # return "<h1> About</h1>"
    return render_template('about.html')


def page_not_found(e):
    return render_template('404.html'), 404


# def create_app(config_filename):
#     app = Flask(__name__)
#     app.register_error_handler(404, page_not_found)
#     return app

if __name__ == "__main__":
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
