import os.path as osp
import argparse
import cv2
from tqdm import tqdm

def main(args):
    cap = cv2.VideoCapture(args.video_path)
    
    fps_vid = cap.get(cv2.CAP_PROP_FPS)
    frame_skip = round(fps_vid / args.target_fps)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    filename = osp.basename(args.video_path).split('.')[0]
    for extracted_frame_count, frame_index in enumerate(tqdm(range(0, frame_count, frame_skip))):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_file = osp.join(args.output_dir_path, f'{filename}_{extracted_frame_count:04d}.jpg')
        cv2.imwrite(frame_file, frame)

    cap.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--video_path')
    parser.add_argument('--output_dir_path', default=None)
    parser.add_argument('--target_fps', type=int)

    args = parser.parse_args()
    main(args)
