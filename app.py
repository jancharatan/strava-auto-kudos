import json
from threading import Thread
from flask import Flask, request
from dotenv import dotenv_values
from strava_controller import StravaController

app = Flask(__name__)
secrets = dotenv_values(".env")

def give_kudos(object_id: int) -> None:
    sc = StravaController()
    sc.give_kudos_by_activity_id(object_id)
    sc.driver.close()

@app.route('/webhook', methods=['GET', 'POST'])
def webhooks():
    if request.method == 'GET':
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if (mode == 'subscribe' and token == secrets["STRAVA_VERIFY_TOKEN"]):
            return json.dumps({ "hub.challenge": challenge }), 200
        return json.dumps({}), 403
    elif request.method == 'POST':
        data = request.get_json()
        if data.get("object_type") == "activity":
            Thread(target=lambda: give_kudos(data.get("object_id"))).start()
        return json.dumps({ 'message': 'Event Received', 'code': 'SUCCESS' }), 200  

def main():
    print("Starting strava-auto-kudos...")
    app.run(port=5000, debug=True)

if __name__ == "__main__":
    main()
