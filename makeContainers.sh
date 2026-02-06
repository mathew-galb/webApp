#!/usr/bin/env bash

#Logging for script.
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>make-container-log.out 2>&1


#Exit on Error
set -e

#Check if Docker is present.
if ! command -v docker; then
    echo "Docker is not installed."
    exit 1
fi

#Check if Dockerfile is present on directory
if ! test -f ./Dockerfile; then
  echo "Dockerfile does not exist"
  exit 1
fi



docker build -t flask-web-api .
docker run -d -e WEB_API_PORT=8080 -e WEB_API_VALUE=container1 -p 8080:8080 --name container1 flask-web-api    
docker run -d -e WEB_API_PORT=5000 -e WEB_API_VALUE=container2 -p 5000:5000 --name container2 flask-web-api     
