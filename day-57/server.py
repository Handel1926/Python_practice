from flask import Flask, render_template
import random
from datetime import datetime
import requests
app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route('/')
def home():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<username>")
def guess(username):
    gender_url = f"https://api.genderize.io?name={username}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={username}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", name=username, gender=gender, age=age)

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", post=blog_data)


if __name__ == "__main__":
    app.run(debug=True)