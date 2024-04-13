DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker-compose.yaml
APP_CONTAINER = fastapi_backend


.PHONY: up
up:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: logs
logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: shell
shell:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: down
down:
	${DC} -f ${APP_FILE} down
