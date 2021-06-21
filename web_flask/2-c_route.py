#!/usr/bin/python3
"""A script that starts a Flask web application."""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """web application to listen on 0.0.0.0, port 5000"""

    strict_slashes = False
    return 'Hello, HBNB!'


@app.route('/hbnb')
def hello_again():
    """web application to listen on 0.0.0.0, port 5000"""

    strict_slashes = False
    return 'HBNB'


@app.route('/c/{}'.format(sometexts))
def hello_again(sometexts):
    """web application to listen on 0.0.0.0, port 5000"""

    strict_slashes = False
    alt_string = sometexts.replace('_', ' ')
    return 'C {}'.format(alt_string)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
