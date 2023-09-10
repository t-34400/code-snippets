from fastapi import FastAPI
from websocket_router import router as websocket_router

app = FastAPI()
app.include_router(websocket_router)
