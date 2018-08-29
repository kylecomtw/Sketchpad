import logging
import config

logger = logging.getLogger("Sketchpad")
ch = logging.StreamHandler()
ch.setLevel("INFO")
formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel("INFO")

from flask import Flask, jsonify
from flask_cors import CORS
from Sketchpad import base_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(base_bp, url_prefix="/sketchpad")
app.config["JSON_AS_ASCII"] = False
app.config["SECRET_KEY"] = "3fa9j(7sl9"
app.config["ENV"] = "development"

if __name__ == "__main__":    
    app.run(debug=True, host="0.0.0.0", port=int(config.SERVER_PORT))

