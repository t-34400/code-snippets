<h1>MEMO</h1>
個人的な注意点をまとめたメモ

# Android API
- LiveDataのvalueはobserverがいないと更新されない
- LiveDataにすでに値がセットされている場合，observerを登録すると即座にコールされる
- ランタイムの権限が必要かどうかは，API referenceのProtection levelを見れば良い（dangerousなら必要）

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
- [Unity.md](Unity.md)
 
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
