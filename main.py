from fastapi import FastAPI , websocket , websocketdisconnect
from typing import List

class ConnectionManager:
    def __init__(self):
        pass

    def connect(self, websocket: websocket):
        pass

    def disconnect(self, websocket:websocket):
        pass

    def broadcast(self, message:str):
        pass