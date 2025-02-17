#!/bin/sh

confirm() {
    read -p "[y/N] " response
    if [[ $response == "y" || $response == "Y" || $response == "yes" || $response == "Yes" ]]
    then
        return 0
    else 
        return 1
    fi
}

echo "Thanks for your interest in strava-auto-kudos 🏃 :)"

# Create venv
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip

# Ask for a bunch of api + account related stuff
read -p "What is the email for your Strava account? 📧 " STRAVA_EMAIL
echo "STRAVA_EMAIL=$STRAVA_EMAIL" > .env
read -p "What is the password for your Strava account? 🔑 " STRAVA_PASSWORD
echo "STRAVA_PASSWORD=$STRAVA_PASSWORD" >> .env
read -p "What is the verify token you will use for the cURL command to set up the Strava API? 💻 " STRAVA_VERIFY_TOKEN
echo "STRAVA_VERIFY_TOKEN=$STRAVA_VERIFY_TOKEN" >> .env
read -p "What is the client id for your strava API? 🆔 " STRAVA_CLIENT_ID
echo "STRAVA_CLIENT_ID=$STRAVA_CLIENT_ID" >> .env
read -p "What is the client secret for your strava API? 🤐 " STRAVA_CLIENT_SECRET
echo "STRAVA_CLIENT_SECRET=$STRAVA_CLIENT_SECRET" >> .env


# Install requirements + optionally dev requirements
printf "Do you want to install dev dependencies? 🤖 "
confirm && python3 -m pip install -r requirements/dev.txt
python3 -m pip install -r requirements/requirements.txt

echo "All done ✅"