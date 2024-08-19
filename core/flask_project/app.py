from flask import Flask, render_template
from core.crabmodel import CrabModel
from core.get_data import GetData
from serializer import viewserial
from models import Student


app = Flask(__name__)



@app.route("/")
def home():
    data = viewserial()
    print(f'This is data: {data}')
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
