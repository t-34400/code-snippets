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
      　key = websocket.headers.get("key")

        async with sender_client_lock:
          　clients[client_id] = websocket
          　client_keys[client_id] = key

        async with receiver_client_lock:
            receiver_clients[client_id] = []
        

    try:
        while True:
            data = await websocket.receive_text()

            async with receiver_client_lock:
                

    except WebSocketDisconnect:
        async with sender_client_lock:
          　del clients[client_id]
          　del client_keys[client_id]

        async with receiver_client_lock:
            for receiver in receiver_clients[client_id]:
                receiver.close()
            
            del receiver_clients[client_id]


@app.websocket("/receive/{client_id}/{key}")
async def receive_endpoint(websocket: WebSocket, client_id: str, key: str):
    await websocket.accept()

    try:
        # クライアントIDとキーの検証
        if client_id in clients and client_keys.get(client_id) == key:
            # 正しい組み合わせの場合、接続を確立
            await websocket.send_text(f"Connected to the receiving endpoint.")
            
            # 送信側に接続確立の通知を送信
            send_websocket = clients.get(client_id)
            if send_websocket:
                await send_websocket.send_text(f"Receiver connected.")
            
            while True:
                # クライアントからのデータ受信
                data = await websocket.receive_text()
                
                # サーバー側の処理
                # ...

        else:
            # 正しくない組み合わせの場合、接続を拒否
            await websocket.close()

    except WebSocketDisconnect:
        # クライアントから切断された場合の処理
        pass

# IDリストを取得するエンドポイント
@app.get("/client_ids")
async def get_client_ids():
    return list(clients.keys())
