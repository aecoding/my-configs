export PORT=80
sudo docker pull searx/searx
sudo docker run --rm -d -v ${PWD}/.searx:/etc/searx -p $PORT:8080 -e BASE_URL=http://localhost:$PORT/ searx/searx
