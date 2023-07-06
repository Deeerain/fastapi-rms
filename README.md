<h1>Система управления записью</h1>

## Система управления записью на разные виды услуг

## Запуск:

### Клонируем репозиторий:

`git clone https://github.com/Deeerain/fastapi-rms.git`

`cd ./fastapi-rms`

### Создаем и активируем виртуальное окружение:

`python3.10 -m venv env`

`source ./env/bin/activate`

### Устанавливаем зависимости

`pip install -r ./backend/requirements.txt`

### Запускаем:

`docker-compose -f ./docker-compose.dev.yaml -d`

или

`make run-dev`

### Применяем миграции

`docker-compose -f ./docker-compose.dev.yaml exec backend alembic upgrade head `