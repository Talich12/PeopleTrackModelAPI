from flask import Flask
from .people_track import PeopleTrackModel
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = PeopleTrackModel()

from app import routes
