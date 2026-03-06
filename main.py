from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()

@app.get("/")

def read_root():
    html_content = "<h2>Hello FastApi</h2>"
    return HTMLResponse(content=html_content)