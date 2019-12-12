#!/bin/bash

DB_DIR_NAME=db_storage

if [[ -d "$DB_DIR_NAME" ]]; then
    echo "$DB_DIR_NAME directory exists."
else
    mkdir $DB_DIR_NAME
    echo "$DB_DIR_NAME directory created."
fi

ENV_FILE_NAME=.env
if [ -f "$ENV_FILE_NAME" ]; then
    echo "$ENV_FILE_NAME file exists"
else
    touch $ENV_FILE_NAME
    echo "$ENV_FILE_NAME file created"
fi
