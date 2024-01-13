#!/bin/sh
echo "Thanks for your interest in strava-auto-kudos 🏃 :)"

python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip

read -r -p "Do you want to install dev dependencies? [y/N]} " response
pip install -r requirements/requirements.txt
if [[ $response == "y" || $response == "Y" || $response == "yes" || $response == "Yes" ]]
then
    pip install -r requirements/dev.txt
fi

echo "All done ✅"