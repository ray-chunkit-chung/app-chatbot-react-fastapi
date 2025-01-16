from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import api_router
import uvicorn

from dotenv import load_dotenv
import logging
import os

load_dotenv()

app = FastAPI()

environment = os.getenv("ENVIRONMENT", "prod")
logger = logging.getLogger("uvicorn")


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
)

# Import the API router
app.include_router(api_router, prefix="/api")

# Serve the static files from the "out" directory
url_path = "/"
static_files = "static"
logger.info(f"Mounting static files '{static_files}' at '{url_path}'")
app.mount(url_path, StaticFiles(directory=static_files, html=True), name="static")



if __name__ == "__main__":
    app_host = os.getenv("APP_HOST", "0.0.0.0")
    app_port = int(os.getenv("APP_PORT", "8000"))
    reload = True if environment == "dev" else False

    uvicorn.run(app="main:app", host=app_host, port=app_port, reload=reload)
