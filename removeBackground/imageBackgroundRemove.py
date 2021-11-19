from rembg.bg import remove
import numpy as np
import io
import os
from PIL import Image
from func import *
images_path = get_images_path()
convert_to_png(images_path)



# input_path = '20.png'
# im = Image.open('20.jpg')
# im.save('20.png')
# output_path = 'out.png'

cwd = os.getcwd()
for image in images_path:
    c_path = cwd+'/images/'+image
    c_path = c_path.replace('jpg','png')
    f = np.fromfile(c_path)
    result = remove(f)
    result = remove(f,alpha_matting=True,    alpha_matting_foreground_threshold=240,
    alpha_matting_background_threshold=1,alpha_matting_erode_structure_size=1, alpha_matting_base_size=2000,)
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    c_path = c_path.replace('.png','_bgrem.png')
    img.save(c_path)

print("images background removed!")
# f = np.fromfile(input_path)
# # result = remove(f)
# result = remove(f,alpha_matting=True,    alpha_matting_foreground_threshold=240,
# alpha_matting_background_threshold=1,
#     alpha_matting_erode_structure_size=1,
#     alpha_matting_base_size=2000,)
# img = Image.open(io.BytesIO(result)).convert("RGBA")
# img.save(output_path)