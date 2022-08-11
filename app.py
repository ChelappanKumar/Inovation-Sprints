from flask import Flask, render_template  

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/login')
def about():
    return 'Login Page'

@app.route('/register')
def register():
    return 'Register Page'


if __name__ == '__main__':
    app.run(debug=True)
