from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, NumberRange



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

class LoginDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    fname = db.Column(db.String(250), nullable=False)
    lname = db.Column(db.String(250), nullable=False)
    mname = db.Column(db.String(250), nullable=False)
    date_of_birth = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    matric_number = db.Column(db.String(250), nullable=False)
    department = db.Column(db.String(250), nullable=False)
    faculty = db.Column(db.String(250), nullable=False)


class SignUp(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    middle_name = StringField("Middle Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    date_of_birth = DateField("Date of birth: d/m/y", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=2, max=2)])
    matric_number = StringField("Matric number Eg ug/08/0401", validators=[DataRequired()])
    department = StringField("Department", validators=[DataRequired()])
    faculty = StringField("Faculty", validators=[DataRequired()])
    submit = SubmitField("Signup")

class Signin(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField('Login')





@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portal')
def portal():
    return render_template("portal.html")

@app.route('/login', methods=["GET", "POST"])
def sign_in():
    form = Signin()
    if form.validate_on_submit():
        return redirect(url_for("portal"))
    return render_template("signin.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)