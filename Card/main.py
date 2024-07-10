from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def makes():
    return render_template('card_my.html')


if __name__ == '__main__':
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True
    app.run(debug=True)