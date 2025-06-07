from fastapi import FastAPI
import uvicorn
from url_shortener import URLShortener
from pydantic import BaseModel
app = FastAPI()

class URL(BaseModel):
    value: str

@app.post("/api/v1/shorten")
async def shorten(url: URL):
    original_url = url.value
    shortened_url = url_shortener.shorten(original_url)
    return {
        "shortened_url": shortened_url
    }

@app.post("/api/v1/recover")
async def recover(url: URL):
    shortened_url = url.value
    original_url = url_shortener.recover(shortened_url)
    return {
        "original_url": original_url
    }

if __name__ == '__main__':
    url_shortener = URLShortener()
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
