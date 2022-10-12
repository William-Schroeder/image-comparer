a = ['255','255','255']
b = "apple"
'''# index and list
for index, value in enumerate(a):
    if value == "255":
        a[index] = "not a bannana"
print(a)'''

from PIL import Image


def get_image(image_path):
    image = Image.open(image_path).convert("L")
    image_rgb = image.convert("RGB")
    pixel_values = list(image_rgb.getdata())

    return pixel_values


c = get_image('./test.png')
print(c)
