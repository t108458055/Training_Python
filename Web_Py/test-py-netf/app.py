# -*- coding: utf-8 -*-
import sys
from flask import Flask, render_template
from flask_frozen import Freezer


app = Flask(__name__)
freezer = Freezer(app)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about.html")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        print("Building website...")
        freezer.freeze()
    else:
        app.run(debug=True)