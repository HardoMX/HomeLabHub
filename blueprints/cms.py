from flask import Blueprint ,render_template, redirect, request

from blueprints.data.sites import SITES
import blueprints.data.settings

cms_bp = Blueprint("cms", __name__)

@cms_bp.route("/cms/sites/create", methods=["POST"])
def create_site():
    print(request.form)
