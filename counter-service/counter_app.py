from flask import Flask

app = Flask(__name__)


counter = 0

@app.route('/increment')
def increment_counter():
    global counter
    counter += 1
    return str(counter)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)