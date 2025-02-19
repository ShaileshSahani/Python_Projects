import webbrowser
from tkinter import *
from tkinter import messagebox as msg
from PIL import ImageTk, Image

try:
    root = Tk()
    root.minsize(1000, 700)
    root.maxsize(1000, 700)


    def toggle():
        if var.winfo_ismapped():
            var.place_forget()
        else:
            var.place(x=0, y=62)


    def frame_maker(master, x, y, text):
        cards = Frame(master, width=180, height=280, bg="grey", bd=2, relief=SOLID)
        lab = Label(cards)
        lab.place(x=0, y=0)
        te = Label(cards, image=text)
        te.place(x=10, y=0)
        cards.place(x=x, y=y)


    def check_active_frame(frame_name):
        if frame_name.winfo_ismapped():
            frame_name.place_forget()
        else:
            frame_name.place(x=0, y=125)


    def disable_if_active_frame(f1, f2, f3, f4, f5, f6, f7):
        if (f1.winfo_ismapped() or f2
                or f3.winfo_ismapped() or f4.winfo_ismapped() or f5.winfo_ismapped()
                or f7.winfo_ismapped() or f7.winfo_ismapped()):
            f1.place_forget()
            f2.place_forget()
            f3.place_forget()
            f4.place_forget()
            f5.place_forget()
            f6.place_forget()
            f7.place_forget()


    def phone_frame():
        disable_if_active_frame(histories, book, carts, watches, sale, computers, tvs)
        check_active_frame(mobiles)


    def history_frame():
        disable_if_active_frame(mobiles, book, carts, watches, sale, computers, tvs)
        check_active_frame(histories)


    def cart_frame():
        disable_if_active_frame(histories, book, mobiles, watches, sale, computers, tvs)
        check_active_frame(carts)


    def sales_frame():
        disable_if_active_frame(histories, book, carts, watches, mobiles, computers, tvs)
        check_active_frame(sale)


    def watch_frame():
        disable_if_active_frame(histories, book, carts, sale, computers, tvs, mobiles)
        check_active_frame(watches)


    def tv_frame():
        disable_if_active_frame(histories, book, carts, watches, sale, computers, mobiles)
        check_active_frame(tvs)


    def books_frame():
        disable_if_active_frame(histories, mobiles, carts, watches, sale, computers, tvs)
        check_active_frame(book)

    def computer_frame():
        disable_if_active_frame(histories, book, carts, watches, sale, mobiles, tvs)
        check_active_frame(computers)


    def home_frame():
        if (mobiles.winfo_ismapped() or histories.winfo_ismapped() or book.winfo_ismapped()
                or carts.winfo_ismapped() or watches.winfo_ismapped() or sale.winfo_ismapped()
                or computers.winfo_ismapped() or tvs.winfo_ismapped()):
            mobiles.place_forget()
            tvs.place_forget()
            histories.place_forget()
            book.place_forget()
            carts.place_forget()
            watches.place_forget()
            sale.place_forget()
            computers.place_forget()


    # Home Frame
    head = Label(root, text="Super E-Com", bg="#9D9C9A", fg="purple", font="Ariel 30 bold",
                 padx=372, bd=3, relief="groove", pady=6)
    head.place(x=0, y=0)

    user = ImageTk.PhotoImage(Image.open("Images/user.ico"))
    login = Button(root, image=user, bg="#9D9C9A", bd=0, activebackground="#9D9C9A")
    login.place(x=930, y=5)

    img = ImageTk.PhotoImage(Image.open("Images/menu.ico"))
    tog = Button(root, image=img, command=toggle, bd=0, bg="#9D9C9A", activebackground="#9D9C9A")
    tog.place(x=13, y=8)

    # All Frames
    mobiles = Frame(root, height=574, width=1000, bg="blue", relief=GROOVE, bd=3)
    tvs = Frame(root, height=574, width=1000, bg="red", relief=GROOVE, bd=3)
    watches = Frame(root, height=574, width=1000, bg="green", relief=GROOVE, bd=3)
    histories = Frame(root, height=574, width=1000, bg="yellow", relief=GROOVE, bd=3)
    book = Frame(root, height=574, width=1000, bg="black", relief=GROOVE, bd=3)
    sale = Frame(root, height=574, width=1000, bg="grey", relief=GROOVE, bd=3)
    carts = Frame(root, height=574, width=1000, bg="orange", relief=GROOVE, bd=3)
    computers = Frame(root, height=574, width=1000, bg="aqua", relief=GROOVE, bd=3)

    # search Menu
    search_Frame = Frame(root, height=65, width=1000, bg="#42e2ed", bd=2, relief=GROOVE)
    search_Frame.place(x=0, y=62)
    search_ico = ImageTk.PhotoImage(Image.open("Images/search.png"))
    link = ImageTk.PhotoImage(Image.open("Images/link.png"))
    website = Button(search_Frame, text="Website         ", font="corbel 12 bold",
                     pady=4.5, bg="#ed574a", activebackground="#ed574a",
                     command=lambda: webbrowser.open("https://www.amazon.com/"))
    website.place(x=0, y=10)
    link_lab = Button(search_Frame, image=link, activebackground="#ed574a", bd=0, bg="#ed574a",
                      command=lambda: webbrowser.open("https://www.amazon.com/"))
    link_lab.place(x=64, y=15)
    search_input = Entry(search_Frame, font="corbel 22 bold", width=50)
    search_input.place(x=103, y=10)
    search_button = Button(search_Frame, image=search_ico, bd=0)
    search_button.place(relx=0.823, rely=0.2)
    insta = ImageTk.PhotoImage(Image.open("Images/insta.png"))
    face = ImageTk.PhotoImage(Image.open("Images/facebook.png"))
    tele = ImageTk.PhotoImage(Image.open("Images/telegram.png"))
    insta_button = Button(search_Frame, image=insta, bd=0, bg="#42e2ed", activebackground="#42e2ed",
                          command=lambda: webbrowser.open("https://www.instagram.com/"))
    face_button = Button(search_Frame, image=face, bd=0, bg="#42e2ed", activebackground="#42e2ed",
                         command=lambda: webbrowser.open("https://www.facebook.com/"))
    tele_button = Button(search_Frame, image=tele, bd=0, bg="#42e2ed", activebackground="#42e2ed",
                         command=lambda: webbrowser.open("https://web.telegram.org/a/"))
    insta_button.place(x=860, rely=0.2)
    face_button.place(x=905, rely=0.2)
    tele_button.place(x=950, rely=0.2)

    poco = ImageTk.PhotoImage(Image.open("Items/Mobile/poco.jpg"))
    redmi = ImageTk.PhotoImage(Image.open("Items/Mobile/redmi.jpg"))

    # Side Menu
    var = Frame(root, height=640, width=75, bg="#70e0d7", bd=1, relief=GROOVE)

    sales = ImageTk.PhotoImage(Image.open("Images/sales.png"))
    mobile = ImageTk.PhotoImage(Image.open("Images/pixel.png"))
    history = ImageTk.PhotoImage(Image.open("Images/history.png"))
    home = ImageTk.PhotoImage(Image.open("Images/home.png"))
    tv = ImageTk.PhotoImage(Image.open("Images/tv.png"))
    watch = ImageTk.PhotoImage(Image.open("Images/watch.png"))
    cart = ImageTk.PhotoImage(Image.open("Images/cart.png"))
    computer = ImageTk.PhotoImage(Image.open("Images/computer.png"))
    books = ImageTk.PhotoImage(Image.open("Images/books.png"))
    exit_ = ImageTk.PhotoImage(Image.open("Images/exit.png"))

    b1 = Button(var, image=home, command=home_frame)
    b1.place(x=9, y=10)
    b2 = Button(var, image=tv, command=tv_frame)
    b2.place(x=9, y=72)
    b3 = Button(var, image=watch, command=watch_frame)
    b3.place(x=9, y=134)
    b4 = Button(var, image=mobile, command=phone_frame)
    b4.place(x=9, y=196)
    b5 = Button(var, image=computer, command=computer_frame)
    b5.place(x=9, y=258)
    b6 = Button(var, image=books, command=books_frame)
    b6.place(x=9, y=320)
    b7 = Button(var, image=sales, command=sales_frame)
    b7.place(x=9, y=382)
    b8 = Button(var, image=history, command=history_frame)
    b8.place(x=9, y=444)
    b9 = Button(var, image=cart, command=cart_frame)
    b9.place(x=9, y=506)
    b10 = Button(var, image=exit_, command=root.destroy)
    b10.place(x=9, y=568)

    # Frames
    root.mainloop()
except Exception as E:
    msg.showerror(str(E))
