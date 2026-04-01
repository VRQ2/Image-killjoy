from PIL import Image, ImageFilter, ImageOps, ImageEnhance
from tkinter.filedialog import askopenfilename, askdirectory
import os
import random

#file_to_convert = askopenfilename()

directory_to_convert = askdirectory()

directory_to_save = askdirectory()

#input_img = Image.open(file_to_convert)

#TODO: Simple console GUI (1.degrade one, 2.degrade folder, 3.exit)

#output_img = input_img.filter(ImageFilter.GaussianBlur(1.8))
#output_img = ImageOps.posterize(input_img, bits=2)
#output_img = ImageOps.solarize(input_img, 150)
#output_img = ImageEnhance.Contrast(input_img).enhance(1.7)

files = [f for f in os.listdir(directory_to_convert) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
print(files)
print(directory_to_convert)
print(directory_to_save)

for e in range(len(files)):
    input_img = Image.open(f"{directory_to_convert}/{files[e]}")
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

    output_img.save(f'{directory_to_save}/changed{e}.jpg')
