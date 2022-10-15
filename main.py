import tkinter as tk
import PIL
from PIL import Image


def checker(img1, img2):
    def check_pixels(least_list, greater_list):
        for place, color in enumerate(least_list):
            if not least_list[place] == greater_list[place]:
                least_list[place] = (255, 0, 0, 255)
                greater_list[place] = (255, 0, 0, 255)
        return [least_list, greater_list]

    def get_image(image_path):
        image = Image.open(image_path)
        size = image.size
        image_rgb = image.convert("RGB")
        pixel_values = list(image_rgb.getdata())
        return [pixel_values, size[0], size[1]]

    # gets the pixels from each both images and sets them to different variables
    first_image_data = get_image(img1)
    second_image_data = get_image(img2)

    pixel_checking_data = check_pixels(first_image_data[0], second_image_data[0])  # get data of different pixels
    revised_pixel_data = pixel_checking_data[0]  # gets list of different pixels

    PIL.Image.new(mode="RGB", size=(first_image_data[1], first_image_data[2])).save("img1.png")  # create blank image
    revised_image = Image.open("img1.png")

    x = 0
    y = 0
    pix = revised_image.load()

    for rgb in revised_pixel_data:
        x = x + 1  # go over one pixel on the x axis
        if x > first_image_data[1] - 1:  # if the image is not big enough to hold next pixel
            # goes up one y axis value
            x = x - first_image_data[1]
            y = y + 1

        if y > first_image_data[2] - 1:
            y = y - first_image_data[2]
        # sets the pixel to the right color
        pix[x, y] = rgb

    revised_image.save("img1.png")  # saves new image

    newroot = tk.Toplevel()
    newroot.title("results")
    newframe = tk.Frame()
    newframe.pack()

    img = tk.PhotoImage(
                        file='./img1.png'
    )
    imgl = tk.Label(newroot, image=img)
    imgl.pack(side=tk.LEFT)

    def stop_veiw():
        veiwoldimg['text'] = 'view original images'
        veiwoldimg['command'] = veiw_img

    def veiw_img():
        veiwoldimg['text'] = 'stop veiwing'
        veiwoldimg['command'] = stop_veiw
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
                           text="view original images",
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
