from flask import Flask

def mmenu():
    menu = [
        {"name": "FLASK"
        , "url": "flask"},
        {"name": "JINJA", "url": "jinja"},
        {"name": "install & irst-app", "url": "install-flask"},
        {"name": "ABOUT", "url": "about"},
        {"name": "CONTACT", "url": "contact"},
        {"name": "lOGIN", "url": "login"}
        ]
    return menu