# Strava Kudos Bot

## Description

A bot that gives Strava kudos everytime an account it follows uploads an activity. For instructions on how to set up your own Strava kudos bot, check out the section below!

## Create your own Strava Kudos Bot

Instructions for creating your own Strava Kudos Bot can be found below.

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

6. Not Complete Yet: At this point, every time someone who your bot is following posts something, the bot should go ahead and give kudos. Note that for this to work, the sharing settings need to be set properly.

### Troubleshooting

-   Some issues might arise if your environment variables are configured incorrectly. Make sure that you have the correct `STRAVA_EMAIL`, `STRAVA_PASSWORD` and `NGROK_DOMAIN` set up in your `.env` file.
-   Make sure that the authorization callback domain within your Strava API settings matches your `NGROK_DOMAIN` in your `.env` file and that you started the ngrok session with this domain redirecting to localhost running on port 5000.

## Resources

-   [Strava Webhooks](https://developers.strava.com/docs/webhooks/)
-   [Strava API Settings](https://www.strava.com/settings/api)
-   [Strava Webhook Example](https://developers.strava.com/docs/webhookexample/)
-   [Getting Started with ngrok](https://ngrok.com/docs/getting-started/)
