# RabbitMQ RPC with FastAPI

Sample app with FastAPI endpoint. RabbitMQ is used as a postman to deliver and return message between endpoint API and backend. Backend code could run on different microservice. Multiple backends can be started for scalability.

RabbitMQ logic is based on official example [Remote procedure call (RPC)](https://www.rabbitmq.com/tutorials/tutorial-six-python.html)

## Commands

* Start backend (you can start multiple instances)
  * **python rpc_server.py**
* Start FastAPI endpoint (from rabbitmq-web folder)
  * **uvicorn endpoint:app --reload**


API url: http://127.0.0.1:8000/api/v1/fibonacci/docs
