from flask import Blueprint
from flask import request, jsonify, session
from .wander_engine import WanderEngine

base_bp = Blueprint('sketchpad', __name__)
we = WanderEngine()

@base_bp.route("/")
def index():
    return "Hello Sketchpad"

@base_bp.route("/wander", methods=["POST"])
def wander():
    jobj = request.get_json(silent=True)
    if not jobj:
        resp = jsonify(status="Json object expected")
        resp.status_code = 400
        return resp
         
    input_text = jobj.get("text", "")    
    if not input_text:
        resp = jsonify(status="empty string")
        resp.status_code = 400
        return resp
    
    thought, memory = we.wander(input_text, session["memory"]) 
    session["memory"] = memory
        
    session.modified = True
    resp = jsonify(status="ok", responseText=thought.responseText)
    return resp
    