from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import random
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("input",type=Path, help="")
parser.add_argument("output",type=Path, help="")
#TODO:Implement -c argument that will count numer of images that were degraded
parser.add_argument("-c", "--count",action="store_true", help="Number of images")
args = parser.parse_args()

if not args.input.is_dir():
    print(f"ERROR: Path {args.input} is not a directory!")
    exit(1)

input_dir = args.input
output_dir = args.output

files = [f for f in input_dir.iterdir() if f.suffix.lower() in ('.png', '.jpg', '.jpeg')]
# print(files)
# print(directory_to_convert)
# print(directory_to_save)
args.output.mkdir(parents=True, exist_ok=True)

for plik in files:
    input_img = Image.open(plik)
    seed = random.randrange(4)
    match seed:
        case 0:
            output_img = ImageEnhance.Contrast(input_img).enhance(random.uniform(0.5,1.4))

        case 1:
            output_img = input_img.filter(ImageFilter.GaussianBlur(random.uniform(1.7,2)))

        case 2:
            output_img = ImageOps.solarize(input_img, random.randint(180,240))

        case 3:
            output_img = ImageOps.posterize(input_img, bits=random.randint(1,2))

    output_img.save(output_dir/plik.name)
