import argparse
import qrcode

def main(args):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=args.box_size,
        border=args.border
    )
    qr.add_data(args.data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=args.fill_color, back_color=args.back_color)

    img.save(args.output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--data', type=str, required=True)
    parser.add_argument('--box_size', type=int, default=10)
    parser.add_argument('--border', type=int, default=4)
    parser.add_argument('--fill_color', type=str, default="black")
    parser.add_argument('--back_color', type=str, default="white")

    parser.add_argument('--output_path', type=str, default="qr.png")


    args = parser.parse_args()
    main(args)



