from flask import Flask, render_template
from models import Methods

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/docs")
def docs():
    data = ["#overview", "#usage", "#methods", "#datatypes", "#getdata", "#serializer"]
    method_data = Methods.return_model()
    return render_template('docs.html', data=data, method_data=method_data)


@app.route("/success")
def success():
    return "Operation Success!"



if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")