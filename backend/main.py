from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve the static files from the "out" directory
app.mount("/", StaticFiles(directory="static", html=True), name="static")