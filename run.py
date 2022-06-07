from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    user = {
        'username': 'brians',
        'email': 'brain@codingtemple.com'
    }
    return render_template('index')


@app.route("/test")
def test():
    return 'this is a prueba'