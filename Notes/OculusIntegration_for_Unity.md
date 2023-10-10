# Oculus Integration
- 使い方
  - [Unity Asset Store](https://assetstore.unity.com/packages/tools/integration/oculus-integration-82022)からOculus Integrationをダウンロードし，プロジェクトにインポートする．
  - [Configure Unity Settings](https://developer.oculus.com/documentation/unity/unity-conf-settings/)に従って設定を行う．
  - [Getting Started with Interaction SDK](https://developer.oculus.com/documentation/unity/unity-isdk-getting-started/)に従ってカメラリグ等を設置する．
    - スティックで視点を動かしたい場合は，`OVRPlayerController` Prefabを利用する．
- Touchコントローラの入力の取得方法(以下は右コントローラのAボタン)．
  ```c#
  OVRInput.Get(OVRInput.Button.One, OVRInput.Controller.RTouch); // 押されている間はtrue
  OVRInput.GetDown(OVRInput.Button.One, OVRInput.Controller.RTouch); // 押したフレームでtrue
  OVRInput.GetUp(OVRInput.Button.One, OVRInput.Controller.RTouch); // 離したフレームでtrue
  ```

## トラブルシューティング
- 影がピクセレートされる
  - `Project Settings` > `Quality`の以下の項目を確認
    - `Shadow Distance`が非常に大きい値になっていないか
    - AndroidのデフォルトのLevelがMediumなどになっていないか

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
        - このままでは，指がオブジェクトを貫通してしまうので，以下の手順で`HandGrabVisual`を有効化する．
          - `OVRCameraRig`/`OVRInteraction`/`OVRControllerHands`/`LeftControllerHand`/`ControllerHandInteractors`/`HandGrabAPI`/`Visuals`/`HandGrabVisual`を有効化する．
          - `Synthetic Hand`に`OVRLeftHandSynthetic`をアタッチする．
          - 逆の手や，`OVRHands`についても同様の手順を行う．
    - Hover/Selectイベントを取得する場合は，`InteractableUnityEventWrapper`コンポーネントを使うと楽．
 
- Gesture Control
  - `OVRControllerHands`/`Left(Right)ControllerHand`/`ControllerHandFeaturesLeft(Right)`に必要なデータプロバイダコンポーネントをアタッチする
    - `Finger Feature State Provider`
      - 指の状態の判定を行いデータを供給する
      - Finger State Thresholdsに各指の閾値を設定する．
        - 基本的にはデフォルト値で良い（？）
          - Thumb: `DefaultThumbFeatureStateThresholds`
          - Index: `IndexFingerFeatuerStateThresholds`
          - Middle: `MiddleFingerFeatureStateThresholds`
          - Ring: `DefaultFingerFeatureStateThresholds`
          - Pinky: `DefaultFingerFeatureStateThresholds`
    - `TransformFeatureStateProvider`
      - 手の向きの判定を行いデータを供給する．
    - `JointDeltaProvider`
      - 手の関節のポーズの変化に関するデータを供給する．
    - データプロバイダを参照するオブジェクトをプレハブ化する際に，何度もアタッチするのが面倒なら，`...ProviderRef`コンポーネントをプレハブ側に用意し，プレハブ内からはこのRefコンポーネントを参照するようにする．
  - Active Stateを定義する．
    - `ShapeRecognizerActiveState`: 指の状態を指定するカスタムポーズを定義し，状態が一致したらtrue, しなかったらfalseを返す．
    - `TransformRecognizerActiveState`: 手の向きが指定したものであれば指定したbool値を返す．
      - TransformFeatureConfigsから判定を行う向きとbool値を指定
    - `JointVelocityActiveState`: 指定したジョイントの速度が指定した値以上であるときにtrueを返す．
    - `JointRotationActiveState`: 指定したジョイントの回転速度が指定した値以上であるときにtrueを返す．
    - `ActiveStateGroup`: 複数のActive Stateを同時に評価する(接続はAND, OR, XORから選択)．
    - `ActiveStateSelector`: 利用するActive Stateを指定
    - `SelectorUnityEventWrapper`: Selectorの状態が変化した際にUnityEventを発行する．
- 参考文献: [Oculus Hand Interaction: Pose detection](https://immersive-insiders.com/blog/oculus-hand-interaction-pose-detection)


## Haptic feedback
- 呼び出したいスクリプトのアセンブリに，Oculus.VRへの参照を追加する．
- 以下のメソッドでhapticを発生させる（半永続的に発生する）．
  ```c#
  OVRInput.SetControllerVibration(float frequency, float amplitude, OVRInput.Controller controllerMask);
  ```
- 一定時間経過で止めたい場合は，コルーチンなどを利用する．
  ```c#
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

## Movement SDK
- Oculus Linkを使いEditor上でトラッキングデータを使うには，Oculusアプリの`設定` > `ベータ`の`開発者ランタイムモード`をオンにする．
- BodyStateのPoseは，カメラリグのTracking Spaceからの相対位置で，Right-handed system?
    ```c#
    private void Update()
    {
        if(bodyTrackingDataManager.TryGetBodyTrackingData(out var bodyTrackingData))
        {
            var trackingSpacePosition = trackingSpace.transform.position;
            var trackingSpaceRotation = trackingSpace.transform.rotation;

            foreach(var (anchorObject, index) in anchorObjects.Select((anchorObject, index) => (anchorObject, index)))
            {
                var location = bodyTrackingData.locations.ElementAtOrDefault(index);
                anchorObject.transform.position = playerPosition + playerRotation * (location.position + location.orientation * cubeOffset);
                anchorObject.transform.rotation = playerRotation * location.orientation;
            }
        }
    }

    private bool TryGetBodyTrackingData(out BodyTrackingData bodyTrackingData)
    {
        var _bodyState = ovrBody?.BodyState;

        if(_bodyState == null)
        {
            bodyTrackingData = default!;
            return false;
        }

        var bodyState = _bodyState!.Value;

        var time = bodyState.Time;
        var confidence = bodyState.Confidence;

        var locations = bodyState.JointLocations.Select(location => 
            {
                var pose = location.Pose;
                return (ConvertVector3f(pose.Position), ConvertQuatf(pose.Orientation));
            })
            .ToList();

        bodyTrackingData = new(time, confidence, locations);
        return true;
    }

    private record BodyTrackingData(double time, float confidence, List<(Vector3 position, Quaternion orientation)> locations);
    
    private Vector3 ConvertVector3f(OVRPlugin.Vector3f vector)
    {
        return new Vector3(vector.x, vector.y, -vector.z);
    }

    private Quaternion ConvertQuatf(OVRPlugin.Quatf quat)
    {
        return new Quaternion(quat.x, quat.y, -quat.z, -quat.w);
    }    
    ```
    
