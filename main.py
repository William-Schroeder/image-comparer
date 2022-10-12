from PIL import Image, ImageTk
import tkinter as tk

debounce = False


def load(img1, img2):
    firstimg = (

    )


def get_image(image_path):
    image = Image.open(image_path).convert("L")
    pixel_values = list(image.getdata())

    return pixel_values


while True:
    if not debounce:
        root = tk.Tk()
        root.geometry('600x500+250+200')
        frame = tk.Frame()
        frame.pack()
        firstimgtext = tk.Text(root,
                               height=1,
                               width=25
                               )
        firstimgtext.pack()
        firstimgtext.place(x=-0, y=0)
        secondimgtext = tk.Text(root,
                                height=1,
                                width=25
                                )
        secondimgtext.pack()
        secondimgtext.place(x=390, y=0)
        load_button = tk.Button(text="load",
                                command=lambda: load(str(firstimgtext.get("1.0", 'end-1c')),
                                                     str(secondimgtext.get("1.0", 'end-1c'))))
        root.mainloop()
    else:
        print(get_image(image_path='./test.png'))
