# Unity

## Nullable
- Project settings > Player > Other settingsのAdditional Compiler Argumentsに以下を追加する．
    - -nullable:enable
- アセンブリ単位で有効化するには，asmdefファイルと同じディレクトリに.rspファイルを作成し，以下を記述する．
    - -nullable:enable
- SerializeFieldは，null非許容なので初期値を与えないと警告が出る．
    - GameObjectなどの場合は，default!を代入しておく？

## VS CodeのIntelliSense．
- Preference > External ToolsのGenerate.csprojの下のチェックボックスにチェックを入れる．
- VS Code上でCtrl+Shift+Pを押して，Develoer: Reload Windowを選択して実行する．
- .NET Framework 4.7.1アセンブリへの参照エラーが発生する場合は，[Download .NET Framework 4.7.1](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net471)からDeveloper Packをインストールする．
 
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

# [Oculus Lipsync SDK](https://developer.oculus.com/downloads/package/oculus-lipsync-unity)
- SDKをダウンロードして展開する．
- メニューバーの`Assets` > `Import package` > `Custom package`を選択して，展開したファイルに含まれている.unitypackageファイルを開き，インポートする．
- 適当なゲームオブジェクトに`OVR Lip Sync Context`と`OVR Lip Sync context Morph Target`をアタッチする．
- `OVR Lip Sync Context`の`Audio Source`，`OVR Lip Sync context Morph Target`の`Skinned Mesh Renderer`に適当なオブジェクト/コンポーネントをアタッチする．
