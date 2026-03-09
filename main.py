from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGOURI = os.getenv("MONGO_URI")
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


connectDB = MongoClient(f"{MONGOURI}/FastApi")


@app.get("/index", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = connectDB.notes.notes.find_one({})
    print(docs)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )