from flask import Blueprint

bp = Blueprint("gateway", __name__, url_prefix="/mgr")


@bp.route("/")
def index():
    return "index page"
