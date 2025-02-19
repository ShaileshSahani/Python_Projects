from tkinter import *
from tkinter import ttk, messagebox as ms
import mysql.connector as conn
from random import choice, randint
from PIL import ImageTk, Image

try:
    db = conn.connect(host="localhost", user="root", password="root")
    cu = db.cursor()
    book_names = [
        "The Great Gatsby", "To Kill a Mockingbird", "1984", "The Catcher in the Rye",
        "Harry Potter and the Sorcerers Stone", "The Da Vinci Code", "The Hobbit", "The Lord of the Rings", "Sapiens",
        "Pride and Prejudice",
        "Brave New World", "Animal Farm", "Fahrenheit 451", "The Alchemist",
        "One Hundred Years of Solitude", "The Hitchhikers Guide to the Galaxy", "The Shining", "The Hunger Games",
        "A Tale of Two Cities", "The Brothers Karamazov", "The Grapes of Wrath", "Crime and Punishment",
        "The Chronicles of Narnia", "The Picture of Dorian Gray", "Lord of the Flies", "The Odyssey",
        "The Count of Monte", "War and Peace", "The Art of War", "Moby-Dick", "The Power of Habit",
        "Atlas Shrugged", "The Girl with the Dragon Tattoo",
        "Gone with the Wind", "The Road", "The Kite Runner", "The Divine Comedy",
        "Heights", "The Martian", "The Help", "The Silence of the Lambs", "Jurassic Park",
        "The Princess Bride", "The Color Purple", "The Three Musketeers", "The Joy Luck Club",
        "The Secret Garden", "The Fault in Our Stars", "The Old Man and the Sea", "Siddhartha",
        "The Bell Jar", "Dracula", "The Outsiders", "The Giver", "The Road Less Traveled",
        "A Clockwork Orange", "Down", "The Stand", "Les Miserables", "The Jungle",
        "The Wind in the Willows", "The Book Thief", "The Handmaids Tale", "The Girl on the Train",
        "East of Eden", "The Scarlet Letter", "Anna Karenina", "Catch-22",
        "Where the Red Fern Grows", "The Sun Also Rises", "The Wizard of Oz", "The Hound of the Gold",
        "The Iliad", "The Aeneid",
        "The Inferno", "The Canterbury Tales", "The Sound and the Fury", "All Quiet on the Western Front",
        "A Farewell to Arms", "The Glass Menagerie", "The Phantom of the Opera", "The War of the Worlds",
        "The Time Machine", "The Picture of Dorian Gray", "The Importance of Being Earnest", "The Jungle Book",
        "The Little Prince", "The Prince", "The Communist Manifesto", "The Republic", "The Art of War", "Meditations",
        "The Prince and the Pauper", "The Adventures of Sherlock Holmes",
        "The Arabian Nights", "The Swiss Family Robinson", "The Call of the Wild", "White Fang", "Treasure Island"
    ]
    author_names = [
        "Jane Austen", "George Orwell", "J.K. Rowling", "Dan Brown", "J.R.R. Tolkien", "Yuval Noah",
        "Charles", "Leo Tolstoy", "Jane Austen", "Aldous Huxley", "George Orwell", "Ray Bradbury",
        "Paulo Coelho", "Gabriel Garcia Marquez", "Douglas Adams", "Stephen King", "Suzanne Collins",
        "Charles Dickens", "Fyodor Dostoevsky", "John Steinbeck", "Fyodor Dostoevsky", "C.S. Lewis", "Oscar Wilde",
        "William Golding", "Homer", "Alexandre Dumas", "Leo Tolstoy", "Sun Tzu", "Herman Melville", "Ayn Rand",
        "Margaret Mitchell", "Khaled Hosseini", "Dante Alighieri",
        "Emily Bronte", "Andy Weir", "George Orwell", "Kathryn", "Thomas Harris",
        "Michael Crichton", "William Goldman", "Alice Walker", "Alexandre Dumas", "Amy Tan",
        "Frances Hodgson Burnett", "John Green", "Ernest Hemingway"
    ]
    book_types = ["Fiction", "Non-fiction", "Mystery", "Science Fiction", "Fantasy", "Biography", "History",
                  "Self-help", "Romance", "Thriller"]

    cu.execute("create database if not Exists library")
    cu.execute("use library")
    cu.execute("create table if not exists books(NAME varchar(60), Author varchar(60), Genre varchar(20),"
               " PRICE int, STOCK int)")


    def select():
        cu.execute("select * from books")
        return cu.fetchall()


    def bin_search(array, low, high, search):
        mid = (low + high) // 2
        if array[mid] == search:
            return mid
        elif low >= high:
            return -1
        elif array[mid] > search:
            return bin_search(array, low, mid - 1, search)
        elif array[mid] < search:
            return bin_search(array, mid + 1, high, search)


    def merge_sort(array):
        if len(array) > 1:
            l_half = array[:len(array) // 2:]
            r_half = array[len(array) // 2:]
            merge_sort(l_half)
            merge_sort(r_half)
            i = j = k = 0
            while i < len(l_half) and j < len(r_half):
                if l_half[i] <= r_half[j]:
                    array[k] = l_half[i]
                    i += 1
                else:
                    array[k] = r_half[j]
                    j += 1
                k += 1
            while i < len(l_half):
                array[k] = l_half[i]
                i += 1
                k += 1
            while j < len(r_half):
                array[k] = r_half[j]
                j += 1
                k += 1
        return array


    results = select()
    if len(results) == 0:
        for s in book_names:
            cu.execute(f"insert into books values('{s}', '{choice(author_names)}', '{choice(book_types)}', "
                       f"{choice([100, 200, 250, 300, 80, 500])}, {choice([randint(10, 50)])})")
            db.commit()


    def home_frame():

        def buy_book(event):

            def view_details():
                v1 = name.get()
                v2 = num.get()
                if v1 == "" or v1 == " ":
                    ms.showerror(message="Empty Fields!!!")
                    buy_but["state"] = DISABLED
                elif v1 == "" or v1 == " ":
                    ms.showerror(message="Enter number")
                    buy_but["state"] = DISABLED
                elif len(v2) != 10:
                    ms.showerror(message="Invalid number")
                else:
                    buy_but["state"] = ACTIVE
                    recip.delete("1.0", "end")
                    string_ = (f"Name: {v1}\nContact: {v2}\nBook Name: {values[0]}\nBook Author: {values[1]}"
                               f"\nGenre: {values[2]}\nPrice: {values[3]}")
                    recip.insert(END, string_)

            values = view.item(view.focus())["values"]

            def print_bill():
                recip.delete("1.0", END)

                he = Label(buy, text="Anjali's Library", font="ariel 20 bold", bg="#e0c494")
                he.place(x=340, y=330)
                l1 = Label(buy, text=f"Name: {name.get()}", font="ariel 15 bold", bg="#e0c494")
                l1.place(x=60, y=370)
                l2 = Label(buy, text=f"Contact: {num.get()}", font="ariel 15 bold", bg="#e0c494")
                l2.place(x=60, y=410)
                l3 = Label(buy, text=f"Book Name: {values[0]}", font="ariel 15 bold", bg="#e0c494")
                l3.place(x=60, y=450)
                l4 = Label(buy, text=f"Author: {values[1]}", font="ariel 15 bold", bg="#e0c494")
                l4.place(x=60, y=490)
                l5 = Label(buy, text=f"Genre: {values[2]}", font="ariel 15 bold", bg="#e0c494")
                l5.place(x=560, y=450)
                l6 = Label(buy, text=f"Price: {values[3]}", font="ariel 15 bold", bg="#e0c494")
                l6.place(x=560, y=490)
                buy_but["state"] = DISABLED

            if len(values) != 0:
                msg = ms.askyesno("Buying", f"Do You Want to buy this book??")
                if msg is True:
                    buy = Frame(body, height=540, width=900, bg="#e0c494")
                    buy.place(x=0, y=0)

                    n1 = Label(buy, text="Enter your name", font="Georgia 20 italic bold", padx=70)
                    n1.place(x=55, y=20)
                    name = StringVar()
                    e1 = Entry(buy, textvariable=name, font="Georgia 20 italic bold", width=20)
                    e1.place(x=55, y=70)

                    n2 = Label(buy, text="Enter your number", font="Georgia 20 italic bold", padx=55)
                    n2.place(x=55, y=135)
                    num = StringVar()
                    e2 = Entry(buy, textvariable=num, font="Georgia 20 italic bold", width=20)
                    e2.place(x=55, y=190)

                    button1 = Button(buy, text="Cancel", font="ariel 12 bold", padx=60, command=buy.destroy)
                    button1.place(x=55, y=240)
                    button2 = Button(buy, text="View details", font="ariel 12 bold", padx=38, command=view_details)
                    button2.place(x=260, y=240)

                    v_sep = ttk.Separator(buy, orient=VERTICAL)
                    v_sep.place(relx=0.55, rely=0, relwidth=0.003, relheight=0.52)

                    lab = Label(buy, text="Book details", font="Georgia 20 bold", padx=113, bd=2, relief=GROOVE)
                    lab.place(x=498, y=0)

                    recip = Text(buy, height=10, width=50, font="Ariel 16 bold", bg="lightBlue")
                    recip.place(x=498, y=37)

                    buy_but = Button(buy, text="Purchase this book", font="ariel 12 bold", padx=120,
                                     state=DISABLED, command=print_bill)
                    buy_but.place(x=498, y=248)

                    sep = ttk.Separator(buy, orient=HORIZONTAL)
                    sep.place(relx=0, rely=0.52, relwidth=3, relheight=0.005)

                    bill = Label(buy, text="Book Invoice", font="ariel 20 bold", padx=361, bd=2, relief=GROOVE)
                    bill.place(x=0, y=286)

        def select_values(columns, values):
            cu.execute(f"select * from books where {columns} = '{values}'")
            return cu.fetchall()

        def clear():
            for item in view.get_children():
                view.delete(item)

        def sorts(var):
            clear()
            values = []
            cu.execute(f"select {var.lower()} from books")
            for r in cu:
                values.append(r[0])
            values = merge_sort(values)
            for item in values:
                current = select_values(var, item)
                view.insert("", END, values=(current[0][0], current[0][1],
                                             current[0][2], current[0][3], current[0][4]))
            return values

        def search_values():
            val = find.get()
            if val == "" or val == " ":
                ms.showerror(message="Empty Filed")
            else:
                clear()
                cu.execute(f"select * from books where name like '%{val}%'")
                for i2 in cu:
                    view.insert("", END, values=(i2[0], i2[1], i2[2], i2[3], i2[4]))

        def bin_ser():
            val = find.get()
            if val == "" or val == " ":
                ms.showerror(message="Empty Filed")
            else:
                dataset = sorts("name")
                res = bin_search(dataset, 0, len(dataset) - 1, val)
                if res != -1:
                    ms.askyesno(message=f"The Book was found on number {res + 1}")
                else:
                    ms.showinfo(message="No book of this name")

        sea_bt = Menubutton(head, image=icon, bg="#baa077", activebackground="#baa077", bd=0)
        sea_bt.menu = Menu(sea_bt)
        sea_bt["menu"] = sea_bt.menu
        sea_bt.menu.add_command(label="Common Search", command=search_values, font="Ariel 12 bold")
        sea_bt.menu.add_command(label="Binary Search", command=bin_ser, font="Ariel 12 bold")
        sea_bt.place(x=727, y=13)

        data = Button(head, text="Sort", bd=2, relief=GROOVE, font="Georgia 15 bold", padx=17, bg="#d9aa84",
                      command=lambda: sorts("Name"))
        # data.menu = Menu(data)
        # data["menu"] = data.menu
        # data.menu.add_command(label="Name", font="Ariel 13 bold", command=lambda: sorts("Name"))
        # data.menu.add_command(label="Author", font="Ariel 13 bold", command=lambda: sorts("Author"))
        # data.menu.add_command(label="Price", font="Ariel 13 bold", command=lambda: sorts("Price"))
        # data.menu.add_command(label="Genre", font="Ariel 13 bold", command=lambda: sorts("Genre"))
        data.place(x=800, y=10)

        body = Frame(lib, height=540, width=900)
        scroll = ttk.Scrollbar(body)
        view = ttk.Treeview(body, columns=("NAME", "AUTHOR", "GENRE", "PRICE", "STOCK"), show="headings", height=25,
                            yscrollcommand=scroll.set)
        body.place(x=0, y=61)
        style.theme_use("clam")
        scroll.config(command=view.yview)
        style.configure("Treeview.Heading", background="#b6f2ee", font="Sarif 14 bold")
        style.configure("Treeview", font="Sarif 12 bold", background="#292827", foreground="white")
        view.column("NAME", width=316, stretch=False)
        view.heading(text="NAME", column="NAME")
        view.column("AUTHOR", width=176, stretch=False)
        view.heading(text="AUTHOR", column="AUTHOR")
        view.column("GENRE", width=176, stretch=False, anchor=CENTER)
        view.heading(text="GENRE", column="GENRE")
        view.column("PRICE", width=106, stretch=False, anchor=CENTER)
        view.heading(text="PRICE", column="PRICE")
        view.column("STOCK", width=106, stretch=False, anchor=CENTER)
        view.heading(text="STOCK", column="STOCK")
        view.pack(side=LEFT, fill=Y)
        scroll.pack(side=RIGHT, fill=Y)
        for i in results:
            view.insert("", END, values=(i[0], i[1], i[2], i[3], i[4]))
        view.bind("<ButtonRelease>", buy_book)


    def sales_frame():
        sales = Frame(lib, height=540, width=900)
        sales.place(x=0, y=61)


    lib = Tk()
    lib.title("Anjali's Library")
    lib.wm_minsize(900, 600)
    lib.wm_maxsize(900, 600)
    style = ttk.Style()

    logo = ImageTk.PhotoImage(Image.open("Images/library.jpg"))
    head = Frame(lib, height=60, width=900, bg="#d9aa84")
    head.place(x=0, y=0)

    head_logo = Label(head, image=logo, bd=0, bg="#d9aa84")
    head_logo.place(x=20, y=0)

    home = Button(head, text="Home", font="Georgia 18 bold", bd=0, bg="#d9aa84", fg="Blue", activebackground="skyBlue",
                  command=home_frame)
    home.place(x=140, y=8)

    sale = Button(head, text="Sales", font="Georgia 18 bold", bd=0, bg="#d9aa84", activebackground="aqua",
                  command=sales_frame)
    sale.place(x=270, y=8)

    find = StringVar()
    ser = Entry(head, textvariable=find, font="Georgia 25 bold", width=16, bg="#baa077")
    ser.place(x=400, y=10)

    icon = ImageTk.PhotoImage(Image.open("Images/SEARCH.ico"))
    home_frame()
    lib.mainloop()
except Exception as e:
    ms.showerror("Error", f"Error While Connection {e}")
