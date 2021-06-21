#!/usr/bin/python3
"""A script that starts a Flask web application."""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """text hello hbnb!"""

    strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_again():
    """text hbnb"""

    strict_slashes = False
    return 'HBNB'


@app.route('/c/<text>')
def cis_alwaysfun(text):
    """text c and something"""

    strict_slashes = False
    alt_string = text.replace('_', ' ')
    return 'C {}'.format(alt_string)


@app.route('/python/')
@app.route('/python/<text>')
def pythonis_cool(text='is cool'):
    """text python and something"""

    strict_slashes = False
    alt_string = text.replace('_', ' ')
    return 'Python {}'.format(alt_string)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
