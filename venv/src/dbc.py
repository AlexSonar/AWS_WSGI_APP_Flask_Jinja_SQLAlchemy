import sqlite3
import os
from flask import Flask, render_template, request

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
    with app.open_resource('../sql/sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


create_db()
# from dbc import create_db


if __name__ == "__main__":
    app.run(debug=True)