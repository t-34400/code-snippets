import os.path as osp
import argparse
from glob import glob
from PIL import Image

def main(args):
    print(f'Input directory path: {args.input_dir_path}')
    print(f'Output file path: {args.output_file}')
    
    extensions = ["jpg", "jpeg", "png", "bmp", "gif"]
    image_files = sum([glob(osp.join(args.input_dir_path, f'*.{extension}')) for extension in extensions], [])
    image_files.sort()

    target_size = (args.target_w, args.target_h)
    images = [load_resized_image(image_file, target_size) for image_file in image_files]
    
    image_count = len(images)
    if image_count == 0:
        print('No image file found')
        return
    else:
        print(f'{image_count} image files loaded')

    images[0].save(
        args.output_file, 
        save_all=True, 
        append_images=images[1:],
        optimize=False,
        duration=args.duration,
        loop=args.loop)


def load_resized_image(image_file, target_size):
    with Image.open(image_file) as image:
        image.thumbnail(target_size)
        return image


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_dir_path')
    parser.add_argument('--output_file', default='./output.gif')
    parser.add_argument('--target_w', type=int, default=600)
    parser.add_argument('--target_h', type=int, default=400)
    parser.add_argument('--duration', type=int, default=17, help="Specifies the display time of each frame in milliseconds")
    parser.add_argument('--loop', type=int, default=0, help="Specify the GIF loop count. If 0 is specified, it loops infinitely.")

    args = parser.parse_args()
    main(args)