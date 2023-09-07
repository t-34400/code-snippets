# サーバーのセットアップ

- FastAPI, WebSocketsを環境にインストール
  ```bash
  pip install fastapi uvicorn websockets
  ```
- エンドポイントを作成
  ```python
  # main.py
  
  from fastapi import FastAPI
  from websocket_router import router as websocket_router

  app = FastAPI()
  app.include_router(websocket_router)
  ```
  ```python
  # websocket_router.py

  import asyncio

  from fastapi import WebSocket
  from fastapi.routing import WebSocketRoute
  from fastapi.routing import APIRouter
  import websockets

  # Use OAuth2, etc. when higher security is required.
  valid_api_key = "valid_api_key"

  
  router = APIRouter()


  receiving_clients = set()
  receiving_clients_lock = asyncio.Lock()
    
  @app.websocket("/ws")
  async def websocket_endpoint(websocket: websockets.WebSocket):
    api_key = websocket.headers.get("api-key")
    if not api_key or api_key != valid_api_key:
      await websocket.close()
      return
  
    await websocket.accept()

    async with receiving_clients_lock:
        receiving_clients.add(websocket) 
  
    try:
      while True:
        data = await websocket.receive_text()

        message_type = message.get("type")
        if message_type == "transform":
          # validation
          async with connected_clients_lock:
            for client in connected_clients:
              await client.send_text(data)
    
    except:
      connected_clients.remove(websocket)
      await ws.close()
  ```

# クライアントUnityプロジェクトにWebSocket-sharpを追加
- [WebSocket-sharp](https://github.com/sta/websocket-sharp)をダウンロード
- websocket-sharpディレクトリをリリースビルドしてDLLを生成し，UnityのAssets内に配置
- 適宜アセンブリ参照を追加

# クライアント側の処理を実装
- 接続を確立し，リスナーを登録
  ```c#
  using WebSocketSharp;

  var ws = new WebSocket("ws://localhost:8000/ws");
  ws.SetCookie(new Cookie("api-key", "valid_api_key"));

  ws.OnOpen += (sender, e) =>
  {
      // ...
  }
  ws.OnError += (sender, e) =>
  {
      // ...
  }
  ws.OnClose += (sender, e) =>
  {
      // ...
  }

  // Receive
  ws.OnMessage += (sender, e) => {
      var data = e.Data;
      // ...
  };
  
  ws.Connect();

  //　Send
  var data = new DataClass(
      type: "transform",
      position: new { x = 1.0, y = 2.0, z = 3.0 },
      rotation: new { x = 0.0, y = 90.0, z = 0.0 }
  );
  var jsonData = JsonUtility.ToJson(data);
  ws.Send(jsonData);

  ws.Close();
  ```
- Unityの多くのAPIはメインスレッドでのみ適切に動作するため，データを受信した際に基本的にはメインスレッドに返す必要がある．
  ```c#
  using System.Collections.Generic;
  using WebSocketSharp;

  var ws = new WebSocket("ws://localhost:8000/ws");
  private Queue<string> receivedMessageQueue = new();

  ws.OnMessage += (sender, e) =>
  {
    messageQueue.Enqueue(e.Data);
  };

  ws.Connect();


  // MonoBehaviour
  private void Update()
  {
      while (messageQueue.Count > 0)
      {
          var data = messageQueue.Dequeue();
          var parsedData = JsonUtility.FromJson<DataClass>(data);

          // ...
      }      
  }
  ```
