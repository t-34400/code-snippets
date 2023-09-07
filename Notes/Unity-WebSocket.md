# サーバーのセットアップ

- FastAPI, WebSocketsを環境にインストール
  ```bash
  pip install fastapi uvicorn websockets
  ```
- エンドポイントを作成
  ```python
  # main.py
  
  from fastapi import FastAPI
  import websockets

  app = FastAPI()

  @app.websocket("/ws")
  async def websocket_endpoint(websocket: websockets.WebSocket):
    await websocket.accept()
    try:
      while True:
        data = await websocket.receive_text()
    except;
      await ws.close()
  ```

# クライアントUnityプロジェクトにWebSocket-sharpを追加
- [WebSocket-sharp](https://github.com/sta/websocket-sharp)をダウンロード
- websocket-sharpディレクトリをリリースビルドしてDLLを生成し，UnityのAssets内に配置
- 適宜アセンブリ参照を追加

# クライアント側の処理を実装
- 接続を確立し，リスナーを登録
  ```cshirp
  using WebSocketSharp;

  WebSocket ws = new WebSocket("ws://localhost:8000/ws");

  // 受信処理
  ws.OnMessage += (sender, e) => {
      string data = e.Data;
      ParseAndApply(data);
  };
  
  ws.Connect();

  //　送信処理
  var data = new {
      position = new { x = 1.0, y = 2.0, z = 3.0 },
      rotation = new { x = 0.0, y = 90.0, z = 0.0 }
  };
  string jsonData = JsonUtility.ToJson(data);
  ws.Send(jsonData);
  ```
