#!/usr/bin/python3
"""a list of states on HTML states_list"""

from models import storage
from flask import render_template, Flask
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display a HTML page: (inside the tag BODY)"""
    # sort states by name from a to z
    slist = sorted(storage.all(
        State).values(), key=lambda x: x.name)
    # sort cities by name from a to z
   
    return render_template("8-cities_by_states.html", sorted_states_list=slist)


@app.teardown_appcontext
def terminate(exc):
    """close the storage"""
    storage.close()


if __name__ == '__main__':
    """start the server"""
    app.run(host='0.0.0.0', port=5000)
