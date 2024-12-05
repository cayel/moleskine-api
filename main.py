#main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json

concerts = [
  {
    "id" :'1',
    "date": '2025-01-16',
    "bands": ['H-Burns'],
    "venue": 'Transbordeur',
    "city": 'Villeurbanne'
  }
]

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def healthcheck():
    return "<h1>All good!</h2>"

@app.get("/concerts", response_class=HTMLResponse)
def get_concerts():
  return json.dumps(concerts, indent=4, default=str)
 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)