#! /usr/bin/env/python

from flask import Flask, render_template, request, redirect

app=Flask(__name__)

cats=[]

@app.route('/index.html')
def hello_world():
    author = "Yummo"
    name = "World"
    return render_template("index.html", author=author, name=name)

@app.route('/cats.html')
def cat_world():
    return render_template("cats.html", cats=cats)

@app.route('/fish.html')
def fish_world():
    return render_template("fish.html")

@app.route('/submit-cat', methods=["POST"])
def signup_cat():
    name=request.form["name"]
    cats.append(name)
    print(cats)
    return redirect('/index.html')

if __name__== '__main__':
    app.run()

