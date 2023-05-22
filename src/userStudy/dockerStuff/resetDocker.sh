docker stop server

docker rm server

docker rmi ubuntu-openssh

docker build -t ubuntu-openssh .

ssh-keygen -f "$HOME/.ssh/known_hosts" -R "[localhost]:2222"

docker run -d -p 2222:22 --name server ubuntu-openssh