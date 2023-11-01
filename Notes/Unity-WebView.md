# [unity-webview](https://github.com/gree/unity-webview/tree/de540e922510a134291ace77462debfc7a3355d3)

## 使い方
1. Unityのプロジェクトを作成する
2. プロジェクトフォルダの`Packages/manifest.json`を開く（エディタ上ではなくエクスプローラから）．
3. dependenciesに以下を追加
     ```json
     {
       "dependencies": {
         ...
           "net.gree.unity-webview": "https://github.com/gree/unity-webview.git?path=/dist/package",
         ...
       }
     }
     ```
4. GitHubのREADMEに従って，プラットフォームごとに実装する．



