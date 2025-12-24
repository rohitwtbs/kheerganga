from fastapi import FastAPI , WebSocket , websocketdisconnect
from typing import List

class ConnectionManager:
    def __init__(self):
        pass

    def connect(self, websocket: WebSocket):
        pass

    def disconnect(self, websocket: WebSocket):
        pass

    def broadcast(self, message:str):
        pass