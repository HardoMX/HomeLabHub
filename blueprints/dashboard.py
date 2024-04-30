from flask import Blueprint, render_template
from datetime import datetime

dash_bp = Blueprint('dash', __name__)

@dash_bp.route("/", methods=["GET"])
def dash():
    # TODO: figure out how to dynamically update time without page refresh
    time = datetime.now().strftime("%H:%M:%S")
    date = datetime.now().strftime("%B %d, %Y")

    if int(datetime.now().strftime("%H")) < 12:
        time_of_day = "morning"
    elif int(datetime.now().strftime("%H")) < 18:
        time_of_day = "afternoon"
    elif int(datetime.now().strftime("%H")) < 21:
        time_of_day = "evening"
    else:
        time_of_day = "night"

    return render_template("dashboard.html", title="Dashboard", time=time, date=date, time_of_day=time_of_day)
