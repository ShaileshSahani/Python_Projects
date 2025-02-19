from tkinter import *
from PIL import ImageTk, Image

try:
    def slide_2():
        create_header(2, 537)

        img_frame2 = Frame(root, height=620, width=1200, bd=1, relief=SOLID, bg="#56abf5")
        img_frame2.place(x=0, y=50)

        question = Label(img_frame2, text="Introduction To Project", font="Ariel 35 bold", padx=235,
                         bd=1, relief=GROOVE)
        question.place(x=115, y=25)

        # sep = Label(img_frame2, text="•", bg="green", bd=0, relief=GROOVE, pady=260)
        # sep.place(x=600, y=75)

        l1 = Label(img_frame2, text="• React", font="Ariel 30 bold", padx=200)
        l1.place(x=350, y=100)

        l2 = Label(img_frame2, text="• JSX", font="Ariel 30 bold", padx=216)
        l2.place(x=350, y=160)

        l3 = Label(img_frame2, text="• Files", font="Ariel 30 bold", padx=209)
        l3.place(x=350, y=220)

        l3 = Label(img_frame2, text="• Website", font="Ariel 30 bold", padx=178)
        l3.place(x=350, y=280)

        l3 = Label(img_frame2, text="• Cards", font="Ariel 30 bold", padx=199)
        l3.place(x=350, y=340)

        l3 = Label(img_frame2, text="• Poster", font="Ariel 30 bold", padx=195)
        l3.place(x=350, y=400)

        l3 = Label(img_frame2, text="• App.css", font="Ariel 30 bold", padx=182)
        l3.place(x=350, y=460)

        l3 = Label(img_frame2, text="• App.js", font="Ariel 30 bold", padx=198)
        l3.place(x=350, y=520)

        footer(slide_1, slide_3)


    def slide_3():
        create_header(3, 537)

        img_frame3 = Frame(root, height=620, width=1200, bd=1, relief=SOLID, bg="#56abf5")
        img_frame3.place(x=0, y=50)

        lab = Label(img_frame3, image=react, width=1200, height=620)
        lab.place(x=0, y=0)

        footer(slide_2, slide_4)


    def slide_4():
        create_header(4, 537)

        img_frame4 = Frame(root, height=620, width=1200, bd=1, relief=SOLID, bg="#56abf5")
        img_frame4.place(x=0, y=50)

        lab = Label(img_frame4, image=jsx, width=1200)
        lab.place(x=0, y=0)

        footer(slide_3, slide_5)


    def slide_5():
        create_header(5, 537)

        img_frame5 = Frame(root, height=620, width=1200, bd=1, relief=SOLID, bg="#56abf5")
        img_frame5.place(x=0, y=50)

        lab = Label(img_frame5, image=web, width=1200)
        lab.place(x=0, y=0)

        footer(slide_4, slide_6)


    def slide_6():
        create_header(6, 537)

        img_frame6 = Frame(root, height=620, width=1200, bd=1, relief=SOLID, bg="#56abf5")
        img_frame6.place(x=0, y=50)

        lab = Label(img_frame6, image=cards, width=1200)
        lab.place(x=0, y=0)

        footer(slide_5, slide_7)


    def slide_7():
        create_header(7, 537)

        img_frame7 = Frame(root, height=620, width=1200, bd=1, relief=SOLID, bg="#56abf5")
        img_frame7.place(x=0, y=50)

        lab = Label(img_frame7, image=makima, width=1200)
        lab.place(x=0, y=0)

        footer(slide_6, slide_8)


    def slide_8():
        create_header(8, 537)

        img_frame8 = Frame(root, height=620, width=1200, bd=1, relief=SOLID, bg="#56abf5")
        img_frame8.place(x=0, y=50)

        lab = Label(img_frame8, image=css, width=1200)
        lab.place(x=0, y=0)

        footer(slide_7, slide_9)


    def slide_9():
        create_header(9, 537)

        img_frame9 = Frame(root, height=620, width=1200, bd=1, relief=SOLID, bg="#56abf5")
        img_frame9.place(x=0, y=50)

        lab = Label(img_frame9, image=app, width=1200)
        lab.place(x=0, y=0)

        footer(slide_8, slide_10)


    def slide_10():
        create_header(10, 534)

        img_frame10 = Frame(root, height=620, width=1200, bd=1, relief=SOLID, bg="#56abf5")
        img_frame10.place(x=0, y=50)

        wel_lab = Label(img_frame10, text="Thank You", font=("Garamond", 90, 'italic'),
                        padx=303, bg="#2159ad", fg="#00eeff")
        wel_lab.place(x=2, y=240)

        footer(slide_9, "")


    root = Tk()
    root.wm_minsize(1200, 720)
    root.wm_maxsize(1200, 720)
    root.title("Python DSA ppt")

    react = ImageTk.PhotoImage(Image.open("Images/React.jpg"))
    jsx = ImageTk.PhotoImage(Image.open("Images/JSX.jpg"))
    web = ImageTk.PhotoImage(Image.open("Images/web.jpg"))
    makima = ImageTk.PhotoImage(Image.open("Images/Makima.jpg"))
    app = ImageTk.PhotoImage(Image.open("Images/App.jpg"))
    css = ImageTk.PhotoImage(Image.open("Images/css.jpg"))
    cards = ImageTk.PhotoImage(Image.open("Images/cards.jpg"))



    def create_header(num, size):
        head_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        head_frame.pack(anchor=CENTER)
        head_lab = Label(root, text=f"Slide {num}", font=("Georgia", 27, 'bold'), padx=size, bg="#8fc7c5", pady=1,
                         fg="#ff0548")
        head_lab.place(x=1, y=1)


    def footer(fun1, fun2):
        foot = Frame(root, height=50, width=1200, bd=1, relief=SOLID, bg="#8b8c8b")
        foot.place(x=0, y=670)

        b1 = Button(foot, text="Previous", font="Georgia 14 bold", bg="Green", command=fun1)
        b1.place(x=400, y=4)

        b2 = Button(foot, text="Next", font="Georgia 14 bold", bg="Green", padx=30, command=fun2)
        b2.place(x=700, y=4)


    def slide_1():
        create_header(1, 537)

        img_frame1 = Frame(root, height=620, width=1200, bd=1, relief=SOLID, bg="#56abf5")
        img_frame1.place(x=0, y=50)

        lab_1 = Label(img_frame1, text="Name : Shailesh Sahani ", font=("Garamond", 35, 'italic'), bg="#2159ad")
        lab_1.place(x=150, y=150)
        lab_2 = Label(img_frame1, text="Subject : Framework of Web Development ", font=("Garamond", 35, 'italic'),
                      bg="#2159ad")
        lab_2.place(x=150, y=240)
        lab_3 = Label(img_frame1, text="Project : Anime Website ", font=("Garamond", 35, 'italic'),
                      bg="#2159ad")
        lab_3.place(x=150, y=330)
        lab_4 = Label(img_frame1, text=" - By using Python Tkinter ", font=("Garamond", 20, 'italic'),
                      fg="#00ffee", bg="#2159ad")
        lab_4.place(x=800, y=550)

        footer("", slide_2)


    slide_1()

    # Images

    root.mainloop()
except Exception as Er:
    print(Er)
