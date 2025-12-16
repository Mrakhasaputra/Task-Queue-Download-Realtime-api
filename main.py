from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import router as api_router
import asyncio
from worker import worker


app = FastAPI(
    title="Task Queue API",
)


app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_status():
    return {"Status": "Active"}

@app.on_event("startup")
async def start_worker():
    asyncio.create_task(worker())

app.include_router(api_router, prefix="/api")