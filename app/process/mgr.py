from flask import Blueprint
from markupsafe import escape

bp = Blueprint("mgr", __name__, url_prefix="/mgr")


@bp.route("/")
def index():
    return "index page"


@bp.route("/create/<path>")
def create(path):
    path = escape(path)
    print("create path: ", path)
    pass


@bp.route("/ensure_path/<path>")
def ensure_path(path):
    pass


@bp.route("/exists/<path>")
def exists(path):
    pass


@bp.route("/get/<path>")
def get(path, watch=None):
    pass


@bp.route("/get/<path>")
def get_children(path):
    pass


@bp.route("/set/<path>/<data>")
def set(path, data):
    """# 设置数据"""
    pass


@bp.route("/delete/<path>")
def delete(path):
    """# 删除数据"""
    pass
