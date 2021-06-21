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


@app.route('/cities_by_states')
def citiesdisplay():
    """display HTML of a state"""

    strict_slashes = False
    listate = []
    for vst in storage.all(State).values():
        listcity = []
        for vci in vst.cities:
            listcity.append((vci.name, vci.id))
        listcity.sort(key=lambda ytuple: ytuple[0])
        listate.append((vst.name, vst.id, listcity))
    listate.sort(key=lambda xtuple: xtuple[0])
    return render_template('8-cities_by_states.html', listate=listate)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
