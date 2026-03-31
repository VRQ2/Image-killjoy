from PIL import Image, ImageFilter, ImageOps, ImageEnhance
from tkinter.filedialog import askopenfilename
import os

file_to_convert = askopenfilename()

input_img = Image.open(file_to_convert)

#TODO: Add loop for every image in directory
#TODO: Randomizer for image filter
#TODO: Adjust filters
#TODO: Simple console GUI (1.degrade one, 2.degrade folder, 3.exit)

#output_img = input_img.filter(ImageFilter.GaussianBlur(1.8))
#output_img = ImageOps.posterize(input_img, bits=2)
#output_img = ImageOps.solarize(input_img, 150)
output_img = ImageEnhance.Contrast(input_img).enhance(1.7)

output_img.save('test.jpg')
output_img.show()
