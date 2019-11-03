#!/bin/bash

docker pull rasa/rasa-sdk:latest
docker pull rasa/rasa:latest-full
docker build -t barfobot_actions:latest .
echo "Successfully pulled rasa images and built barfobot_action image."
