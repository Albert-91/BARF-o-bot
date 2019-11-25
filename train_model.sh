#!/bin/bash

chmod 777 models/model.tar.gz
docker run -v $(pwd):/app rasa/rasa:1.4.3-full train --domain config/domain.yml --data data --config config/config.yml --out models --fixed-model-name model
