from flask import Flask
import random
ANS = random.randint(0, 9)
app = Flask(__name__)



@app.route('/')
def intro():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.g' width=200 height =200>"

@app.route('/<int:number>')
def correct(number):
    if number == ANS:
        return "<h1>You are correct</h1>"
    elif number < ANS:
        return "<h1>It's too low</h1>"
    else:
        return "<h1>It's too high</h1>"

