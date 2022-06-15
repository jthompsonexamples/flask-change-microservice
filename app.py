from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def tutorialspoint():
    return "Yay, thanks for working"


if __name__ == '__main__':
    app.run()
