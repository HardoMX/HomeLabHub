from flask import Blueprint, render_template

from pyowm import OWM
from blueprints.data.api import OWM_API_KEY
from blueprints.data.settings import CATEGORIES, BACKGROUND, SITES, LOCATION

dash_bp = Blueprint('dash', __name__)

owm = OWM(OWM_API_KEY)
mgr = owm.weather_manager()

@dash_bp.route("/", methods=["GET"])
def dash():
    weather = mgr.weather_at_place(LOCATION).weather.detailed_status
    temp = mgr.weather_at_place(LOCATION).weather.temperature('celsius')['temp']
    weather_symbol = mgr.weather_at_place(LOCATION).weather.weather_icon_name

    return render_template("dashboard.html", title="Dashboard", background=BACKGROUND, weather=weather, temp=temp, weather_symbol=weather_symbol, location=LOCATION, sites=SITES, categories=CATEGORIES)
