#!/bin/bash
export PORT=80
docker pull searx/searx
docker run --rm -d -v ${PWD}/.searx:/etc/searx -p $PORT:8080 -e BASE_URL=http://localhost:$PORT/ searx/searx
