# BARF-o-bot

This repo contains the BARF-o-bot sources based on Rasa framework. BARF-o-bot is a specialist in BARF dogs diet based on raw meat. Currently his abilities are:
*  calculating of products to buy, where input of this calculation is amount of meat,
*  calculating distribution of ingredients to make a portions,
*  smalltalk.

Chatbot's training data and responses are only in polish language.

If you want to try it then go to [Messenger](https://www.messenger.com/t/105119554259120).

## Procedures

For development, there are used special credentials files `dev.credentials.yml` that are not stored in repo - every developer shout maintain own versions (that keeps development messenger page credentials etc.). The same file is needed to create on production environment `prod.credentials.yml` and this file is also not stored in repo. The only file `credentials.yml` stored in repo is a template.

### Training a model

Development models is not part of repo and their contains `_dev` suffix. Production models are part of repo and must be stored in `models/` directory with `_prod` suffix.

#### Training development model command (model will be generated as `models/model_dev.tar.gz`): 
```bash
$ rasa train --data data --config config/config.yml --domain config/domain.yml --out models --fixed-model-name model_dev
```

#### Training production model command (model will be generated as `models/model_prod.tar.gz`): 
```bash
$ rasa train --data data --config config/config.yml --domain config/domain.yml --out models --fixed-model-name model_prod
```

### Deployment

Firstly make your node as a [swarm manager](https://docs.docker.com/engine/swarm/) by command:
```bash
docker swarm init
```

To deploy: 
  * BARF-o-bot service 
  * Custom action service
  * Duckling service

1. Override rasa-sdk image by command:
   ```bash
   docker build -t barfobot_actions:latest .
   ```
1. Run stack called "barfobot":
   ```bash
   docker stack deploy -c docker-compose-prod.yml barfobot
   ```
On screen should appear a message that three services was created.

## Deploy new version (update a chatbot with trained model via Docker on production)

1. Pull latest Rasa images and override rasa-sdk image
    ```bash
    bash update_rasa_images.sh
    ```
1. Stop current stack
    ```bash
    docker stack rm barfobot
    ```
1. Run deploy script
    ```bash
    docker stack deploy -c docker-compose-prod.yml barfobot
    ```
