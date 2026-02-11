
Running Python
- python app/main.py   
- curl http://127.0.0.1:{port}/value or health


Docker:
Ensure you are on the root dir
- docker build -t flask-web-api .  
- docker run -d -e WEB_API_PORT="$PORT1" -e WEB_API_VALUE="$value1" -p "$PORT1":"$PORT1" --name "$container1" flask-web-api

makeContainer:
.\makeContainers.sh
.\makeContainers.sh 7000 9000 "this is container 3" "this is container 4" "container3" "container4"


GitHub Actions please see the Repo,
For Branch Strategy, we have 2 workflows - 
development:  intended for PR reviews, this workflow must pass before a merge can occur.
              workflow has a small test that the must pass. 

main:         inteded for pushing the new image as latest into dockerHub

K8:
kubectl apply -f webApp.yaml    
then visit, http://localhost:30000/health






# docker pull galbrmanwraith/webapi:latest