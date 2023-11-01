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

# Meta Questアプリ上のWorld Spaceに表示する(パフォーマンスは度外視)

1. Oculus Integrationをインストールし，[初期設定](https://developer.oculus.com/documentation/unity/unity-tutorial-hello-vr/)する．
2. 生成された`Assets/Plugins/Android/AndroidManifestJson.xml`の以下の部分を書き換える(パッケージ名，クラス名は任意)．
     ```XML
     <!-- android:name="com.unity3d.player.UnityPlayerActivity" -->
     android:name="com.unity3d.player.YourUnityPlayerActivity"
     ```
     生成されていない場合は，`Project Settings` > `Player` > `Publishing Settings` > `Build` > `Custom Main Manifest`にチェックを入れる．
4. `Plugins/Android`にYourUnityPlayerActivity.javaを作成し，次のように入力する，
   ```java
   // This code is largely borrowed from CUnityPlayerActivity.java in gree/unity-webview.
   // https://github.com/gree/unity-webview/blob/de540e922510a134291ace77462debfc7a3355d3/plugins/Android/webview/src/main/java/net/gree/unitywebview/CUnityPlayerActivity.java
     
   package com.unity3d.player;
     
   import net.gree.unitywebview;
   import com.unity3d.player.*;
   import android.os.Bundle;
     
   public class YourUnityPlayerActivity
       extends UnityPlayerActivity
   {
       @Override
       public void onCreate(Bundle bundle) {
           requestWindowFeature(1);
           super.onCreate(bundle);
           getWindow().setFormat(2);
           mUnityPlayer = new CUnityPlayer(this);
           setContentView(mUnityPlayer);
           mUnityPlayer.requestFocus();
       }
   }
   ```
6. unity-webviewをカスタムパッケージ化する．
   - Plugins/unity-webviewを右クリックし`Show in Explorer`を選択する．
   - `net.gree.unity-webview@...`をプロジェクト直下のPackagesにコピーし，末尾のバージョン情報を削除する．
   - 
8. 



