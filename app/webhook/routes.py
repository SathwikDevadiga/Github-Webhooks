from flask import Blueprint, request
from app.extensions import mongo
from .utils import Format_Date
from datetime import datetime , timezone

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    if request.headers['Content-Type'] =='application/json':
        payload = request.json
        event = request.headers.get('X-GitHub-Event')
        print("event "+event)
        data = None
        
        #handling push request
        if event == "push":
            data = {
                "request_id": data["after"],
                "action": "push",
                "author": payload['pusher']['name'],
                "to_branch": payload['ref'].split('/')[-1],
                "timestamp": datetime.strptime(Format_Date(payload["head_commit"]['timestamp']), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                }
        else:
            #handling merge request
            if event == "pull_request" and payload['action'] == 'closed':
                pr = payload['pull_request']
                data = {
                    "request_id": pr["id"],
                    "action": "merge",
                    "author": pr['user']['login'],
                    "from_branch": pr['head']['ref'],
                    "to_branch": pr['base']['ref'],
                    "timestamp": datetime.strptime(pr["merged_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                    
                }
            
            #handling pull request
            elif event == "pull_request":
                pr = payload['pull_request']
                data = {
                    "request_id": pr["id"],
                    "action": "pull_request",
                    "author": pr['user']['login'],
                    "from_branch": pr['head']['ref'],
                    "to_branch": pr['base']['ref'],
                    "timestamp": datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                    
                }
        # If data is not None, insert it into the MongoDB collection
        if data != None:
            print("data "+str(data))
            mongo.db.github_events.insert_one(data) 
        return {}, 200

