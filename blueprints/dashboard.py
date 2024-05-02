from flask import Blueprint, render_template
from datetime import datetime
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from blueprints.data.api import OWM_API_KEY

dash_bp = Blueprint('dash', __name__)

owm = OWM(OWM_API_KEY)
mgr = owm.weather_manager()

@dash_bp.route("/", methods=["GET"])
def dash():
    # TODO: figure out how to dynamically update time without page refresh
    time = datetime.now().strftime("%H:%M")
    date = datetime.now().strftime("%B %d, %Y")

    if int(datetime.now().strftime("%H")) < 12:
        time_of_day = "morning"
    elif int(datetime.now().strftime("%H")) < 18:
        time_of_day = "afternoon"
    elif int(datetime.now().strftime("%H")) < 21:
        time_of_day = "evening"
    else:
        time_of_day = "night"
        
    weather = mgr.weather_at_place('Laxa,SE').weather.detailed_status
    temp = mgr.weather_at_place('Laxa,SE').weather.temperature('celsius')

    return render_template("dashboard.html", title="Dashboard", time=time, date=date, time_of_day=time_of_day, weather=weather, temp=temp['temp'])
