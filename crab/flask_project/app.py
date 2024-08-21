from flask import Flask, render_template, request, url_for, redirect
from serializer import serializer
from crab.core.add_data import Data


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



@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    model = 'student'
    data = None
    if request.method == 'POST':
        name = request.form.get('student_name')
        age = request.form.get('age')
        email = request.form.get('email')
        data = Data.add_data(table_name=model, column={
            'name': name,
            'email': email,
            'age':age
        })
        return redirect(url_for('success'))

    return render_template('add_student.html', data=data)



@app.route("/success")
def success():
    return "Operation Success!"



if __name__ == '__main__':
    app.run(debug=True)
