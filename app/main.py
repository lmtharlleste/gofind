# app/main.py

from fastapi import FastAPI
from api.v1 import user_routes, auth_routes  # Certifique-se de que isso está correto

app = FastAPI()

router_prefix = "/api/v1"

app.include_router(user_routes.router, prefix=router_prefix)
app.include_router(auth_routes.router, prefix=router_prefix)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
