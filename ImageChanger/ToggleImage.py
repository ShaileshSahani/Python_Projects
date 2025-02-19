from PIL import ImageTk
from tkinter import *
from random import choice

try:

    win = Tk()
    win.title("Anime Images")
    win.wm_maxsize(800, 590)
    win.wm_minsize(800, 590)
    Deku = ImageTk.PhotoImage(file="Deku.jpg")
    Eren = ImageTk.PhotoImage(file="Eren.jpg")
    Giyu = ImageTk.PhotoImage(file="Giyu.jpg")
    Gojo = ImageTk.PhotoImage(file="Gojo.jpg")
    Katagiri = ImageTk.PhotoImage(file="Katagiri.jpg")
    Kukushibo = ImageTk.PhotoImage(file="Kukushibo.jpg")
    Light = ImageTk.PhotoImage(file="Light.jpg")
    Megumi = ImageTk.PhotoImage(file="Megumi.jpg")
    Nanami = ImageTk.PhotoImage(file="Nanami.jpg")
    Sasuke = ImageTk.PhotoImage(file="Sasuke.jpg")
    Tanjiro = ImageTk.PhotoImage(file="Tanjiro.jpg")
    Yuji = ImageTk.PhotoImage(file="Yuji.jpg")
    Yuta = ImageTk.PhotoImage(file="Yuta.jpg")
    Zenitsu = ImageTk.PhotoImage(file="Zenitsu.jpg")
    image_ = [Deku, Eren, Giyu, Gojo, Katagiri, Kukushibo, Light,
              Megumi, Nanami, Sasuke, Tanjiro, Yuji, Yuta, Zenitsu]


    def load():
        lab = Label(win, image=choice(image_), bd=2, relief=GROOVE, bg="black")
        lab.place(x=0, y=0)


    load()
    but = Button(win, text="Change The Image", bg="red", fg="blue", pady=3, padx=328, bd=2, relief=GROOVE,
                 font=20, command=load)
    but.place(x=0, y=554)
    win.mainloop()
except Exception as E:
    print(E)
