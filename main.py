a = ['255', '255', '255']
b = "apple"
'''# index and list
for index, value in enumerate(a):
    if value == "255":
        a[index] = "not a bannana"
print(a)'''
import tkinter
import PIL
from PIL import Image, ImageTk

def check(least_list,greater_list):
    for place, rgb in enumerate(greater_list):
        if place > (len(least_list) -1):
            greater_list[place] = (255, 0 ,0,255)
    for place, rgb in enumerate(least_list):
        if not least_list[place] == greater_list[place]:
            least_list[place] = (255, 0, 0, 255)
            greater_list[place] = (255, 0, 0,255)
    return [least_list,greater_list]
def get_image(image_path):
    image = Image.open(image_path)
    size = image.size
    image_rgb = image.convert("RGB")
    pixel_values = list(image_rgb.getdata())
    return [pixel_values, size[0], size[1]]


c = get_image('test1.png')
c2 = get_image('test2.png')
if len(c[0]) >= len(c2[0]):
    checking = check(c2[0], c[0])
    cr = checking[1]
    c2r = checking[0]
else:
    checking = check(c[0], c2[0])
    cr = checking[0]
    c2r = checking[1]
crim = PIL.Image.new(mode="RGB", size=(c[1], c[2]))
crim.save("img1.png")
crims = Image.open("img1.png")
crimse = get_image("img1.png")

x = 0
y = 0
pix = crims.load()
for rgb in cr:
    x = x + 1
    if x > c[1] - 1:
        x = x - c[1]
        y = y + 1
    if y > c[2] - 1:
        y = y - c[2]
    pix[x, y] = rgb
crims.save("img1.png")
