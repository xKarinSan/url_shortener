from fastapi import FastAPI
from fastapi.responses import JSONResponse,RedirectResponse
from pydantic import BaseModel
from uuid import uuid4
app = FastAPI()

class URLRequesBody(BaseModel):
    url: str

data = {}

@app.post("/shorten")
def set_id(body:URLRequesBody):
    
    unique_id = str(uuid4())[:7]
    data[unique_id] = body.url
    return JSONResponse(
        content={
        "id":unique_id
        }
    )

@app.get("/shortUrl/{id}")
def get_id(id:str):
    if id not in data:
        return JSONResponse(
            status_code=404,
            content={
                "message":"Not found!"

            }
        )
    return RedirectResponse(
        status_code=307,
        url=data[id]
    )
