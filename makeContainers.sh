#!/usr/bin/env bash

#Logging for script.
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>make-container-log.out 2>&1

PORT1="${1:-8080}"
PORT2="${2:-5000}"
value1="${3:-"This is Container1"}"
value2="${4:-"This is Container2"}"
container1="${5:-container1}"
container2="${6:-container2}"


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
echo "Built Image"

docker run -d -e WEB_API_PORT="$PORT1" -e WEB_API_VALUE="$value1" -p "$PORT1":"$PORT1" --name "$container1" flask-web-api  
echo "Built Container: " + $container1  
docker run -d -e WEB_API_PORT="$PORT2" -e WEB_API_VALUE="$value2" -p "$PORT2":"$PORT2" --name "$container2" flask-web-api  
echo "Built Container: " + $container2   
