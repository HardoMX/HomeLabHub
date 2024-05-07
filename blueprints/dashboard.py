from flask import Blueprint, render_template

from flask_socketio import emit
import subprocess

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

from blueprints.data.api import OWM_API_KEY
from blueprints.data.sites import sites

dash_bp = Blueprint('dash', __name__)

owm = OWM(OWM_API_KEY)
mgr = owm.weather_manager()

@dash_bp.route("/", methods=["GET"])
def dash():
    weather = mgr.weather_at_place('Laxa,SE').weather.detailed_status
    temp = mgr.weather_at_place('Laxa,SE').weather.temperature('celsius')['temp']

    return render_template("dashboard.html", title="Dashboard", weather=weather, temp=temp, sites=sites)