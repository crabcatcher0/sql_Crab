from flask import Flask, render_template
from crab.crabmodel import CrabModel
from crab.get_data import GetData
from serializer import serializer
from models import Student


app = Flask(__name__)



@app.route("/")
def home():
    model = 'student'
    fields = ('id', 'name', 'email', 'age')
    data = serializer(model=model, fields=fields)
    return render_template('index.html', data=data)


@app.route("/teacher")
def teacher():
    model = 'teacher'
    fields = ('id', 'name', 'email', 'subject')
    data = serializer(model=model, fields=fields)
    return render_template('teacher.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
