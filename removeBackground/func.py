import os
from PIL import Image
def get_images_path():       # 1.Get file names from directory
    cwd = os.getcwd()
    image_dir = cwd + "/images/"
    file_list=os.listdir(image_dir)
    return file_list

# input_path = '20.png'
# im = Image.open('20.jpg')
# im.save('20.png')


def convert_to_png(images_path):
    cwd = os.getcwd()
    for image in images_path:
        c_path = cwd+'/images/'+image
        im = Image.open(c_path)
        c_path = c_path.replace('jpg','png')
        im.save(c_path)