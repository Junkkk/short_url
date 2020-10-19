import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/redirect")
async def read_url():
    response = RedirectResponse("https://typer.tiangolo.com")
    return response

@app.post("/redirect")
async def create_short_url():
    

if __name__ == '__main__':
    uvicorn.run(app)