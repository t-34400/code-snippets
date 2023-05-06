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