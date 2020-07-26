#! /usr/bin/env/python

from flask import Flask, render_template, request, redirect

app=Flask(__name__)

cats=[]

@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def catch_all(path):
    author = "Yummo"
    name = "World"
    return render_template("index.html", author=author, name=name)

@app.route('/cats.html')
def cat_world():
    return render_template("cats.html", cats=cats)

@app.route('/fish.html')
def fish_world():
    return render_template("fish.html")

@app.route('/about.html')
def about_world():
    return render_template("about.html")

@app.route('/submit-cat', methods=["POST"])
def signup_cat():
    name=request.form["name"]
    cats.append(name)
    print(cats)
    return redirect('/')

if __name__== '__main__':
    app.run()

