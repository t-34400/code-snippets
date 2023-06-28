<h1>MEMO</h1>
個人的な注意点をまとめたメモ

# Android API
- LiveDataのvalueはobserverがいないと更新されない
- LiveDataにすでに値がセットされている場合，observerを登録すると即座にコールされる

# Blender
- multiprocessingモジュールで並列処理はできるが，sys.pathの問題で，メインプロセス以外のBlender APIモジュールのimportに失敗する．
    - 対処法としては，メインプロセスでのみBlender APIモジュールのimportを行うようにする
        ```Python
        from multiprocessing import current_process

        if current_process().name == 'MainProcess':
            import bpy
        ```
    - ただし，当然のことながら，サブプロセスではBlender APIを利用できない．
    - 
# Python
- Windowsでpytorch3dのインストールに失敗する問題
    - version
        - torch 2.1.0.dev20230420+cu118
        - torchvision 0.16.0.dev20230420+cu118
    - git clone https://github.com/facebookresearch/pytorch3d.git
    - [cub](https://github.com/NVIDIA/cub/releases)からCUB 1.17.1をダウンロードして展開
    - pytorch3dディレクトリ直下のconfig.hの#ifndef THRUST_IGNORE_CUB_VERSION_CHECKの行の前にTHRUST_IGNORE_CUB_VERSION_CHECKを定義して，ifnブロックが実行されないようにする．
        ```c
        #define THRUST_IGNORE_CUB_VERSION_CHECK
        #ifndef THRUST_IGNORE_CUB_VERSION_CHECK
        ```
    - pytorch3dディレクトリ直下のsetup.pyの以下の部分を変更
        ```cpp
        // extra_compile_args = {"cxx": ["-std=c++14"]} ->
        extra_compile_args = {"cxx": []}
        ```
    - x64 Native Tools Command Prompt for VS 2022から以下の操作を行う
    - where clでclにパスが通っていることを確認する．
    - 変数を定義
        - set PYTORCH3D_NO_NINJA=1
        - set DISTUTILS_USE_SDK=1
        - set CUB_HOME=[展開したcub-1.17.1のパス]
    - Pythonの環境をactivate
        - env\scripts\activate
    - cd [pytorch3dのパス]
    - py setup.py install

# PyTorch
- CrossEntropyLossを計算する前に，Softmaxをかけない．
    - PyTorchのCrossEntropyLossは内部でSoftmaxをかけているので，学習の効率が悪化する．

# Unity
- Nullableを有効にする．
    - Project settings > Player > Other settingsのAdditional Compiler Argumentsに以下を追加する．
        - -nullable:enable
    - アセンブリ単位で有効化するには，asmdefファイルと同じディレクトリに.rspファイルを作成し，以下を記述する．
        - -nullable:enable
    - SerializeFieldは，null非許容なので初期値を与えないと警告が出る．
        - GameObjectなどの場合は，default!を代入しておく？
- APIなどにVS CodeのIntelliSenseを効かせる．
    - Preference > External ToolsのGenerate.csprojの下のチェックボックスにチェックを入れる．
    - VS Code上でCtrl+Shift+Pを押して，Develoer: Reload Windowを選択して実行する．
    - .NET Framework 4.7.1アセンブリへの参照エラーが発生する場合は，[Download .NET Framework 4.7.1](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net471)からDeveloper Packをインストールする．
- Barracudaは，パッケージマネージャにはデフォルトで表示されない．
    - 左上の＋ボタンから，Add package from git URLを選び，com.unity.barracudaと入力する．
- XR
    - インストール
        - Package Managerから`XR Interaction Toolkit`と`XR Plugin Management`をインストールする．
            - XR Interaction Toolkit: v2.4.0
            - XR Plugin Management: v4.2.1
        - Package Managerを開き，`XR Interaction Toolkit`のSamplesタブからStarter Assets（デバイスなしでテストしたいならXR Device Simulatorも）をインポートする．
        - Project SettingsのXR Plug-in Managementタブのプロバイダを選択する．
    - シーン
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

- [Oculus Lipsync SDK](https://developer.oculus.com/downloads/package/oculus-lipsync-unity)
    - SDKをダウンロードして展開する．
    - メニューバーの`Assets` > `Import package` > `Custom package`を選択して，展開したファイルに含まれている.unitypackageファイルを開き，インポートする．
    - 適当なゲームオブジェクトに`OVR Lip Sync Context`と`OVR Lip Sync context Morph Target`をアタッチする．
    - `OVR Lip Sync Context`の`Audio Source`，`OVR Lip Sync context Morph Target`の`Skinned Mesh Renderer`に適当なオブジェクト/コンポーネントをアタッチする．
 
# Amazon Fire Tablet
- TTS(Text to speech)のエンジンをデフォルトエンジンから変更する．
    - Google Play Storeをインストールして，Speech Service by Googleを導入しておく
    - USB debuggingを有効にする．
    - ADB shellから以下のコードを入力
      ```
      settings put secure tts_default_synth com.google.android.tts
      ```
    - スピードを変更する場合は，以下のコマンドを入力
      ```
      settings put secure tts_default_rate [rate(default=100)]
      ```
    - 音声がインストールされていない場合や音声を変更する場合は，Activity Launcherなどを使って，Speech Serviceの設定画面を開きインストールする．
