import json
from flask import Flask, request
from dotenv import dotenv_values

app = Flask(__name__)
secrets = dotenv_values(".env")

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
        return json.dumps({ 'message': 'Event Received', 'code': 'SUCCESS' }), 200  

def main():
    print("Starting strava-auto-kudos...")
    app.run(port=5000, debug=True)

if __name__ == "__main__":
    main()
