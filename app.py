from flask import Flask, render_template, redirect, request, url_for
from model import salary_model


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/salary", methods=['POST'])
def salary():
    if request.method == 'POST':
        experience = request.form['years']
        model_prediction = salary_model(experience)
        return render_template('salary.html', years=model_prediction)
    else:
        pass


@app.route("/404", methods=['GET'])
def error_404():
    try:
        return render_template('404.html')
    except:
        pass


if __name__ == "__main__":
    app.run(debug=True)