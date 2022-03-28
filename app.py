from flask import Flask, render_template, request
from model import salary_model

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/salary', methods=['POST'])
def salary_page():
    if request.method == "POST":
        years = request.form['years']
        model_salary = salary_model(years)
    return render_template('salary.html', predicted_salary=model_salary)


if __name__ == "__main__":
    app.run(debug=True)