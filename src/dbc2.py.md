import sqlite3
import os
from flask import Flask, render_template, request

# Config
DATABASE = '/tmp/flsile.db'
DEBUG = True
SECRET_KEY = 'khg6sdlkj34fhglds45jh'

app = Flask(__name__)
app.config.from_object(__name__)

