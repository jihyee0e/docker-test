# app.py
from flask import Flask

app = Flask(__name__)

# / 주소로 호출
@app.route('/')
def home():
    return "Hello, Dockerized Flask!"

@app.route('/hello')
def home2():
    return "Hello2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
