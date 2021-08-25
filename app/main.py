from flask import Flask, request,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello_world')
def hello_world():
    return render_template('hello_world.html')

if __name__ == '__main__':
    app.run(debug=True)
