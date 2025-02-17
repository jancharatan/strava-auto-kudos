import json
import requests
from threading import Thread
from flask import Flask, request
from dotenv import dotenv_values
from strava_controller import StravaController
from comments import fetch_random_comment

app = Flask(__name__)

def give_kudos_and_post_comment(object_id: int, comment: str | None) -> None:
    print(f"Giving kudos and a nice comment to activity {object_id}...")
    sc = StravaController()
    sc.login()
    sc.give_kudos(object_id)
    if comment:
        sc.post_comment(object_id, comment)
    sc.driver.close()

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    secrets = dotenv_values(".env")
    if request.method == 'GET':
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if (mode == 'subscribe' and token == secrets["STRAVA_VERIFY_TOKEN"]):
            return json.dumps({ "hub.challenge": challenge }), 200
        
        client_id = secrets["STRAVA_CLIENT_ID"]
        client_secret = secrets["STRAVA_CLIENT_SECRET"]
        code = request.args.get("code")
        grant_type = "authorization_code"

        url = "https://www.strava.com/oauth/token"
        payload = json.dumps({ "client_id": client_id, "client_secret": client_secret, "code": code, "grant_type": grant_type })
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        if code:
            requests.post(url, data=payload, headers=headers)
            return json.dumps({ "verification": "success"}), 200

        return json.dumps({}), 403
    elif request.method == 'POST':
        data = request.get_json()
        if data.get("object_type") == "activity":
            Thread(target=lambda: give_kudos_and_post_comment(data.get("object_id"), fetch_random_comment())).start()
        return json.dumps({ 'message': 'Event Received', 'code': 'SUCCESS' }), 200  

def main():
    print("Starting strava-auto-kudos...")
    give_kudos_and_post_comment(13637247752, "Hi")

if __name__ == "__main__":
    main()
