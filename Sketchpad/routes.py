from flask import Blueprint

base_bp = Blueprint('sketchpad', __name__)

@base_bp.route("/")
def index():
    return "Hello Sketchpad"