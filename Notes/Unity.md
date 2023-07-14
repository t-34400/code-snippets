# Unity

## 一般
- 一定の条件下でコンポーネントのイベント関数を有効化するには，enabledを変更するのがよい．
  ```cshirp
  gameObject.GetComponent<Hoge>().enabled = false;
  ```

## Nullable
- Project settings > Player > Other settingsのAdditional Compiler Argumentsに以下を追加する．
    - -nullable:enable
- アセンブリ単位で有効化するには，asmdefファイルと同じディレクトリに.rspファイルを作成し，以下を記述する．
    - -nullable:enable
- SerializeFieldは，null非許容なので初期値を与えないと警告が出る．
    - GameObjectなどの場合は，default!を代入しておく？
 
## Tests
- テスト用のasmdefは，以下のように設定する．
  - `Override References`にチェックを入れる
  - `Assembly　Definition　References`に`UnityEditor.TestRunner`と`UnityEngine.TestRunner`を指定する．
  - `Assembly References`に`nunit.framework.dll`を指定する．
- Internalなクラスをチェックするには，公開元のasmdefと同じディレクトリに以下を記述したcsファイルを配置する．
  ```cshirp
  using System.Runtime.CompilerServices;
  [assembly: InternalsVisibleTo("[公開先のアセンブリ名]")]
  ```

## VS CodeのIntelliSense．
- Preference > External ToolsのGenerate.csprojの下のチェックボックスにチェックを入れる．
- VS Code上でCtrl+Shift+Pを押して，Develoer: Reload Windowを選択して実行する．
- .NET Framework 4.7.1アセンブリへの参照エラーが発生する場合は，[Download .NET Framework 4.7.1](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net471)からDeveloper Packをインストールする．

## ScriptableObject
- 次のようなスクリプトを作成する．
  ```cshirp
  using UnityEngine;

  [CreateAssetMenu]
  class SampleScriptableObject: ScriptableObject
  {
    //
  }
  ```
- プロジェクトウィンドウのCreateメニューに`SampleScriptableObject`が現れるので，これを選択してアセットを生成する．
- このオブジェクトをSerializeFieldにアタッチして使用する．

## Baraccuda
- Barracudaは，パッケージマネージャにはデフォルトで表示されない．
    - 左上の＋ボタンから，Add package from git URLを選び，com.unity.barracudaと入力する．

## XR

### インストール
- Package Managerから`XR Interaction Toolkit`と`XR Plugin Management`をインストールする．
    - XR Interaction Toolkit: v2.4.0
    - XR Plugin Management: v4.2.1
- Package Managerを開き，`XR Interaction Toolkit`のSamplesタブからStarter Assets（デバイスなしでテストしたいならXR Device Simulatorも）をインポートする．
- Project SettingsのXR Plug-in Managementタブのプロバイダを選択する．

### 設定
- Project settingsのQualityタブから，Shadow distanceを小さくしておく．

### シーン
- 既存のカメラやイベントシステムを削除しておく．
- プレイヤーオブジェクトを作成
    - Starter AssetsのPrefabsに入っている`Complete XR Origin Set Up`を使うのが手っ取り早い．
    - シーン上に`Input Action Manager`と`InteractionManager`を追加する．
    - プレイヤーオブジェクトに`XR Origin`をアタッチする．
    - コントローラオブジェクトに`XR Controller`を追加する．
    - コントローラで相互作用を起こす場合は，`XR ** Interactor`を追加する．
- Interactorイベントを発生させるInteractorを任意のオブジェクトに追加する．
    - AR Gesture Interactor
    - XR Direct Interactor
    - XR Poke Interactor
    - XR Ray Interactor
    - XR Socket Interactor
- イベントを受信するInteractableを任意のオブジェクトに追加する．
    - XR Grab Interactable
    - XR Simple Interactable
- デバイスから入力を受けるUIのキャンバスに，`Tracked Device Graphic Raycaster`を追加する．
- Reference: [Components | XR Interaction Toolkit | 2.3.0-pre.1 ](https://docs.unity.cn/Packages/com.unity.xr.interaction.toolkit@2.3/manual/components.html)

### XR Hands

### Quest Pro
- [Meta Quest Developer Hub](https://developer.oculus.com/documentation/unity/ts-odh/)をインストールする．
    - デバイスを接続し，Developer modeを有効化する．
- ビルド設定は[公式の解説](https://developer.oculus.com/documentation/unity/unity-conf-settings/)を参照．
    - Unity 2022.3.2f1では，以下の部分が記述時の説明と異なった．
        - `Low Overhead Mode`が，Project Settingsの`XR Plug-in Management` > `Oculus`に移動している．
        - `Texture Quality`が，`Quality` > `Textures` > `Global Mipmap Limit`に変更されている．
- Compute Shaderを使う場合は以下の点に注意する．
    - float型のサイズに注意する．
        - `RenderTexture`を使う場合は，フォーマットを`RenderTextureFormat.ARGBFloat`にする．
    - Compute Shaderは，OpenGL ES 3.1以降しか対応していないため，Player SettingsのRequire ES3.1にチェックを入れる．

# [Oculus Lipsync SDK](https://developer.oculus.com/downloads/package/oculus-lipsync-unity)
- SDKをダウンロードして展開する．
- メニューバーの`Assets` > `Import package` > `Custom package`を選択して，展開したファイルに含まれている.unitypackageファイルを開き，インポートする．
- 適当なゲームオブジェクトに`OVR Lip Sync Context`と`OVR Lip Sync context Morph Target`をアタッチする．
- `OVR Lip Sync Context`の`Audio Source`，`OVR Lip Sync context Morph Target`の`Skinned Mesh Renderer`に適当なオブジェクト/コンポーネントをアタッチする．

