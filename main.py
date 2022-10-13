import tkinter as tk
import PIL
from PIL import Image, ImageTk


def checker(img1, img2):
    def check(least_list, greater_list):
        wrong = []
        for place, rgb in enumerate(greater_list):
            if place > (len(least_list) - 1):
                wrong.append(greater_list[place])
                greater_list[place] = (255, 0, 0, 255)
        for place, rgb in enumerate(least_list):
            if not least_list[place] == greater_list[place]:
                least_list[place] = (255, 0, 0, 255)
                greater_list[place] = (255, 0, 0, 255)
                wrong.append(greater_list[place])
        return [least_list, greater_list, wrong]

    def get_image(image_path):
        image = Image.open(image_path)
        size = image.size
        image_rgb = image.convert("RGB")
        pixel_values = list(image_rgb.getdata())
        return [pixel_values, size[0], size[1]]

    c = get_image(img1)
    c2 = get_image(img2)
    if len(c[0]) >= len(c2[0]):
        checking = check(c2[0], c[0])
        cr = checking[1]
    else:
        checking = check(c[0], c2[0])
        cr = checking[0]
    crim = PIL.Image.new(mode="RGB", size=(c[1], c[2]))
    crim.save("img1.png")
    crims = Image.open("img1.png")

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
    newroot = tk.Toplevel()
    newroot.title("results")
    newframe = tk.Frame()
    newframe.pack()
    img = tk.PhotoImage(
                        file='img1.png')
    imgl = tk.Label(newroot, image=img)
    imgl.pack(side=tk.LEFT)
    def veiw_img():
        newimg = tk.PhotoImage(
            file=img1
        )
        newimg2 = tk.PhotoImage(
            file=img2
        )
        newimglabel = tk.Label(newroot, image=newimg)
        newimglabel2 = tk.Label(newroot, image=newimg2)
        newimglabel.pack(side=tk.RIGHT)
        newimglabel2.pack(side=tk.RIGHT)
    veiwoldimg = tk.Button(newroot,
                           text="view pixels",
                           command=veiw_img)
    veiwoldimg.pack(side=tk.BOTTOM)
    newroot.mainloop()

root = tk.Tk()
root.geometry('600x50+250+200')
root.title("input paths")
frame = tk.Frame()
frame.pack()
firstimgtext = tk.Text(root,
                       height=1,
                       width=25
                       )
firstimgtext.pack()
firstimgtext.place(x=-0, y=10)
secondimgtext = tk.Text(root,
                        height=1,
                        width=25
                        )
secondimgtext.pack()
secondimgtext.place(x=390, y=10)
load_button = tk.Button(text="load",
                        command=lambda: checker(str(firstimgtext.get("1.0", 'end-1c')),
                                                str(secondimgtext.get("1.0", 'end-1c'))))
load_button.pack()
load_button.place(x=270, y=10)
root.mainloop()
