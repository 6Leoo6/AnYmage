import argparse
import math

import numpy as np
from PIL import Image


def convert_to_image(input_path, output_path, reverse=False):

    if not reverse:
        with open(input_path, 'rb') as f:
            file_bytes = bytearray(f.read())

        useful_bytes = file_bytes
        number_of_bytes = len(useful_bytes) + 3
        number_of_useful_pixels = math.ceil(number_of_bytes / 3)


        smallest_image_dim = math.ceil(math.sqrt(
            number_of_useful_pixels
        ))
        min_number_of_pixels = smallest_image_dim ** 2
        min_number_of_bytes = min_number_of_pixels * 3

        number_of_leftover_bytes = int(min_number_of_bytes - number_of_bytes)

        file_suffix = bytearray(number_of_leftover_bytes.to_bytes(3, byteorder="big"))
        filler_bytes = bytearray(number_of_leftover_bytes * b'\x00')

        output_bytes = np.array(
            useful_bytes + filler_bytes + file_suffix,
        )

        rgb_array = output_bytes.reshape((smallest_image_dim, smallest_image_dim, 3))

        Image.fromarray(rgb_array).save(output_path)
    else:
        image_bytes = bytearray(Image.open(input_path).tobytes())
        filler_length = int.from_bytes(image_bytes[-3:])

        file_bytes = image_bytes[:-filler_length - 3]

        with open(output_path, 'wb') as f:
            f.write(file_bytes)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="anymage",
        description="Convert any file to a png image representation",
    )

    parser.add_argument("-i", "--input", nargs=1, required=True, help="Input file")
    parser.add_argument("-o", "--output", nargs=1, required=True, help="Output file")
    parser.add_argument("-r", "--reverse", action="store_true", help="Reverse the process")

    args = parser.parse_args()

    convert_to_image(args.input[0], args.output[0], args.reverse)