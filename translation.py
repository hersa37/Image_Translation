from tkinter import *
from PIL import ImageTk, Image


# Function untuk ubah posisi gambar berdasarkan posisi slider
def changeposition(panel, im):
    panel.moveto(im, x=hslider.get(), y=vslider.get())


# Main window
root = Tk()
root.minsize(700, 700)

# Window dibagi menjadi grid 10 x 10. (0,0) hingga (9,9) dipakai untuk frame gambar
imagepane = Frame(root, bg="red")
imagepane.grid(sticky="nsew", row=0, column=0, columnspan=9, rowspan=9)

# Drawable canvas untuk memasukkan gambar
canvas = Canvas(imagepane)
canvas.pack(expand=YES, fill=BOTH)

# Buka dan tampilkan gambar dengan anchor gambar north west
image = ImageTk.PhotoImage(Image.open("cat.jpg"))
im = canvas.create_image(0, 0, image=image, anchor=NW)

# Slider bawah untuk pindah horizontal
bottomslider = Frame(root)
bottomslider.grid(row=9, column=0, padx=10, pady=10, columnspan=9)
hslider = Scale(
    bottomslider,
    from_=0,
    to=500,
    orient=HORIZONTAL,
    length=630,
    tickinterval=50,
    # Command yang dijalankan saat slider dipindah
    command=lambda x, cvs=canvas, i=im: changeposition(cvs, i),
)
hslider.pack()

# Slider samping untuk pindah vertikal
sideslider = Frame(root)
sideslider.grid(row=0, column=9, padx=10, pady=10, rowspan=9)
vslider = Scale(
    sideslider,
    from_=0,
    to=500,
    length=700,
    tickinterval=50,
    # Command yang dijalankan saat slider dipindah. panggil changeposition
    command=lambda y, cvs=canvas, i=im: changeposition(cvs, i),
)
vslider.pack()

root.mainloop()
