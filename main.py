from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>私のホームページ</title>
        </head>
        <body>
            <h1>ようこそ！</h1>
            <p>これは私のページです。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present: str):
    return {"response": f"ありがとう！{present}めっちゃ嬉しい！お返しはラーメンです。"}