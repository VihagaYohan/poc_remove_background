import os

from rembg import remove
from PIL import Image

# input_path = "cl.jpg"
# output_path = "output.jpg"
#
# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)

# directory where the images are stored
ASSET_DIR = "assets"
OUTPUT_DIR = "output"

def loop_images():
    for filename in os.listdir(ASSET_DIR):
        if filename.endswith(('.jpg','jpeg','.png')):
            image_path = os.path.join(ASSET_DIR, filename)
            output_path = os.path.join(ASSET_DIR,'output', 'no_bg_'+filename)

            # remove background
            input = Image.open(image_path)
            output = remove(input)
            output.save(output_path)

            #print(image_path)
            #print(output_path)

loop_images()