from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///names.db"
db.init_app(app)


class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    surname = db.Column(db.String(250), nullable=False)




with app.app_context():
    db.create_all()





@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        user_name = Name(name=request.form["fname"], surname=request.form["lname"])
        db.session.add(user_name)
        db.session.commit()
        return redirect(url_for("home", id=user_name.id))
    tame = db.session.query(Name)
    for p in tame:
        print(p.name)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)