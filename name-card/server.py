from flask import Flask, render_template
app = Flask(__name__, template_folder="template", static_folder="static")

@app.route('/')
def start_page():
    return render_template("handels.html")