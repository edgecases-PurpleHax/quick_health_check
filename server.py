from flask import Flask, request

app = Flask(__name__)


@app.route('/health_check')
def hello_world():  # put application's code here
    return request.args['active']


@app.route('/alert')
def alert():
    return "Server down"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
