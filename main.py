# main.py
import argparse
from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    """
    Remove the background of an image and save the result.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the output image without background.
    """
    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path)
    print(f"Background removed! Saved as {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove background from an image.")
    parser.add_argument("input_path", help="Path to the input image file.")
    parser.add_argument("output_path", help="Path to save the output image without background.")
    args = parser.parse_args()

    remove_background(args.input_path, args.output_path)