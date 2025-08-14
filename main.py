from fastapi import FastAPI
from utils.util import load_json
from utils.endpoints import router as endpoints_router
import uvicorn

app = FastAPI()

app.include_router(endpoints_router)

if __name__ == "__main__":
    conf = load_json()
    uvicorn.run("main:app", host=conf["ip"], port=5678, reload=True)
    