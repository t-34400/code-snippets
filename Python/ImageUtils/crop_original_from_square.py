import argparse
from PIL import Image

def main(args):
    original_image_path = args.original_image_path
    resized_image_path = args.resized_image_path
    output_path = args.output_path

    crop_original_image(original_image_path, resized_image_path, output_path)


def crop_original_image(original_image_path, resized_image_path, output_path):
    original_image = Image.open(original_image_path)
    original_size = original_image.size
    print("Original size: ", original_size)

    resized_image = Image.open(resized_image_path)
    resize_length = resized_image.size[0]
    print("Resize length: ", resize_length)

    aspect = resize_length / max(original_size)
    print("Aspect: ", aspect)

    width = (int) (original_size[0] * aspect)
    height = (int) (original_size[1] * aspect)

    left = (resize_length - width) // 2
    top = (resize_length - height) // 2
    right = left + width
    bottom = top + height

    print("Crop box: ", left, top, right, bottom)

    cropped_image = resized_image.crop((left, top, right, bottom))
    cropped_image = cropped_image.resize(original_size)

    cropped_image.save(output_path)
    print(f"Successfully saved original size image: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--original_image_path', type=str)
    parser.add_argument('--resized_image_path', type=str)
    parser.add_argument('--output_path', type=str, default="output.png")

    args = parser.parse_args()
    main(args)
