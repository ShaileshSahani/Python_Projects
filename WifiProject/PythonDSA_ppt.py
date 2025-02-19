from tkinter import *
from PIL import ImageTk, Image

try:
    def slide_2():
        head_lab.config(text="Slide 2")
        img_frame2 = Frame(root, bg="#2159ad", height=700, width=1200)
        img_frame2.place(x=0, y=50)
        l1 = Label(img_frame2, text="• Topics", bg="#2159ad", font=("Garamond", 35, 'italic'))
        l1.place(x=440, y=70)

        l2 = Label(img_frame2, text="• Introduction", bg="#2159ad", font=("Garamond", 20, 'italic'))
        l2.place(x=440, y=150)

        l3 = Label(img_frame2, text="• Modules", bg="#2159ad", font=("Garamond", 20, 'italic'))
        l3.place(x=440, y=200)

        l3 = Label(img_frame2, text="• Functions", bg="#2159ad", font=("Garamond", 20, 'italic'))
        l3.place(x=440, y=250)

        l9 = Label(img_frame2, text="• Tkinter Gui", bg="#2159ad", font=("Garamond", 20, 'italic'))
        l9.place(x=440, y=300)

        l4 = Label(img_frame2, text="• Database Mysql", bg="#2159ad", font=("Garamond", 20, 'italic'))
        l4.place(x=440, y=350)

        l5 = Label(img_frame2, text="• Multiple Tables", bg="#2159ad", font=("Garamond", 20, 'italic'))
        l5.place(x=440, y=400)

        l6 = Label(img_frame2, text="• Validation", bg="#2159ad", font=("Garamond", 20, 'italic'))
        l6.place(x=440, y=450)

        l7 = Label(img_frame2, text="• Searching", bg="#2159ad", font=("Garamond", 20, 'italic'))
        l7.place(x=440, y=500)

        l8 = Label(img_frame2, text="• History", bg="#2159ad", font=("Garamond", 20, 'italic'))
        l8.place(x=440, y=550)

        l8 = Label(img_frame2, text="• Conclusion", bg="#2159ad", font=("Garamond", 20, 'italic'))
        l8.place(x=440, y=600)

        l10 = Label(img_frame2, image=modules, bd=0, bg="#2159ad")
        l10.place(x=700, y=200)

        button_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        button_frame.place(x=0, y=750)

        slide2 = Button(button_frame, text="Previous", command=slide_1, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide2.place(x=205, y=1)

        slide2 = Button(button_frame, text="Next", command=slide_3, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide2.place(x=655, y=1)


    def slide_3():
        head_lab.config(text="Slide 3")
        img_frame3 = Frame(root, height=700, width=1200, bg="#2159ad")
        img_frame3.place(x=0, y=50)
        tp = Label(img_frame3, text="Login Page", font=("Garamond", 40, 'italic'), padx=300, fg="Blue")
        tp.place(x=168, y=20)
        l2 = Label(img_frame3, image=login_page, width=1200, bg="#2159ad")
        l2.place(x=0, y=120)

        button_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        button_frame.place(x=0, y=750)
        slide3 = Button(button_frame, text="Previous", command=slide_2, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide3.place(x=205, y=1)

        slide3 = Button(button_frame, text="Next", command=slide_4, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide3.place(x=655, y=1)


    def slide_4():
        head_lab.config(text="Slide 4")
        img_frame4 = Frame(root, height=700, width=1200, bg="#2159ad")
        img_frame4.place(x=0, y=50)
        tp = Label(img_frame4, text="Nested Functions", font=("Garamond", 30, 'italic'), padx=320, fg="Blue")
        tp.place(x=122, y=60)
        l2 = Label(img_frame4, image=nested, width=1200, bg="#2159ad")
        l2.place(x=0, y=160)

        button_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        button_frame.place(x=0, y=750)
        slide4 = Button(button_frame, text="Previous", command=slide_3, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide4.place(x=205, y=1)

        slide4 = Button(button_frame, text="Next", command=slide_5, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide4.place(x=655, y=1)


    def slide_5():
        head_lab.config(text="Slide 5")
        img_frame5 = Frame(root, height=700, width=1200, bg="#2159ad")
        img_frame5.place(x=0, y=50)
        l2 = Label(img_frame5, image=main, width=1200, bg="#2159ad")
        l2.place(x=0, y=50)

        l3 = Label(img_frame5, text="Contains Calculator, Calender, Dropdown menus, Validation, Buttons",
                   font="ariel 16 bold",padx=104)
        l3.place(x=150, y=600)

        button_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        button_frame.place(x=0, y=750)
        slide5 = Button(button_frame, text="Previous", command=slide_4, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide5.place(x=205, y=1)

        slide5 = Button(button_frame, text="Next", command=slide_6, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide5.place(x=655, y=1)


    def slide_6():
        head_lab.config(text="Slide 6")
        img_frame6 = Frame(root, height=700, width=1200, bg="#2159ad")
        img_frame6.place(x=0, y=50)
        l1_ = Label(img_frame6, text="Data base connection using MYSQL", font=("Garamond", 30, 'italic'), padx=100)
        l1_.place(x=170, y=60)
        l2 = Label(img_frame6, image=db_, width=1200, bg="#2159ad")
        l2.place(x=0, y=160)

        button_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        button_frame.place(x=0, y=750)
        slide6 = Button(button_frame, text="Previous", command=slide_5, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide6.place(x=205, y=1)

        slide6 = Button(button_frame, text="Next", command=slide_7, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide6.place(x=655, y=1)


    def slide_7():
        head_lab.config(text="Slide 7")
        img_frame7 = Frame(root, height=700, width=1200, bg="#2159ad")
        img_frame7.place(x=0, y=50)
        l1 = Label(img_frame7, image=image_bin_algo_, width=1200, bg="#2159ad")
        l1.place(x=0, y=20)
        l2 = Label(img_frame7, image=image_bin_algo, width=1200, bg="#2159ad")
        l2.place(x=0, y=110)

        button_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        button_frame.place(x=0, y=750)
        slide7 = Button(button_frame, text="Previous", command=slide_6, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide7.place(x=205, y=1)

        slide7 = Button(button_frame, text="Next", command=slide_8, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide7.place(x=655, y=1)


    def slide_8():
        head_lab.config(text="Slide 8")
        img_frame8 = Frame(root, height=700, width=1200, bg="#2159ad")
        img_frame8.place(x=0, y=50)
        l1 = Label(img_frame8, text="Update Admin Data", font=("Garamond", 30, 'italic'), padx=275)
        l1.place(x=150, y=20)
        l1 = Label(img_frame8, image=image_binary, width=1200, bg="#2159ad")
        l1.place(x=0, y=80)

        button_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        button_frame.place(x=0, y=750)
        slide8 = Button(button_frame, text="Previous", command=slide_7, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide8.place(x=205, y=1)

        slide8 = Button(button_frame, text="Next", command=slide_9, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide8.place(x=655, y=1)


    def slide_9():
        head_lab.config(text="Slide 9")
        img_frame9 = Frame(root, height=700, width=1200, bg="#2159ad")
        img_frame9.place(x=0, y=50)
        l1 = Label(img_frame9, text="Storing data inside the Database", font=("Garamond", 30, 'italic'), padx=270)
        l1.place(x=70, y=20)
        l2 = Label(img_frame9, image=image_binary__tree, width=1200, bg="#2159ad")
        l2.place(x=00, y=100)

        button_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        button_frame.place(x=0, y=750)
        slide9 = Button(button_frame, text="Previous", command=slide_8, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide9.place(x=205, y=1)

        slide9 = Button(button_frame, text="Next", command=slide_10, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide9.place(x=655, y=1)


    def slide_10():
        head_lab.config(text="END Slide")
        img_frame10 = Frame(root, height=700, width=1200, bg="#2159ad")
        img_frame10.place(x=0, y=50)
        wel_lab = Label(img_frame10, text="Thank You", font=("Garamond", 90, 'italic'),
                        padx=303, bg="#2159ad", fg="#00eeff")
        wel_lab.place(x=2, y=300)

        button_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        button_frame.place(x=0, y=750)
        slide10 = Button(button_frame, text="Previous", command=slide_9, activebackground="cyan",
                         activeforeground="red",
                         font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide10.place(x=455, y=1)


    root = Tk()
    root.geometry("1200x800")
    root.wm_minsize(1200, 800)
    root.wm_maxsize(1200, 800)
    root.title("Python DSA ppt")

    headFrame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
    headFrame.pack(anchor=CENTER)
    head_lab = Label(root, text="Slide 1", font=("Georgia", 27, 'bold'), padx=537, bg="#8fc7c5", pady=1, fg="#ff0548")
    head_lab.place(x=1, y=1)


    def slide_1():
        head_lab.config(text="Slide 1")
        img_frame1 = Frame(root, height=700, width=1200, bg="#2159ad")
        img_frame1.place(x=0, y=50)
        lab_1 = Label(img_frame1, text="Name : Shailesh Sahani ", font=("Garamond", 35, 'italic'), bg="#2159ad")
        lab_1.place(x=150, y=150)
        lab_2 = Label(img_frame1, text="Subject : Python DSA ", font=("Garamond", 35, 'italic'), bg="#2159ad")
        lab_2.place(x=150, y=240)
        lab_3 = Label(img_frame1, text="Topic : Wifi Payment App ", font=("Garamond", 35, 'italic'), bg="#2159ad")
        lab_3.place(x=150, y=330)
        lab_4 = Label(img_frame1, text=" - By using Python Tkinter ", font=("Garamond", 20, 'italic'),
                      fg="#00ffee", bg="#2159ad")
        lab_4.place(x=800, y=590)

        button_frame = Frame(root, height=50, width=1200, bd=3, relief=SOLID)
        button_frame.place(x=0, y=750)
        slide1 = Button(button_frame, text="Next", command=slide_2, activebackground="cyan", activeforeground="red",
                        font=('ariel', 16, "italic"), bd=2, relief=SOLID, padx=100)
        slide1.place(x=455, y=1)


    slide_1()

    # Images
    modules = ImageTk.PhotoImage(Image.open("Img/Modules.jpg"))
    login_page = ImageTk.PhotoImage(Image.open("Img/Login.jpg"))
    nested = ImageTk.PhotoImage(Image.open("Img/NestedFun.jpg"))
    main = ImageTk.PhotoImage(Image.open("Img/MAin.jpg"))
    db_ = ImageTk.PhotoImage(Image.open("Img/DB.jpg"))
    image_bin_algo_ = ImageTk.PhotoImage(Image.open("Img/BinaryAlgo_.png"))
    image_bin_algo = ImageTk.PhotoImage(Image.open("Img/BinaryAlgo.png"))
    image_binary = ImageTk.PhotoImage(Image.open("Img/Update.jpg"))
    image_binary__tree = ImageTk.PhotoImage(Image.open("Img/History.jpg"))

    root.mainloop()
except Exception as Er:
    print(Er)
