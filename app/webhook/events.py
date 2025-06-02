from flask import Blueprint, render_template, jsonify
from datetime import datetime, timedelta , timezone
from app.extensions import mongo
from .utils import Format_Date_UTC

data_bp = Blueprint("data", __name__, url_prefix="/get_data")

@data_bp.route("/")
def index():
    return render_template("index.html")

@data_bp.route("/events")
def get_events():
    
    events = mongo.db.github_events.find({"timestamp": {"$gte": datetime.now(timezone.utc) - timedelta(seconds=15)}})
    
    output = []
    for e in events:
        action = e.get("action")
        author = e.get("author", "Unknown")
        timestamp = Format_Date_UTC(e.get("timestamp", "Unknown time"))


        message_templates = {
            "push": f"{author} pushed to {e.get('to_branch', '?')} on {timestamp}",
            "pull_request": f"{author} submitted a pull request from {e.get('from_branch', '?')} to {e.get('to_branch', '?')} on {timestamp}",
            "merge": f"{author} merged branch {e.get('from_branch', '?')} to {e.get('to_branch', '?')} on {timestamp}",
        }

        message = message_templates.get(action, f"{author} did something on {timestamp}")
        output.append({"message": message})

    return jsonify(output)
