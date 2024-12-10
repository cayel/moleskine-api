from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import json

with open('concerts.json', 'r') as f:
  concerts = json.load(f)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def healthcheck():
    return "<h1>All good!</h1>"

@app.get("/concerts", response_class=HTMLResponse)
def get_concerts():
  return JSONResponse(content=concerts)
 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
