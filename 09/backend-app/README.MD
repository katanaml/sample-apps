##  FastAPI and Oracle DB Client in Docker

# Commands

* docker-compose up --build
  * docker-compose up --build -d (in detached mode)

* docker images

* docker ps -a

* docker exec -it invoice-service /bin/bash

* docker-compose down

# API

* http://127.0.0.1:8001/api/v1/invoices/docs

# Environment variables in docker-compose.yml

* USERNAME=user
* PASSWORD=pass
* CONNECT_STRING=tcps://adb.eu-frankfurt-1.oraclecloud.com:1522/aaa_db_medium.adb.oraclecloud.com
