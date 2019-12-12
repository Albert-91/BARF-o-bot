# BARF-o-bot

This repo contains the BARF-o-bot sources based on Rasa framework. BARF-o-bot is a specialist in BARF dogs diet based on raw meat. Currently his abilities are:
*  calculating of products to buy, where input of this calculation is amount of meat,
*  calculating distribution of ingredients to make a portions,
*  getting weather data from Weatherstack API
*  smalltalk.

Chatbot's training data and responses are only in polish language.

If you want to try it then go to [Messenger](https://www.messenger.com/t/105119554259120).

## Procedures

For all credentials both for production and for development is used special file `.env` which is not tracked in repo. There are environment variables used in files like docker-compose.yml, credentials.yml and some actions.

### Training a model

Models are part of repo and must be stored in `models/` directory named `model.tar.gz` suffix.

#### Training model command (model will be generated as `models/model.tar.gz`): 
```bash
bash train_model.sh
```

### Deployment

Firstly make your node as a [swarm manager](https://docs.docker.com/engine/swarm/) by command:
```bash
docker swarm init
```

To deploy: 
  * BARF-o-bot service 
  * Custom action server
  * Duckling service
  * Postgres service

1. Run script to create directory for Postgres database and pull all necessary images and next override rasa-sk image
    ```bash
    bash prepare_env.sh
    ```
1. Fill in all credentials in .env file with all names of environments variables the same as below WITHOUT quotation marks:
    ```.env
    FACEBOOK_VERIFY=
    FACEBOOK_SECRET=
    FACEBOOK_PAGE_ACCESS_TOKEN=
    POSTGRES_DB=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    WEATHERSTACK_API_KEY=
    ```
1. Set Messenger Profile features like "Get Started" button, "Ice Breakers", "Greeting" and "Persistent Menu", setting content of these features in `config/settings.py` and enter command:
    ```bash
    python3 -m scripts.messenger_profile
    ```
1. Run stack named "barfobot":
   ```bash
   docker stack deploy -c docker-compose.yml barfobot
   ```
On screen should appear a message that four services was created.

## Deploy new version (update a chatbot with trained model via Docker on production)

1. Stop current stack
    ```bash
    docker stack rm barfobot
    ```
1. Run deploy script
    ```bash
    docker stack deploy -c docker-compose.yml barfobot
    ```
