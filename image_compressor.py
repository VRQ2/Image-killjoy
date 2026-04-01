from PIL import Image, ImageFilter, ImageOps, ImageEnhance
from tkinter.filedialog import askopenfilename, askdirectory
import os

#file_to_convert = askopenfilename()

directory_to_convert = askdirectory()

directory_to_save = askdirectory()

#input_img = Image.open(file_to_convert)

#TODO: Add loop for every image in directory
#TODO: Randomizer for image filter
#TODO: Adjust filters
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
    output_img = ImageEnhance.Contrast(input_img).enhance(1.7)
    output_img.save(f'{directory_to_save}/changed{e}.jpg')
