from flask import Flask, render_template
import datetime
import random
import requests


app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def get_guess(name):
    g_url = f"https://api.genderize.io?name={name}"
    g_response = requests.get(g_url)
    g_data = g_response.json()
    gender = g_data["gender"]
    a_url = f"https://api.agify.io?name={name}"
    a_response = requests.get(a_url)
    a_data = a_response.json()
    age = a_data["age"]
    return render_template("guess.html", person_name=name, gender=gender, age=age)


@app.route("/blog")
def get_blog():
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
