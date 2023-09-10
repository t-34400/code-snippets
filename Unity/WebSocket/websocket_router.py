from fastapi import WebSocket
from fastapi.routing import WebSocketRoute
from fastapi.routing import APIRouter

from typing import Dict
import asyncio


router = APIRouter()

valid_api_key = "valid_api_key"

sender_clients: Dict[str, WebSocket] = {}
sender_client_keys: Dict[str, str] = {}
sender_client_lock = ayncio.Lock()

receiver_clients: Dict[str, List[WebSocket]] = {}
receiver_client_lock = ayncio.Lock()


@app.websocket("/send/{client_id}/")
async def send_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()

    if client_id in sender_clients:
      　await websocket.close()
      　return
      
    else:
      　key = websocket.headers.get("key", "")

        async with sender_client_lock:
          　clients[client_id] = websocket
          　client_keys[client_id] = key

        async with receiver_client_lock:
            receiver_clients[client_id] = []
        

    try:
        while True:
            data = await websocket.receive_text()

            async with receiver_client_lock:
                receivers = receiver_clients.get(client_id, [])

            for receiver in receivers:
                receiver.send_text(data)               

    except WebSocketDisconnect:
        async with sender_client_lock:
          　del clients[client_id]
          　del client_keys[client_id]

        async with receiver_client_lock:
            receivers = receiver_clients.get(client_id, [])
            del receiver_clients[client_id]

        for receiver in receivers:
            receiver.close() 
        
        

@app.websocket("/receive/{client_id}/")
async def receive_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    key = websocket.headers.get("key", "")

    try:
        async with sender_client_lock:
            if client_id in clients and client_keys.get(client_id) == key:
                send_websocket = clients.get(client_id)

                if send_websocket:
                    await send_websocket.send_text(f"Receiver connected.")
            else:
                await websocket.close()
                return
            
            async with receiver_client_lock:
                receivers = receiver_clients.get(client_id, [])
                receivers.append(websocket)
                receiver_clients[clients_id] = receivers

            while True:
                data = await websocket.receive_text()
                # do something


    except WebSocketDisconnect:
        if

@app.get("/client_ids")
async def get_client_ids():
    return list(clients.keys())
