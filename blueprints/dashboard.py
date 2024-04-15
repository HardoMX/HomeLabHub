from flask import Blueprint, render_template

dash_bp = Blueprint('dash', __name__)

@dash_bp.route("/", methods=["GET"])
def dash():
    return render_template("dashboard.html", title="Dashboard")
