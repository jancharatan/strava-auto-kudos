#!/bin/sh

confirm() {
    read -r -p "[y/N]} " response
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

# Install requirements + optionally dev requirements
echo -n "Do you want to install dev dependencies? "
confirm && pip install -r requirements/dev.txt
pip install -r requirements/requirements.txt

echo "All done ✅"