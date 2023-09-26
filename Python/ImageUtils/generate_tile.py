import argparse
from PIL import Image

def main(args):
    result_width = args.tile_width * args.num_cols
    result_height = args.tile_height * args.num_rows
    result = Image.new("RGB", (result_width, result_height))

    for i, image_file in enumerate(args.image_paths):
        image = Image.open(image_file)
        image = image.resize((args.tile_width, args.tile_height))
        x = i % args.num_cols * args.tile_width
        y = i // args.num_cols * args.tile_height
        result.paste(image, (x, y))

    result.save(args.output_path)
    print(f"Successfully generate the texture tile: {args.output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--image_paths', nargs='+', required=True)

    parser.add_argument('--tile_width', type=int, default=200)
    parser.add_argument('--tile_height', type=int, default=200)

    parser.add_argument('--num_rows', type=int, default=2)
    parser.add_argument('--num_cols', type=int, default=2)

    parser.add_argument('--output_path', type=str, default="tiled_image.png")

    args = parser.parse_args()
    main(args)
