from flask import Flask, render_template, request
from random import randint


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll-dice')
def roll():
    rolls = [randint(1,6) for _ in range(10)]
    return render_template('roll.html', rolls = rolls)

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/text-type', methods=['POST'])
def handle_form_submission():
    name = request.form['text_message']

    greeting = 'Hello, '

    greeting += name + '!'

    return render_template('text-type.html', greeting=greeting)