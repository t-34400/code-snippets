import argparse
import barcode
# If you want to render image of your barcode, you need to install Pillow:
#    pip install Pillow
# or
#    pip install python-barcode[images]
from barcode.writer import ImageWriter

def main(args):
    bc = barcode.get(args.code_class, args.data, writer=ImageWriter(format='PNG'))

    bc.save(args.output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--data', type=str, required=True)
    parser.add_argument('--code_class', type=str, default="ean13")

    parser.add_argument('--output_path', type=str, default="barcode.png")


    args = parser.parse_args()
    main(args)
