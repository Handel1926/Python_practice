from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route('/')
def start():
    return render_template("handel.html")
