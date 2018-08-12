import flask, requests, os, json
from flask import request

app = flask.Flask(__name__)
API_URL = 'https://api.telegram.org/bot%s/%s'

@app.route('/<token>/', methods = ['POST'])
def fromTelegram(token):
    if token in servers.keys():
        ip, port = servers[token]['ip'], servers[token]['port']
        requests.post('http://%s:%d/%s' % (ip, port, token), data = request.data)
        return '!'
    else: flask.abort(403)

@app.route('/<token>/<method>', methods = ['GET', 'POST'])
def fromVps(token, method):
    if token in servers.keys():
        req = requests.get(API_URL % (token, method), params = request.args)
        return req.text
    else: flask.abort(403)

if __name__ == '__main__':
    servers = json.loads(open('servers.json').read())
    app.run(host = '0.0.0.0', port = os.environ.get('PORT', 5000), debug = True)