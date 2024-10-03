from tkinter import *
from PIL import ImageTk, Image


# Function untuk ubah posisi gambar berdasarkan posisi slider
def changeposition(panel, im):
    panel.moveto(im, x=hslider.get(), y=vslider.get())


def shiftposition(cvs):
    x = hmanualtext.get()
    try:
        x = int(x)
    except:
        x = 0
    y = vmanualtext.get()
    try:
        y = int(y)
    except:
        y = 0

    hslider.set(hslider.get() + x)
    vslider.set(vslider.get() + y)


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
    command=lambda cvs=canvas, i=im: changeposition(cvs, i),
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
    command=lambda cvs=canvas, i=im: changeposition(cvs, i),
)
vslider.pack()

manualinput = Frame(root)
manualinput.grid(row=10, column=0, rowspan=2, columnspan=10)

manualshiftlabel = Label(manualinput, text="Input geser")
manualshiftlabel.grid(row=0, column=0, rowspan=2)

hmanuallabel = Label(manualinput, text="Horizontal")
hmanuallabel.grid(row=0, column=1, padx=10)

hmanualtext = Entry(manualinput, bg="white", width=5)
hmanualtext.grid(row=0, column=2)

vmanuallabel = Label(manualinput, text="Vertikal")
vmanuallabel.grid(row=0, column=3, padx=10)

vmanualtext = Entry(manualinput, bg="white", width=5)
vmanualtext.grid(row=0, column=4, padx=10)

confirmbutton = Button(
    manualinput,
    text="Confirm",
    command=lambda cvs=canvas: shiftposition(cvs),
)
confirmbutton.grid(row=0, column=5, padx=10)

root.mainloop()
