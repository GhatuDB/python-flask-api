from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_template():
    return render_template('home.html')


@app.route('/login')
def login_template():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
