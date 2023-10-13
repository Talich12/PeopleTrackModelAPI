from flask import Flask
from .people_track import PeopleTrackModel

app = Flask(__name__)

model = PeopleTrackModel()

from app import routes
