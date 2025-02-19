import datetime
import os
from tkinter import *
import mysql.connector as conn
from tkinter import ttk, messagebox as msg
from PIL import ImageTk, Image
import pandas as pd

try:
    db = conn.connect(host="localhost", user="root", password="root")
    cu = db.cursor()
    cu.execute("CREATE DATABASE IF NOT EXISTS surya")
    cu.execute("USE surya")
    cu.execute("CREATE TABLE IF NOT EXISTS campaign(CAMPAIGN_START date, CAMPAIGN_END date,"
               " CAMPAIGN_TARGET int, DAYS int)")
    cu.execute("CREATE TABLE IF NOT EXISTS entries(SR_NO int PRIMARY KEY AUTO_INCREMENT,"
               " NAME varchar(50), AGE tinyint, SURYA_NAMASKAR smallint)")
    root = Tk()
    root.title("Surya Namaskar Application")
    root.minsize(1000, 700)
    root.maxsize(1000, 700)
    logo = ImageTk.PhotoImage(Image.open('om.png'))
    logoLg = ImageTk.PhotoImage(Image.open('large.png'))
    cu.execute("SELECT * FROM campaign")
    data = cu.fetchall()


    def initializer():
        def start_app():
            days = date.get()
            tar__ = target.get()
            if not days or not tar__:
                msg.showerror(message="Fields are Empty")
            elif not tar__.isnumeric() or not days.isnumeric():
                msg.showerror(message="Enter a Number")
            else:
                today = datetime.date.today()
                end = today + datetime.timedelta(days=int(days))
                cu.execute(f"INSERT INTO campaign values('{today}', '{end}', {int(tar__)}, {int(days)})")
                db.commit()
                msg.showinfo(message="success insertion")
                frame1.place_forget()
                main_frame_app()

        frame1 = Frame(root, height=700, width=1000, bg="#6cc1e6")
        frame1.place(x=0, y=0)

        head = Label(frame1, text="Surya Namaskar Application", font="NewRomanTimes 30",
                     padx=249, pady=15, bd=3, relief=GROOVE)
        head.place(x=0, y=0)

        logo_lab = Label(frame1, image=logoLg, bg="#6cc1e6")
        logo_lab.place(x=430, y=100)

        l1 = Label(frame1, text="Enter No. of Days", font="NewRomanTimes 20", padx=102, bd=2, relief=GROOVE)
        l1.place(x=280, y=240)
        date = StringVar()
        e1 = Entry(frame1, textvariable=date, font="NewRomanTimes 20", width=28, bd=2, relief=GROOVE)
        e1.place(x=280, y=290)

        l2 = Label(frame1, text="Enter Surya Namaskar Target", font="NewRomanTimes 20", padx=29, bd=2, relief=GROOVE)
        l2.place(x=280, y=400)
        target = StringVar()
        e2 = Entry(frame1, textvariable=target, font="NewRomanTimes 20", width=28, bd=2, relief=GROOVE)
        e2.place(x=280, y=450)

        button = Button(frame1, text="Start", font="NewRomanTimes 15 bold", width=35, fg="Green", command=start_app)
        button.place(x=278, y=550)


    def main_frame_app():
        def get_tot():
            cu.execute("SELECT SURYA_NAMASKAR FROM entries")
            num = cu.fetchall()
            tot = 0
            for i_ in range(len(num)):
                tot += num[i_][0]
            return tot

        cu.execute("SELECT * FROM campaign")
        data_now = cu.fetchall()
        date_obj = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").date()
        remain = (data_now[0][1] - date_obj).days

        def insert():
            n = name.get()
            a = age.get()
            c = count.get()
            if not n or not a or not c:
                msg.showerror("Error", "No Entries")
            elif not a.isnumeric() or not c.isnumeric():
                msg.showerror("Error", "Enter a number")
            elif int(a) > 120:
                msg.showerror("Error", "Invalid Age")
            else:
                cu.execute(f"INSERT INTO entries(NAME, AGE, SURYA_NAMASKAR) values"
                           f"('{n}', {a}, {c})")
                db.commit()
                cu.execute("SELECT * FROM entries ORDER BY SR_NO DESC LIMIT 1")
                current = cu.fetchall()[0]
                view.insert("", END, values=(current[0], current[1], current[2], current[3]))
                c1.config(text=f"Total No: {get_tot()}")
                msg.showinfo("Success", "Inserted Successfully")
                name.set("")
                age.set("")
                count.set("")

        def delete():
            cu.execute("Delete from entries")
            view.delete(*view.get_children())

        def exel():
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

            file_path = os.path.join(downloads_path, "output.xlsx")
            cu.execute("SELECT * FROM entries")
            d = cu.fetchall()
            name_ = []
            age_ = []
            count_ = []
            for s in range(len(d)):
                name_.append(d[s][1])
                age_.append(d[s][2])
                count_.append(d[s][3])
            ex = {
                "NAME": name_,
                "AGE": age_,
                "COUNT": count_
            }
            df = pd.DataFrame(ex)
            try:
                df.to_excel(file_path, index=False, engine="openpyxl")
                msg.showinfo("MSG", "Created")
            except Exception as e:
                print(e)

        def restart():
            cu.execute("Delete from campaign")
            cu.execute("DELETE from entries")
            db.commit()
            initializer()

        root.config(bg="#e6dfd8")
        header = Label(root, text="Surya Namaskar Counter", font="NewRomanTimes 30",
                       padx=275, pady=15, bd=3, relief=GROOVE, bg="#f09d4a")
        header.place(x=0, y=0)
        logo_sm = Label(header, image=logo, bg="#f09d4a")
        logo_sm.place(x=10, y=0)

        add = Label(root, text="ADD COUNT", font="NewRomanTimes 25", padx=49, bd=2, relief=GROOVE)
        add.place(x=0, y=80)

        name_lab = Label(root, text="NAME", font="NewRomanTimes 20", padx=97, bd=2, relief=GROOVE)
        name_lab.place(x=12, y=130)
        name = StringVar()
        name_en = Entry(root, textvariable=name, font="NewRomanTimes 20", bd=2, relief=GROOVE, width=18)
        name_en.place(x=12, y=180)

        age_lab = Label(root, text="AGE", font="NewRomanTimes 20", padx=107, bd=2, relief=GROOVE)
        age_lab.place(x=12, y=250)
        age = StringVar()
        age_en = Entry(root, textvariable=age, font="NewRomanTimes 20", bd=2, relief=GROOVE, width=18)
        age_en.place(x=12, y=300)

        count_lab = Label(root, text="Count", font="NewRomanTimes 20", padx=99, bd=2, relief=GROOVE)
        count_lab.place(x=12, y=370)
        count = StringVar()
        count_en = Entry(root, textvariable=count, font="NewRomanTimes 20", bd=2, relief=GROOVE, width=18)
        count_en.place(x=12, y=420)

        submit = Button(root, text="Submit", font="NewRomanTimes 15", padx=100, command=insert)
        submit.place(x=12, y=479)

        tree = Frame(root, height=400, width=700, bd=2, relief=GROOVE)
        tree.place(x=300, y=80)
        style = ttk.Style()
        scroll = ttk.Scrollbar(tree)
        view = ttk.Treeview(tree, columns=("SR_NO", "NAME", "AGE", "SURYA NAMASKAR"), show="headings", height=20,
                            yscrollcommand=scroll.set)
        style.theme_use("clam")
        scroll.config(command=view.yview)
        style.configure("Treeview.Heading", background="#b6f2ee", font="Sarif 14 bold")
        style.configure("Treeview", font="Sarif 12 bold", background="#e6dfd8", foreground="black")
        view.column("SR_NO", width=120, stretch=False, anchor=CENTER)
        view.heading(text="SR_NO", column="SR_NO")
        view.column("NAME", width=220, stretch=False, anchor=CENTER)
        view.heading(text="NAME", column="NAME")
        view.column("AGE", width=120, stretch=False, anchor=CENTER)
        view.heading(text="AGE", column="AGE")
        view.column("SURYA NAMASKAR", width=218, stretch=False, anchor=CENTER)
        view.heading(text="SURYA NAMASKAR", column="SURYA NAMASKAR")
        view.pack(side=LEFT, fill=Y)
        scroll.pack(side=RIGHT, fill=Y)
        cu.execute("select * from entries")
        for i in cu:
            view.insert("", END, values=(i[0], i[1], i[2], i[3]))

        bottom = Frame(root, height=175, width=1000, bd=3, relief=GROOVE, bg="#f09d4a")
        bottom.place(x=0, y=525)

        s1 = Label(bottom, text=f"Start Date: {data_now[0][0]}", font="NewRomanTimes 20", bd=2, relief=GROOVE)
        s1.place(x=0, y=0)
        e1 = Label(bottom, text=f"End Date: {data_now[0][1]}", font="NewRomanTimes 20", bd=2, relief=GROOVE)
        e1.place(x=0, y=65)
        d1 = Label(bottom, text=f"Total Days: {data_now[0][3]}", font="NewRomanTimes 20", bd=2, relief=GROOVE)
        d1.place(x=0, y=130)
        t1 = Label(bottom, text=f"Target: {data_now[0][2]}", font="NewRomanTimes 20", bd=2, relief=GROOVE)
        t1.place(x=350, y=0)

        c1 = Label(bottom, text=f"Total No: {get_tot()}", font="NewRomanTimes 20", bd=2, relief=GROOVE)
        c1.place(x=350, y=65)
        c2 = Label(bottom, text=f"Days Remain: {remain}", font="NewRomanTimes 20", bd=2, relief=GROOVE)
        c2.place(x=350, y=130)
        b1 = Button(bottom, text=f"Restart Campaign", font="NewRomanTimes 14", padx=79, command=restart)
        b1.place(x=670, y=0)
        b2 = Button(bottom, text=f"Delete All", font="NewRomanTimes 14", padx=114, command=delete)
        b2.place(x=670, y=43)
        b3 = Button(bottom, text="Generate ExcelSheet", font="NewRomanTimes 14", padx=65, command=exel)
        b3.place(x=670, y=86)
        b4 = Button(bottom, text="Exit", font="NewRomanTimes 14", padx=140, command=root.destroy)
        b4.place(x=670, y=130)


    if len(data) == 0:
        initializer()
    elif data[0][0] == data[0][1]:
        cu.execute("DELETE FROM campaign")
        cu.execute("DELETE FROM entries")
        initializer()
    else:
        main_frame_app()
    root.mainloop()
except Exception as E:
    msg.showerror(title="Initialization", message=f"{str(E)}")
