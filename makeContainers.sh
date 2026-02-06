#!/usr/bin/env bash
docker build -t flask-web-api2 .
docker run -d -e WEB_API_PORT=8080 -e WEB_API_VALUE=container1 -p 8080:8080 --name container1 flask-web-api2    
docker run -d -e WEB_API_PORT=5000 -e WEB_API_VALUE=container2 -p 5000:5000 --name container2 flask-web-api2     
