import cv2

# 入力動画ファイルパス
input_video_path = r'C:\Users\81907\Downloads\0.mp4'
# 出力動画ファイルパス
output_video_path = r'C:\Users\81907\Downloads\1.mp4'

# 削除する最初と最後の時間（秒）
start_time_to_delete = 2
end_time_to_delete = 28

# 解像度を設定
output_width = 640  # 新しい幅
output_height = 640  # 新しい高さ

# 入力動画を開く
cap = cv2.VideoCapture(input_video_path)

# 入力動画のプロパティを取得
fps = cap.get(cv2.CAP_PROP_FPS)

# 出力用の動画を設定
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (output_width, output_height))

# 削除する最初のフレームまでスキップ
cap.set(cv2.CAP_PROP_POS_MSEC, start_time_to_delete * 1000)

# ビデオを開始時間まで読み飛ばす
while cap.get(cv2.CAP_PROP_POS_MSEC) < start_time_to_delete * 1000:
    ret, frame = cap.read()

# 最初のフレームから終了時間までのフレームを書き込む
while cap.get(cv2.CAP_PROP_POS_MSEC) < end_time_to_delete * 1000:
    ret, frame = cap.read()
    if ret:
        # フレームの解像度を変更
        resized_frame = cv2.resize(frame, (output_width, output_height))
        out.write(resized_frame)

# キャプチャとアウトプットをリリース
cap.release()
out.release()
