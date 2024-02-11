from fastapi import FastAPI
from quiz import core, api

app = FastAPI(title=core.settings.title)

# TODO: remove russian comments
# TODO: black + isort everything in project
# Подключение роутера с эндпоинтами
app.include_router(api.urls.api_v1_router)  #
