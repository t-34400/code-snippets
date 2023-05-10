import os
import argparse
import cv2


def main(args):
    img = cv2.imread(args.input_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (_, binary_img) = cv2.threshold(gray_img, 254, 255, cv2.THRESH_BINARY)

    if args.invert:
        binary_img = 255 - binary_img

    if(cv2.imwrite(args.output_path, binary_img)):
        print("Save binarized image: ", args.output_path)
    else:
        print("Failed to save binarized image: ", args.output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path')
    parser.add_argument('--output_path')
    parser.add_argument('--invert', action='store_true')

    args = parser.parse_args()
    main(args)