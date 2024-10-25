#main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def healthcheck():
    return "<h1>All good!</h2>"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)