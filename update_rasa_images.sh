#!/bin/bash

docker pull rasa/rasa-skd:latest
docker pull rasa/rasa:latest-full
docker build -t barfobot_actions:latest .
