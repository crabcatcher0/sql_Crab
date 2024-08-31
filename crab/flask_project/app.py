from flask import Flask, render_template, request, url_for, redirect, jsonify



app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/docs")
def docs():
    return render_template('docs.html')


@app.route("/success")
def success():
    return "Operation Success!"



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
