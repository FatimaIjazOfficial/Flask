from flask import Flask

app =Flask(__name__)

@app.route('/')
def data_world():
    return 'Website_making'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()