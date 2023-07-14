# Oculus Integration
- 使い方
  - [Unity Asset Store](https://assetstore.unity.com/packages/tools/integration/oculus-integration-82022)からOculus Integrationをダウンロードし，プロジェクトにインポートする．
  - [Configure Unity Settings](https://developer.oculus.com/documentation/unity/unity-conf-settings/)に従って設定を行う．
  - [Getting Started with Interaction SDK](https://developer.oculus.com/documentation/unity/unity-isdk-getting-started/)に従ってカメラリグ等を設置する．
    - スティックで視点を動かしたい場合は，`OVRPlayerController` Prefabを利用する．
- Touchコントローラの入力の取得方法(以下は右コントローラのAボタン)．
  ```cshirp
  OVRInput.Get(OVRInput.Button.One, OVRInput.Controller.RTouch); // 押されている間はtrue
  OVRInput.GetDown(OVRInput.Button.One, OVRInput.Controller.RTouch); // 押したフレームでtrue
  OVRInput.GetUp(OVRInput.Button.One, OVRInput.Controller.RTouch); // 離したフレームでtrue
  ```

## Interaction SDK
- [Create Grab Interactions](https://developer.oculus.com/documentation/unity/unity-isdk-create-hand-grab-interactions/)に従ってGrab interactionを設定する．
    - Grabbableは，グラブできるオブジェクトに設定する．
        - 非Kinematicなオブジェクトに，グラブ中の物理演算を適用する場合は[`PhysicsGrabbable`](https://developer.oculus.com/documentation/unity/unity-isdk-using-with-physics/#physicsgrabbable)を使う
        - `One Grab Transformer`, `Two Grab Transformer`オプションで，片手グラブ，両手グラブした際の挙動を設定できる．
        - `One Grab Translate Transformer`: 片手でグラブした際に，Positionの移動ができる．
        - `One Grab Rotate Transformer`:　片手でグラブした際に，オブジェクトを回転できる．
        - `One Grab Free Transformer`: 片手でグラブした際に，オブジェクトを移動，回転，スケールできる．
        - `Two Grab Rotate Transformer`: 両手でグラブした際に，オブジェクトを回転できる．
        - `Two Grab Plane Transformer`: 両手でグラブした際に，平面上でオブジェクトを移動，回転，スケールできる．
        - `Two Grab Free Transformer`: 両手でグラブした際に，オブジェクトを移動，回転，スケールできる．
        - いずれもパラメータは制約できる．
        - `One Grab Transformer`を`None`にすると，両手でグラブするまで動かなくなる．
        - `Two Grab Transformer`に`One Grab *** Transformer`を設定することもできる（この場合，両手でグラブした際に，最初にグラブした片手で`One Grab *** Transformer`の挙動をする）．
    - `(Hand) Grab Interactable`は，グラブするポイントに設定する．
        - Grab Poseを設定したい場合，`Hand Grab Interactable`は，[Create a Hand Grab Pose (PC)](https://developer.oculus.com/documentation/unity/unity-isdk-creating-handgrab-poses/)に従って設定するのが楽．
            - HMDとQuest Linkで接続する． 
            - メニューバーから`Oculus` > `Interaction` > `Hand Grab Pose Recorder`を選択する．
            - `Hand used for recording poses`に`Left Hand`(Controllers as handsを使う場合は，`Left Controller hand`)を設定する．
            - `GameObject to record the hand grab poses for`にGrab Poseを設定したいオブジェクトを設定する．
            - プレイモードに入り，**Unity Editorのゲーム画面をクリックしてから**，設定したいPoseに手の形を変えた上でスペースキーを押す（`Hand Grab Pose Recorder`ウィンドウでは，ウィンドウにフォーカスするように書いてあるが，上手くいかなかった）．
                - 一度にいくつでもレコード可能． 
            - プレイモードを抜ける前に，Save To Collectionを押す．
            - プレイモードを抜けて，Load From Collectionを押す．
            - これにより，`HandGrabInteractable`が自動で追加される．
            - 逆の手を追加したい場合は，`HandGrabInteractable`の`Hand Grab Interactable`の`Create Mirrored HandGrabInteractable`をクリックするか，同じ手順で逆の手も設定する．
    - Hover/Selectイベントを取得する場合は，`InteractableUnityEventWrapper`コンポーネントを使うと楽． 
         
## Haptic feedback
- 呼び出したいスクリプトのアセンブリに，Oculus.VRへの参照を追加する．
- 以下のメソッドでhapticを発生させる（半永続的に発生する）．
  ```cshirp
  OVRInput.SetControllerVibration(float frequency, float amplitude, OVRInput.Controller controllerMask);
  ```
- 一定時間経過で止めたい場合は，コルーチンなどを利用する．
  ```cshirp
  public static IEnumerator TriggerHapticFeedback(float duration, float frequency, float amplitude, OVRInput.Controller controller)
  {
    OVRInput.SetControllerVibration(frequency, amplitude, controller);

    yield return new WaitForSeconds(duration);

    OVRInput.SetControllerVibration(0, 0, controller);
  }
  ```
- 明示的に止めなかった場合は，２秒後に自動で止まる．
- [サンプルクラス](../Unity/Oculus/VibrationWrapper.cs)

## Face tracking
- Package Managerの`Add package from git URL`を選択し，以下のURLを追加する．
    - https://github.com/oculus-samples/Unity-Movement.git
- 
