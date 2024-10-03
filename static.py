from PIL import Image
from term_image.image import AutoImage
import numpy as np

img = Image.open("cat.jpg")
print(img.size)
padded_image = Image.new(img.mode, (img.width + 500, img.height + 500), (0, 0, 0))
padded_image.paste(img, (0, 0))
print(padded_image.size)
display = AutoImage(padded_image)
display.draw()

shift_x = 500
shift_y = 500

img_array = np.array(img.convert("RGB"))

width, height, color = img_array.shape

new_image = np.empty([padded_image.height, padded_image.width, 3], dtype=np.uint8)
new_image[0][0] = img_array[0][0]
print(new_image.shape)
print(width, height)
for w in range(width):
    for h in range(height):
        color = img_array[w][h]
        new_x = w + shift_x
        new_y = h + shift_y
        new_image[new_x][new_y] = color
new_image = Image.fromarray(new_image, "RGB")
display = AutoImage(new_image)
display.draw()
