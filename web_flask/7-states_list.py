#!/usr/bin/python3
"""script that starts a Flask web application"""

from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def closestorage(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list')
def statedisplay():
    """display HTML of a state"""

    strict_slashes = False
    listate = []
    for v in storage.all(State).values():
        listate.append((v.name, v.id))
    listate.sort(key=lambda xtuple: xtuple[0])
    return render_template('7-states_list.html', listate=listate)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
