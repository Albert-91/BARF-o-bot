#!/bin/bash

if [[ -d db_storage ]]
    then echo "db_storage directory exists."
else
    mkdir db_storage
    echo "db_storage directory has been created."
fi

docker pull rasa/rasa-sdk:latest
docker pull rasa/rasa:latest-full
docker build -t barfobot_actions:latest .
echo "Successfully pulled rasa images and built barfobot_action image."
