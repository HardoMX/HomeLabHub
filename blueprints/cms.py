from flask import Blueprint ,render_template, redirect, request

from pyowm import OWM
from blueprints.data.api import OWM_API_KEY

from blueprints.data.settings import BACKGROUND

cms_bp = Blueprint("cms", __name__)

owm = OWM(OWM_API_KEY)
mgr = owm.weather_manager()

@cms_bp.route("/settings", methods=["GET"])
def settings():
    weather = mgr.weather_at_place('Laxa,SE').weather.detailed_status
    temp = mgr.weather_at_place('Laxa,SE').weather.temperature('celsius')['temp']
    weather_symbol = mgr.weather_at_place('Laxa,SE').weather.weather_icon_name
    
    file = open('blueprints/data/settings.yaml', 'r')
    settings = file.read()
    file.close()
    
    return render_template("settings.html", title="Settings", background=BACKGROUND, weather=weather, temp=temp, weather_symbol=weather_symbol, settings=settings)

@cms_bp.route("/cms/add/site", methods=["POST"])
def add_site():
    print(request.form)
    return redirect("/settings")

@cms_bp.route("/cms/edit", methods=["POST"])
def edit():
    print(request.form)
    return redirect("/settings")