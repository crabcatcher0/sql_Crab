from flask import Flask, render_template, request, url_for, redirect, jsonify
from serializer import serializer
from models import Student, Teacher


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/student")
def stident():
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
    data = None
    if request.method == 'POST':
        name = request.form.get('student_name')
        age = request.form.get('age')
        email = request.form.get('email')
        data = {
            'name':name,
            'age': age,
            'email': email,
        }
        Student.add_data(column=data)
        return redirect(url_for('success'))

    return render_template('add_student.html', data=data)



@app.route("/add_teacher", methods = ['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form.get('teacher_name')
        subject = request.form.get('subject')
        email = request.form.get('email')
        data = {
            'name': name,
            'subject':subject,
            'email': email
        }
        Teacher.add_data(column=data)
        return redirect(url_for('success'))
    
    return render_template('add_teacher.html')



@app.route("/delete/<int:pk>", methods=['POST'])
def delete_data(pk):
    try:
        Student.delete(pk=pk)
        return redirect(url_for('success'))
    except Exception as e:
        return jsonify({"error": str(e)}), 400




@app.route("/success")
def success():
    return "Operation Success!"




if __name__ == '__main__':
    app.run(debug=True)
