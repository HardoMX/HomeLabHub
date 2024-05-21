from flask import Blueprint ,render_template, redirect, request, url_for

from pyowm import OWM
from blueprints.data.api import OWM_API_KEY

from blueprints.data.settings import BACKGROUND, LOCATION

cms_bp = Blueprint("cms", __name__)

owm = OWM(OWM_API_KEY)
mgr = owm.weather_manager()

@cms_bp.route("/settings", methods=["GET"])
def settings():
    weather = mgr.weather_at_place(LOCATION).weather.detailed_status
    temp = mgr.weather_at_place(LOCATION).weather.temperature('celsius')['temp']
    weather_symbol = mgr.weather_at_place(LOCATION).weather.weather_icon_name
    
    file = open('blueprints/data/settings.yaml', 'r')
    settings = file.read()
    file.close()
    
    return render_template("settings.html", title="Settings", background=BACKGROUND, weather=weather, temp=temp, weather_symbol=weather_symbol, settings=settings)

@cms_bp.route("/cms/add/site", methods=["POST"])
def add_site():
    print(request.form)
    title = request.form["title"]
    url = request.form["url"]
    description = request.form["description"]
    icon = request.form["icon"]
    category = request.form["category"]

    text = f"""  - name: { title }
    url: { url }
    description: { description }
    icon: { icon }
    category: { category }"""

    with open('blueprints/data/settings.yaml', 'a') as file:
        file.write(text)

    return redirect(url_for("dash.dash"))

@cms_bp.route("/cms/edit", methods=["POST"])
def edit():
    print(request.form)

    text = request.form["settings"]
    text.strip("\r")
    print(text)

    with open('blueprints/data/settings.yaml', 'w') as file:
        file.write(text)

    return redirect(url_for("cms.settings"))
