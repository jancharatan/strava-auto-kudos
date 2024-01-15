# Strava Kudos Bot

## Description

A bot that gives Strava kudos everytime an authorized account uploads an activity. For instructions on how to set up your own Strava kudos bot, see the section below!

## Create your own Strava Kudos Bot

### Requirements

-   python3
-   Strava account that logs in just with username/password (not with Google, etc.)
-   `ngrok` installed & a free `ngrok` account (with the included free static domain)

### Instructions

1. Run `sh startup.sh` and respond to all of the prompts. Note: you don't need dev dependencies just to run the app.
2. Create an ngrok account and run `ngrok http http://localhost:5000 --domain {YOUR_NGROK_DOMAIN}`
3. In a separate terminal, make sure you are in the `venv` and run `python3 app.py`
4. Make sure that your Strava API is set up correctly in your account. Most importantly, make sure that your authorization callback domain is set to `YOUR_FREE_STATIC_URL.ngrok-free.app` where you have replaced the subdomain with your subdomain.
5. Run the following `cURL` command to subscribe the Strava webhook. Make sure to change the client id, client secret, the subdomain of the callback url and the verify token.

```
curl -X POST https://www.strava.com/api/v3/push_subscriptions \
    -F client_id=CLIENT_ID_FROM_STRAVA_API_SETTINGS_PAGE \
    -F client_secret=CLIENT_SECRET_FROM_STRAVA_API_SETTINGS_PAGE \
    -F callback_url=https://YOUR_FREE_STATIC_URL.ngrok-free.app/webhook \
    -F verify_token=VERIFY_TOKEN_YOU_CHOSE_IN_STARTUP_SCRIPT_LOCATED_IN_ENV_FILE
```

6. At this point, every time an authorized account that the bot follows uploads an activity, the bot should give kudos. To authorize an account, paste the following url into a browser where you are logged in to the account you want authorized.

```
https://www.strava.com/oauth/authorize?client_id=CLIENT_ID_FROM_STRAVA_API_SETTINGS_PAGE&response_type=code&scope=activity:read_all&redirect_uri=https://YOUR_FREE_STATIC_URL.ngrok-free.app/webhook
```

### Troubleshooting

-   Some issues might arise if your environment variables are configured incorrectly. Make sure that you have the correct `STRAVA_EMAIL`, `STRAVA_PASSWORD`, `STRAVA_VERIFY_TOKEN`, `STRAVA_CLIENT_ID` and `STRAVA_CLIENT_SECRET` set up in your `.env` file.
-   Make sure that the authorization callback domain within your Strava API settings matches your `ngrok` domain and that you started the ngrok session with this domain redirecting to localhost running on port 5000.

## Resources

-   [Strava Webhooks](https://developers.strava.com/docs/webhooks/)
-   [Strava API Settings](https://www.strava.com/settings/api)
-   [Strava Webhook Example](https://developers.strava.com/docs/webhookexample/)
-   [Medium Article](https://medium.com/@eric.l.m.thomas/setting-up-strava-webhooks-e8b825329dc7)
-   [Another Article](https://www.curtiscode.dev/post/project/displaying-strava-stats-using-webhooks/)
-   [Getting Started with ngrok](https://ngrok.com/docs/getting-started/)
