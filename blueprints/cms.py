from flask import Blueprint ,render_template, redirect, request

from pyowm import OWM
from blueprints.data.api import OWM_API_KEY

from blueprints.data.sites import SITES
from blueprints.data.settings import BACKGROUND
import blueprints.data.settings

cms_bp = Blueprint("cms", __name__)

owm = OWM(OWM_API_KEY)
mgr = owm.weather_manager()

@cms_bp.route("/settings", methods=["GET"])
def settings():
    weather = mgr.weather_at_place('Laxa,SE').weather.detailed_status
    temp = mgr.weather_at_place('Laxa,SE').weather.temperature('celsius')['temp']
    weather_symbol = mgr.weather_at_place('Laxa,SE').weather.weather_icon_name
    
    settings = open('blueprints/data/settings.yaml', 'r')
    sites = open('blueprints/data/sites.yaml', 'r')
    
    return render_template("settings.html", title="Settigns", background=BACKGROUND, weather=weather, temp=temp, weather_symbol=weather_symbol, settings=settings.read(), sites=sites.read())

@cms_bp.route("/cms/sites/create", methods=["POST"])
def create_site():
    print(request.form)
    return redirect("/settings")

@cms_bp.route("/cms/edit-settings", methods=["POST"])
def edit_settings():
    print(request.form)
    return redirect("/settings")

@cms_bp.route("/cms/edit-sites", methods=["POST"])
def edit_sites():
    print(request.form)
    return redirect("/settings")