#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display HTML page like 8-index.html """

    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    return render_template(
        '100-hbnb.html',
        states=states,
        amenities=amenities,
        places=places
    )


@app.teardown_appcontext
def close_session(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

