import os
import base64
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pics1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "we moving"
Bootstrap(app)
db = SQLAlchemy(app)


class Pics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50), unique=True, nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)

with app.app_context():
    db.create_all()
class UploadPhoto(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('upload')




@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadPhoto()
    if form.validate_on_submit():
        pic = form.photo.data
        filename = secure_filename(pic.filename)
        upload = Pics(filename=filename, data=pic.read())
        db.session.add(upload)
        db.session.commit()
    return render_template("index.html", form=form)

@app.route('/water')
def water_mark():
    watermark_text = 'handel'
    pic = Image.open(picture)
    draw = ImageDraw.Draw(pic)
    font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
    font = ImageFont.load_default()
    t_width, t_height = draw.textsize(watermark_text, font)
    x = int((pic.size[0] - t_width) / 2)
    y = int((pic.size[1] - t_height) / 2)
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255))

@app.route('/image')
def image():
    file_data = Pics.query.filter_by(id=5).first()
    picture = base64.b64encode(file_data.data).decode('ascii')
    return render_template('show.html', data=list, image=picture)


if __name__ == "__main__":
    app.run(debug=True)