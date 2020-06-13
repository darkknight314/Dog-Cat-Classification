import os
from PIL import Image

for image_file_name in os.listdir('D:\Study\Sem 6\CS 419 - Intro to ML\Project\images\images'):
    if image_file_name.endswith(".jpg"):
        im = Image.open('D:\\Study\\Sem 6\\CS 419 - Intro to ML\\Project\\images\\images\\' + image_file_name)
        new_width  = 256
        new_height = 256
        im = im.resize((new_width, new_height), Image.ANTIALIAS)
        im = im.convert('RGB')
        im.save('D:\\Study\\Sem 6\\CS 419 - Intro to ML\\Project\\images\\resized256\\' + image_file_name[:-4] + '.jpg')