from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = "b6e1129212951e2c500286d8f69c0028"

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/weather", response_class=HTMLResponse)
def get_weather(request: Request, city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data.get("cod") != 200:
        return templates.TemplateResponse("index.html", {"request": request, "error": data.get("message")})
    
    weather = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["description"]
    }
    return templates.TemplateResponse("index.html", {"request": request, "weather": weather})

@app.get("/api/weather")
def api_weather(city: str = Query(..., example="Manila")):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    return {
        "city": response["name"],
        "temperature": response["main"]["temp"],
        "description": response["weather"][0]["description"]
    }
