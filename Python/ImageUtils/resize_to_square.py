import argparse
from PIL import Image
from PIL import ImageOps

def main(args):
    target_size = args.target_size
    desired_size = (target_size, target_size)

    resize_image(args.input_path, desired_size)


def resize_image(image_path, size):
    image = Image.open(image_path)

    resized_image = ImageOps.pad(image, size, color='white')

    resized_image.save(args.output_path)
    print(f"Successfully saved resized image: {args.output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_path', type=str)
    parser.add_argument('--output_path', type=str, default="resized_image.png")

    parser.add_argument('--target_size', type=int, default=200)

    args = parser.parse_args()
    main(args)
