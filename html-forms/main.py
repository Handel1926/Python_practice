from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def data_collect():
    name_data = request.form['username']
    password_data = request.form['password']
    return render_template("login.html", my_name=name_data, my_password=password_data)

if __name__ == "__main__":
    app.run(debug=True)
