from fastapi import FastAPI

from api.routers import all_routers


app = FastAPI(
    title="Сайт со сборками Rimworld",
    version="0.0.1",
)


for router in all_routers:
    app.include_router(router)
