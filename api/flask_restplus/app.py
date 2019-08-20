# -*- coding: utf-8 -*-
from flask import Flask
from apis.todo import blueprint as todo


app = Flask(__name__)
app.register_blueprint(todo, url_prefix='/todo/1')
app.run(debug=True)
