from fastapi import FastAPI , WebSocket , WebSocketDisconnect
from typing import List

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        pass

    def connect(self, websocket: WebSocket):
        pass

    def disconnect(self, websocket: WebSocket):
        pass

    def broadcast(self, message:str):
        pass

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            manager.broadcast(f"Message text was: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)