from flask import Blueprint

bp = Blueprint("util", __name__, url_prefix="/mgr")


@bp.route("/")
def index():
    return "index page"
