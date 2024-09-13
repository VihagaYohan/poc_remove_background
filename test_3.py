from rembg import remove
import requests
from PIL import Image
from io import BytesIO
import os
import time # import time for performance measurement

os.makedirs('original', exist_ok=True)
os.makedirs('masked', exist_ok=True)

# start time
start_time = time.time()

#img_url = 'https://thumbs.dreamstime.com/b/cardboard-box-12876511.jpg'
img_url = 'https://www.socialnicole.com/wp-content/uploads/2015/02/youngsters.jpg'
background_img_url = 'https://assets.bizclikmedia.net/576/9ab34bd7bb989e5a3573a004b7c0afc2:cc72258094e24794c903319427a3c198/404no22rkhlzamdi171120205413.jpeg'
img_name = img_url.split('/')[-1]

img = Image.open(BytesIO(requests.get(img_url).content))
img.save('original/'+img_name, format='jpeg')

output_path = 'masked/'+img_name

with open(output_path, 'wb') as f:
    input = open('original/'+img_name, 'rb').read()
    subject = remove(input, alpha_matting=True, alpha_matting_foreground_threshold=50)
    f.write(subject)

# replacing background
background_img_url = Image.open(BytesIO(requests.get(background_img_url).content))

# resize image
background_img_url = background_img_url.resize((img.width, img.height))

foreground_image = Image.open(output_path)
background_img_url.paste(foreground_image, (0,0), foreground_image)
background_img_url.save('masked/background.jpg',format='jpeg')

# end time measurement
end_time = time.time()

# calculate the total time taken
time_taken = end_time - start_time
print(f"Time taken to process {img_url}: {time_taken:.4f} seconds")
