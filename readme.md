# API сервис для добавления/получения/обновления/удаления счетов на Python3.8 and FastAPI

## Как запустить

Run

````
$ docker-compose up -d --build
````

Документация по работе с API http://127.0.0.1:8002/docs

## Как запустить тесты

````
$ python -m pytest app/tests
````
или

````
$ docker-compose exec app python -m pytest app/tests
````
