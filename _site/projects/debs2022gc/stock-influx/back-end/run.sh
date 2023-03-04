#!/usr/bin/env bash

# local ip: localhost:8080
# prod ip: 172.16.238.11:8080

# Run InfluxDB and Server
docker-compose up -d

for retry_count in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
  response=$(curl -s http://localhost/actuator/health)
  up_count=$(echo $response | grep 'UP' | wc -l)

  if [ $up_count -ge 1 ]
  then
      echo ">>> Success Health check"
      echo "RUN SUCCESSFULLY"
      echo ">>> Start Data inserting from Google Drive"
      curl -s -X POST "http://localhost/v1/api/data" -H "accept: application/json;charset=UTF-8" &
      break
  else
      echo ">>> Health check status doesn't contain 'UP'."
  fi

  if [ $retry_count -eq 10 ]
  then
    echo ">>> Fail Health check. Exit program."
    sudo docker-compose down
    exit 1
  fi

  echo ">>> Fail Health check. Retry... ($retry_count / 20)"
  sleep 10
done