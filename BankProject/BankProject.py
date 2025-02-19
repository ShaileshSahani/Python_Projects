import mysql.connector
from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk
import datetime
from random import randint
import webbrowser as w
import time as stm

try:
    db = mysql.connector.connect(host='localhost', user='root', password='root')
    cu = db.cursor()
    database = []
    cu.execute("SHOW databases")
    for i in cu:
        database.append(i[0])
    if 'bank' in database:
        pass
    else:
        cu.execute('CREATE DATABASE bank')

    if 'transaction' in database:
        cu.execute('USE transaction')
    else:
        cu.execute('CREATE DATABASE transaction')

    if 'account' in database:
        pass
    else:
        cu.execute('CREATE DATABASE account')

    table = []
    cu.execute('Use Bank')
    cu.execute("SHOW TABLES")
    for i in cu:
        table.append(i[0])
    if 'signup' in table:
        pass
    else:
        cu.execute("use bank")
        cu.execute("create table signup(UserID int primary key AUTO_INCREMENT, Username varchar(30),"
                   "Password varchar(30))")
    cu.execute('use account')
    cu.execute("SHOW TABLES")
    for i in cu:
        table.append(i[0])
    if 'user_details' in table:
        pass
    else:
        cu.execute("use account")
        cu.execute("create table user_details(UserID int primary key AUTO_INCREMENT,F_Name char(30),M_Name char(30),"
                   "L_Name char(30),Age tinyint,Gender char(10),Account_Type char(10),Phone bigint,"
                   "G_mail varchar(40),City varchar(30),Aadhar_No varchar(12), PAN_No varchar(30),"
                   " Balance bigint, Password varchar(20))")


except Exception as error:
    print(error)

li = ['0']
t = []


def web():
    w.open('file:///C:/Users/USER/.vscode/projectWD/')


def login():
    info = []
    info_pass = []

    def otp():
        str1 = ''
        for i1 in range(4):
            str1 += str(randint(0, 9))
        li.append(str1)
        li[0] = str1
        msg.showinfo(title="OPT", message=f"Your 4-Digit OPT\n{str1}")

    global cu
    lg = s.get()
    ps = s1.get()
    otp1 = s2.get()
    cu.execute('use bank')
    cu.execute('select * from signup')
    for i3 in cu:
        info.append(i3[1])
    if lg == '':
        ur2.config(text="")
        ur1.config(text="username column cannot be Empty !!", fg="red", bg="#4f9491")
    elif lg not in info:
        ur2.config(text="")
        ur1.config(text="Username doesn't Exist, Sign Up to Create an Account", fg="red", bg="#4f9491")
    elif lg in info:
        cu.execute('use bank')
        cu.execute(f'select Password from signup where Username="{lg}"')
        for i3 in cu:
            info_pass.append(i3[0])
        if ps == '':
            ur1.config(text='')
            ur2.config(text="Password field cannot be empty!!", fg='red', bg="#4f9491")
        elif ps != info_pass[0]:
            ur1.config(text='')
            ur2.config(text="The Password you Entered Is Incorrect!!", fg='red', bg="#4f9491")
        elif otp1 == '':
            ur1.config(text='')
            ur2.config(text="")
            otp = Button(top, text="Send OTP", command=otp, activebackground="aqua", bg="Black", padx=10,
                         fg="White", font=("Arial", 13))
            otp.place(x=285, y=400)
        elif otp1 != li[0]:
            ur1.config(text='')
            ur2.config(text="")
            ur3.config(text='')
            msg.showerror(title="otp", message='Incorrect OTP!!')
        else:
            ur3.config(text='')
            ur1.config(text='')
            ur2.config(text='')
            usr = msg.askyesno(title="Save", message="Login Successful")
            if usr is True:
                top.destroy()
                transaction(lg)


exp = ''


def transaction(name):
    global cu

    cu.execute("use bank")
    val_s = []
    cu.execute(f"select UserId from signup where Username='{name}'")
    for itr in cu:
        val_s.append(itr[0])
    val_s1 = val_s[0]

    def transfer():
        time = datetime.datetime.now()
        dt = time.date()
        tm = stm.localtime()
        now = stm.strftime('%H:%M:%S', tm)

        date_time = str(dt) + ' ' + str(now)

        new_password = []
        cu.execute('use account')
        cu.execute(f"select Password from user_details where UserID={val_s1}")
        for i8 in cu:
            new_password.append(i8[0])
        new_password1 = new_password[0]
        val_balance = []
        cu.execute('use account')
        cu.execute(f"select Balance from user_details where UserID={val_s1}")
        for itr1 in cu:
            val_balance.append(itr1[0])
        val_b1 = val_balance[0]

        val_1 = des.get()
        val_2 = t_amt.get()
        val_3 = password_val.get()

        if val_1 == '':
            msg.showerror(title="Error", message='UPI-ID / Number / Account_No is Required for Transaction')
        elif len(val_1) < 10:
            msg.showerror(title="Error", message='Entered UPI-ID / Number / Account_No is Invalid Or Unavailable')
        elif val_2 == '' or val_2 == 0:
            msg.showerror(title="Amount Error", message="Enter At least 1 Rs")
        elif val_3 == '':
            msg.showerror(title="Password", message="Password is Required for Transaction")
        elif val_3 != new_password1:
            msg.showerror(title="Password", message="The Password You Entered Is Incorrect")
        elif val_3 == new_password1:
            if val_2 > int(val_b1):
                msg.showerror(title="Amount", message="Insufficient Balance")
            else:
                max1 = [0]
                remain_amt = val_b1 - val_2
                cu.execute('use account')
                cu.execute(f'UPDATE user_details SET Balance={remain_amt} WHERE UserID={val_s1}')
                db.commit()
                cu.execute("use transaction")
                cu.execute(f'Insert into {name} (Date_Time,Description,Debit,Balance) values(%s,%s,%s,%s)',
                           (date_time, val_1, val_2, remain_amt))
                db.commit()
                msg.showinfo(title="Transaction Details", message=f"Rs.{val_2} Debited AT {date_time}\n"
                                                                  f"Balance-Remaining {remain_amt}")
                cu.execute("use transaction")
                cu.execute(f"Select Transaction_No from {name}")
                for i6 in cu:
                    max1.append(i6[0])
                max_val = max(max1)
                cu.execute(f'select * from {name} where Transaction_No={max_val}')
                ins1 = []
                ins2 = []
                ins3 = []
                ins4 = []
                ins5 = []
                for ins in cu:
                    ins1.append(ins[1])
                    ins2.append(ins[2])
                    ins3.append(ins[3])
                    ins4.append(ins[4])
                    ins5.append(ins[5])
                    trans.insert('', END, values=(f'{ins[1]}', f'{ins[2]}', f'{ins[3]}', f'{ins[4]}', f'{ins[5]}'))
                des.set('')
                t_amt.set(0)
                password_val.set('')

    def deposit():
        time = datetime.datetime.now()
        dt = time.date()
        tm = stm.localtime()
        now = stm.strftime('%H:%M:%S', tm)

        date_time = str(dt) + ' ' + str(now)

        new_password = []
        cu.execute('use account')
        cu.execute(f"select Password from user_details where UserID={val_s1}")
        for i8 in cu:
            new_password.append(i8[0])
        new_password1 = new_password[0]
        val_balance = []
        cu.execute('use account')
        cu.execute(f"select Balance from user_details where UserID={val_s1}")
        for itr1 in cu:
            val_balance.append(itr1[0])
        val_b1 = val_balance[0]
        des.set("Self Deposit")
        val_1 = des.get()
        val_2 = t_amt.get()
        val_3 = password_val.get()

        if val_2 == '' or val_2 == 0:
            msg.showerror(title="Amount Error", message="Enter At least 1 Rs")
        elif val_3 == '':
            msg.showerror(title="Password", message="Password is Required for Transaction")
        elif val_3 != new_password1:
            msg.showerror(title="Password", message="The Password You Entered Is Incorrect")
        elif val_3 == new_password1:
            max1 = [0]
            remain_amt = val_b1 + val_2
            cu.execute('use account')
            cu.execute(f'UPDATE user_details SET Balance={remain_amt} WHERE UserID={val_s1}')
            db.commit()
            cu.execute("use transaction")
            cu.execute(f'Insert into {name} (Date_Time,Description,Credit,Balance) values(%s,%s,%s,%s)',
                       (date_time, val_1, val_2, remain_amt))
            db.commit()
            msg.showinfo(title="Transaction Details", message=f"Rs.{val_2} Credited AT {date_time}\n"
                                                              f"Balance-Remaining {remain_amt}")
            cu.execute("use transaction")
            cu.execute(f"Select Transaction_No from {name}")
            for i6 in cu:
                max1.append(i6[0])
            max_val = max(max1)
            cu.execute(f'select * from {name} where Transaction_No={max_val}')
            ins1 = []
            ins2 = []
            ins3 = []
            ins4 = []
            ins5 = []
            for ins in cu:
                ins1.append(ins[1])
                ins2.append(ins[2])
                ins3.append(ins[3])
                ins4.append(ins[4])
                ins5.append(ins[5])
                trans.insert('', END, values=(f'{ins[1]}', f'{ins[2]}', f'{ins[3]}', f'{ins[4]}', f'{ins[5]}'))
            des.set('')
            t_amt.set(0)
            password_val.set('')

    def withdraw():
        time = datetime.datetime.now()
        dt = time.date()
        tm = stm.localtime()
        now = stm.strftime('%H:%M:%S', tm)

        date_time = str(dt) + ' ' + str(now)

        new_password = []
        cu.execute('use account')
        cu.execute(f"select Password from user_details where UserID={val_s1}")
        for i8 in cu:
            new_password.append(i8[0])
        new_password1 = new_password[0]
        val_balance = []
        cu.execute('use account')
        cu.execute(f"select Balance from user_details where UserID={val_s1}")
        for itr1 in cu:
            val_balance.append(itr1[0])
        val_b1 = val_balance[0]

        des.set("Self Withdraw")
        val_1 = des.get()
        val_2 = t_amt.get()
        val_3 = password_val.get()

        if val_2 == '' or val_2 == 0:
            msg.showerror(title="Amount Error", message="Enter At least 1 Rs")
        elif val_3 == '':
            msg.showerror(title="Password", message="Password is Required for Transaction")
        elif val_3 != new_password1:
            msg.showerror(title="Password", message="The Password You Entered Is Incorrect")
        elif val_3 == new_password1:
            if val_2 > int(val_b1):
                msg.showerror(title="Amount", message="Insufficient Balance")
            else:
                max1 = [0]
                remain_amt = val_b1 - val_2
                cu.execute('use account')
                cu.execute(f'UPDATE user_details SET Balance={remain_amt} WHERE UserID={val_s1}')
                db.commit()
                cu.execute("use transaction")
                cu.execute(f'Insert into {name} (Date_Time,Description,Debit,Balance) values(%s,%s,%s,%s)',
                           (date_time, val_1, val_2, remain_amt))
                db.commit()
                msg.showinfo(title="Transaction Details", message=f"Rs.{val_2} Debited AT {date_time}\n"
                                                                  f"Balance-Remaining {remain_amt}")
                cu.execute("use transaction")
                cu.execute(f"Select Transaction_No from {name}")
                for i6 in cu:
                    max1.append(i6[0])
                max_val = max(max1)
                cu.execute(f'select * from {name} where Transaction_No={max_val}')
                ins1 = []
                ins2 = []
                ins3 = []
                ins4 = []
                ins5 = []
                for ins in cu:
                    ins1.append(ins[1])
                    ins2.append(ins[2])
                    ins3.append(ins[3])
                    ins4.append(ins[4])
                    ins5.append(ins[5])
                    trans.insert('', END, values=(f'{ins[1]}', f'{ins[2]}', f'{ins[3]}', f'{ins[4]}', f'{ins[5]}'))
                des.set('')
                t_amt.set(0)
                password_val.set('')

    def number(x):
        global exp

        exp = exp + str(x)
        password_val.set(exp)

    def clear():
        global exp
        exp = ''
        password_val.set('')

    def check_bal():
        bal_val = []
        cu.execute('use account')
        cu.execute(f"select Balance from user_details where UserID={val_s1}")
        for i7 in cu:
            bal_val.append(i7[0])
        new_balance = bal_val[0]
        label_1.config(text=f"Rs. {new_balance}")

    def update_name():
        def update():
            v1 = lab_name.get()
            if v1 == "":
                msg.showerror(message="The Name Field is Empty")
            else:
                value = msg.askyesno(title="Update Information", message="Are you sure Want To Update Your Name.?")
                if value is True:
                    cu.execute("use account")
                    cu.execute(f"update user_details set F_name='{v1}' where UserID={val_s1}")
                    label_3.config(text=v1)
                    lab_name.set('')
                    db.commit()
                    msg.showinfo(message="Data Updated Successfully")

        lab12.config(text="Enter New Name")
        lab_name = StringVar()
        lab_en = Entry(frame5, font=('Ariel', 14, 'bold'), width=25, bg='SkyBlue', textvariable=lab_name,
                       relief=GROOVE, highlightthickness=2, highlightcolor='green')
        lab_en.place(x=205, y=200)

        update_but = Button(frame5, text="Update", command=update)
        update_but.place(x=10, y=240)

    def update_number():
        def update():
            v1 = lab_name.get()
            if v1 == "":
                msg.showerror(message="The Number Field is Empty")
            elif len(v1) != 10:
                msg.showerror(message="The Number must Contain 10 Digits Only")
            else:
                value = msg.askyesno(title="Update Information",
                                     message="Are you sure Want To Update Your Phone Number.?")
                if value is True:
                    cu.execute("use account")
                    cu.execute(f"update user_details set Phone='{v1}' where UserID={val_s1}")
                    label_6.config(text=v1)
                    lab_name.set('')
                    db.commit()
                    msg.showinfo(message="Data Updated Successfully")

        lab12.config(text="Enter New Number")
        lab_name = StringVar()
        lab_en = Entry(frame5, font=('Ariel', 14, 'bold'), width=25, bg='SkyBlue', textvariable=lab_name,
                       relief=GROOVE, highlightthickness=2, highlightcolor='green')
        lab_en.place(x=205, y=200)

        update_but = Button(frame5, text="Update", command=update)
        update_but.place(x=10, y=240)

    def update_e_mail():
        def update():
            list23 = []
            v1 = lab_name.get()
            for i7 in v1:
                list23.append(i7)
            if v1 == "":
                msg.showerror(message="The G_mail Field is Empty")
            elif "@" and 'g' and 'm' and 'a' and 'i' and 'l' and '.' not in list23:
                msg.showerror(title='Error', message='Invalid G-Mail Address')
            else:
                value = msg.askyesno(title="Update Information",
                                     message="Are you sure Want To Update Your G_mail Address.?")
                if value is True:
                    cu.execute("use account")
                    cu.execute(f"update user_details set G_mail='{v1}' where UserID={val_s1}")
                    label_8.config(text=v1)
                    lab_name.set('')
                    db.commit()
                    msg.showinfo(message="Data Updated Successfully")

        lab12.config(text="Enter New G_mail")
        lab_name = StringVar()
        lab_en = Entry(frame5, font=('Ariel', 14, 'bold'), width=25, bg='SkyBlue', textvariable=lab_name,
                       relief=GROOVE, highlightthickness=2, highlightcolor='green')
        lab_en.place(x=205, y=200)

        update_but = Button(frame5, text="Update", command=update)
        update_but.place(x=10, y=240)

    def update_city():
        def update():
            v1 = lab_name.get()
            if v1 == "":
                msg.showerror(message="Enter a City Name")
            else:
                value = msg.askyesno(title="Update Information", message="Are you sure Want To Update Your City.?")
                if value is True:
                    cu.execute("use account")
                    cu.execute(f"update user_details set City='{v1}' where UserID={val_s1}")
                    lab_name.set('')
                    db.commit()
                    msg.showinfo(message="Data Updated Successfully")

        lab12.config(text="Enter City Name")
        lab_name = StringVar()
        lab_en = Entry(frame5, font=('Ariel', 14, 'bold'), width=25, bg='SkyBlue', textvariable=lab_name,
                       relief=GROOVE, highlightthickness=2, highlightcolor='green')
        lab_en.place(x=205, y=200)

        update_but = Button(frame5, text="Update", command=update)
        update_but.place(x=10, y=240)

    def close():
        value = msg.askokcancel(message="Do You Want To Exit ?")
        if value is True:
            try:
                db.close()
            except Exception as close1:
                print(close1)
            finally:
                print("Database is Closed")
            tran.destroy()

    def update_password():
        def update():
            v1 = lab_name.get()
            if v1 == "" or v1 == 0:
                msg.showerror(message="Create a password")
            elif len(str(v1)) < 5:
                msg.showerror(message="Crate a More Strong Password")
            else:
                value = msg.askyesno(title="Update Information",
                                     message="Are you sure Want To Update Your Password.?")
                if value is True:
                    cu.execute("use account")
                    cu.execute(f"update user_details set Password='{v1}' where UserID={val_s1}")
                    lab_name.set(0)
                    db.commit()
                    msg.showinfo(message=f"Always Remember Your Password\n{v1}")

        lab12.config(text="Enter Password ")
        lab_name = IntVar()
        lab_en = Entry(frame5, font=('Ariel', 14, 'bold'), width=25, bg='SkyBlue', textvariable=lab_name,
                       relief=GROOVE, highlightthickness=2, highlightcolor='green', show="*")
        lab_en.place(x=205, y=200)

        update_but = Button(frame5, text="Update", command=update)
        update_but.place(x=10, y=240)

    tran = Tk()
    tran.wm_maxsize(1080, 565)
    tran.wm_minsize(1080, 565)
    tran.title("Transaction Page")

    can = Canvas(tran, width=1080, height=565, bg="#afd3ff")
    can.pack()

    frame1 = Frame(tran, height=60, width=1080, bd=4, relief=GROOVE, bg="#29bd22")
    frame1.place(x=0, y=0)

    frame2 = Frame(tran, height=380, width=500, bd=2, relief=GROOVE, bg="lightBlue")
    frame2.place(x=1, y=60)

    frame4 = Frame(tran, height=125, width=500, bd=2, relief=GROOVE, bg="grey")
    frame4.place(x=1, y=440)

    frame3 = Frame(tran, height=505, width=580, bd=2, relief=GROOVE)
    frame3.place(x=500, y=60)

    frame5 = Frame(tran, height=272, width=576, relief=GROOVE, bg="lightblue")
    frame5.place(x=501, y=290)

    label = Label(frame1, text="Welcome To Titan Bank", bg="grey", padx=340, bd=2, font=('Ariel', 26, 'bold'),
                  relief=GROOVE, pady=2)
    label.place(x=0, y=2)

    des = StringVar()
    description1 = Label(frame2, text="Enter UPI / PHONE_NO / ACCOUNT_NO", font=('Ariel', 14, 'bold'), bg='gainsBoro')
    description1.place(x=40, y=30)
    description2 = Entry(frame2, font=('Ariel', 16, 'bold'), width=30, bg='SkyBlue', textvariable=des,
                         relief=GROOVE, highlightthickness=2, highlightcolor='green')
    description2.place(x=40, y=70)

    t_amt = IntVar()
    t_amt1 = Label(frame2, text="Enter Transaction Amount", font=('Ariel', 14, 'bold'), bg='gainsBoro', padx=57)
    t_amt1.place(x=40, y=120)
    t_amt2 = Entry(frame2, font=('Ariel', 16, 'bold'), width=30, bg='SkyBlue', textvariable=t_amt,
                   relief=GROOVE, highlightthickness=2, highlightcolor='green')
    t_amt2.place(x=40, y=160)

    mode = Label(frame2, text="Enter The Mode Of Transaction", font=('Ariel', 16, 'bold'), bg='gainsBoro', padx=25)
    mode.place(x=40, y=220)

    withdraw = Button(frame2, text="Withdraw", padx=20, command=withdraw)
    withdraw.place(x=40, y=260)

    deposit = Button(frame2, text="Deposit", padx=30, command=deposit)
    deposit.place(x=165, y=260)

    transfer = Button(frame2, text="Transfer", padx=30, command=transfer)
    transfer.place(x=300, y=260)

    ex = Button(frame2, text="Close", bd=2, relief=GROOVE, activebackground="red", command=close,
                padx=10, font=("ariel", 10))
    ex.place(x=430, y=2)

    password_val = StringVar()
    password_lb = Label(frame2, text="Enter Your UPI Password", font=('Ariel', 14, 'bold'), bg='gainsBoro', padx=125)
    password_lb.place(x=3, y=310)
    password_en = Entry(frame2, font=('Ariel', 15, 'bold'), width=44, bg='SkyBlue', textvariable=password_val,
                        relief=GROOVE, highlightthickness=2, highlightcolor='green', )
    password_en.place(x=3, y=343)

    b1 = Button(frame4, padx=73, text='1', command=lambda: number(1), font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    b1.place(x=1, y=1)

    b2 = Button(frame4, padx=73, text='2', command=lambda: number(2), font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    b2.place(x=166, y=1)

    b3 = Button(frame4, padx=73, text='3', command=lambda: number(3), font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    b3.place(x=331, y=1)

    b4 = Button(frame4, padx=73, text='4', command=lambda: number(4), font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    b4.place(x=1, y=31)

    b5 = Button(frame4, padx=73, text='5', command=lambda: number(5), font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    b5.place(x=165, y=31)

    b6 = Button(frame4, padx=73, text='6', command=lambda: number(6), font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    b6.place(x=330, y=31)

    b7 = Button(frame4, padx=73, text='7', command=lambda: number(7), font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    b7.place(x=1, y=61)

    b8 = Button(frame4, padx=73, text='8', command=lambda: number(8), font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    b8.place(x=165, y=61)

    b9 = Button(frame4, padx=73, text='9', command=lambda: number(9), font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    b9.place(x=330, y=61)

    b0 = Button(frame4, padx=73, text='0', command=lambda: number(0), font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    b0.place(x=330, y=91)

    bc = Button(frame4, padx=142, text='Clear', command=clear, font=('Ariel', 10, 'bold'), bd=2, relief=GROOVE)
    bc.place(x=1, y=91)

    label = Label(frame5, text="Your Account Details", bg="GainsBoro", bd=3, relief=GROOVE,
                  font=('Ariel', 17, 'bold'), padx=167)
    label.place(x=0, y=0)

    button_1 = Button(frame5, text="Check Balance", bd=3, relief=GROOVE, command=check_bal, activeforeground="red")
    button_1.place(x=470, y=45)

    label_1 = Label(frame5, text="", font=('Ariel', 12, 'bold'), bg="lightblue")
    label_1.place(x=470, y=75)

    label_2 = Label(frame5, text="Username: ", font=('Ariel', 12, 'bold'), bg="lightblue")
    label_2.place(x=10, y=45)

    label_2 = Label(frame5, text=str(name), font=('Ariel', 12, 'bold'), bg="lightblue")
    label_2.place(x=96, y=45)

    label_3 = Label(frame5, text="Name: ", font=('Ariel', 12, 'bold'), bg="lightblue")
    label_3.place(x=10, y=75)

    list1 = []
    cu.execute('use account')
    cu.execute(f"select F_Name from user_details where UserID={val_s1}")
    for lis in cu:
        list1.append(lis[0])
    new_name1 = list1[0]
    label_3 = Label(frame5, text=str(new_name1), font=('Ariel', 12, 'bold'), bg="lightblue")
    label_3.place(x=66, y=75)
    list1.clear()

    label_5 = Label(frame5, text="Mobile_No :", font=('Ariel', 12, 'bold'), bg="lightblue")
    label_5.place(x=215, y=45)
    list1 = []
    cu.execute('use account')
    cu.execute(f"select Phone from user_details where UserID={val_s1}")
    for lis in cu:
        list1.append(lis[0])
    new_name1 = list1[0]
    label_6 = Label(frame5, text=new_name1, font=('Ariel', 12, 'bold'), bg="lightblue")
    label_6.place(x=315, y=45)

    label_7 = Label(frame5, text="G_Mail :", font=('Ariel', 12, 'bold'), bg="lightblue")
    label_7.place(x=215, y=75)
    list1 = []
    cu.execute('use account')
    cu.execute(f"select G_mail from user_details where UserID={val_s1}")
    for lis in cu:
        list1.append(lis[0])
    new_name1 = list1[0]
    label_8 = Label(frame5, text=new_name1, font=('Ariel', 12, 'bold'), bg="lightblue")
    label_8.place(x=282, y=75)

    label_4 = Label(frame5, text="Update Details", bg="GainsBoro", bd=3, relief=GROOVE,
                    font=('Ariel', 16, 'bold'), padx=213)
    label_4.place(x=0, y=115)

    lab12 = Label(frame5, text="", font=('Ariel', 14, 'bold'), bg="lightblue")
    lab12.place(x=10, y=200)

    but_1 = Button(frame5, text="Update Name", bd=3, relief=GROOVE, command=update_name, activeforeground="red")
    but_1.place(x=10, y=155)

    but_1 = Button(frame5, text="Update Number", bd=3, relief=GROOVE, command=update_number, activeforeground="red")
    but_1.place(x=125, y=155)

    but_1 = Button(frame5, text="Update G_mail", bd=3, relief=GROOVE, command=update_e_mail, activeforeground="red")
    but_1.place(x=245, y=155)

    but_1 = Button(frame5, text="Update City", bd=3, relief=GROOVE, command=update_city, activeforeground="red")
    but_1.place(x=360, y=155)

    but_1 = Button(frame5, text="Update Password", bd=3, relief=GROOVE, activeforeground="red", command=update_password)
    but_1.place(x=460, y=155)

    trans = ttk.Treeview(frame3, columns=('Date_Time', 'Description', 'Debit', 'Credit', 'Balance'),
                         show="headings")
    trans.heading(column="Date_Time", text="Date_time")
    trans.column("Date_Time", width=120)
    trans.heading(column="Description", text="Description")
    trans.column("Description", width=140)
    trans.heading(column="Debit", text="Debit")
    trans.column("Debit", width=90)
    trans.heading(column="Credit", text="Credit")
    trans.column("Credit", width=90)
    trans.heading(column="Balance", text="Balance")
    trans.column("Balance", width=120)

    scroll = ttk.Scrollbar(frame3)
    scroll.pack(side=RIGHT, fill=Y)
    trans.pack(side=LEFT, fill=BOTH)
    scroll.config(command=trans.yview)
    trans.configure(yscrollcommand=scroll.set)

    cu.execute("use transaction")
    cu.execute(f'select * from {name}')
    inst1 = []
    inst2 = []
    inst3 = []
    inst4 = []
    inst5 = []
    for inst in cu:
        inst1.append(inst[1])
        inst2.append(inst[2])
        inst3.append(inst[3])
        inst4.append(inst[4])
        inst5.append(inst[5])
        trans.insert('', END, values=(f'{inst[1]}', f'{inst[2]}', f'{inst[3]}', f'{inst[4]}', f'{inst[5]}'))

    tran.mainloop()


def getval():
    user = []
    global cu

    cu.execute('use bank')
    cu.execute('select Username from signup')
    for i2 in cu:
        user.append(i2[0])

    def otp():
        str1 = ''
        for i1 in range(4):
            str1 += str(randint(0, 9))
        li.append(str1)
        li[0] = str1
        msg.showinfo(title="OPT", message=f"Your 4-Digit OPT\n{str1}")

    u1 = s.get()
    u2 = s1.get()
    u3 = s2.get()
    if u1 == '':
        ur2.config(text="")
        ur1.config(text="username column cannot be Empty !!", fg="red", bg="#4f9491")
    elif u1 in user:
        ur2.config(text="")
        ur1.config(text="Username already Exits, Try another name !!", fg="red", bg="#4f9491")
    elif u2 == '':
        ur1.config(text='')
        ur2.config(text="Password field cannot be empty!!", fg='red', bg="#4f9491")
    elif u3 == '':
        ur1.config(text='')
        ur2.config(text='')
        otp = Button(top, text="Send OTP", command=otp,  activebackground="aqua", bg="Black", padx=10,
                     fg="White", font=("Arial", 13))
        otp.place(x=285, y=400)
    elif u3 != li[0]:
        msg.showerror(title="otp", message='Incorrect OTP!!')
    else:
        user.append(u1)
        ur3.config(text='')
        ur1.config(text='')
        ur2.config(text='')
        usr = msg.askyesno(title="Save", message="Do You Want To Save Information")
        if usr is True:
            try:
                top.destroy()

                def submit():
                    v = n.get()
                    v1 = n1.get()
                    v2 = n2.get()
                    v3 = age.get()
                    v4 = x.get()
                    v5 = x1.get()
                    v6 = phn.get()
                    v7 = gml.get()
                    v8 = dis.get()
                    v9 = adh.get()
                    v10 = pan.get()
                    v11 = bal.get()
                    v12 = password.get()
                    g = []
                    for i1 in v7:
                        g.append(i1)

                    if v == '':
                        msg.showerror(title='Error', message='First-Name field is Empty!!')
                    elif v1 == '':
                        msg.showerror(title='Error', message='Middle-Name field is Empty!!')
                    elif v2 == '':
                        msg.showerror(title='Error', message='Last-Name field is Empty!!')
                    elif v3 == 0 or v3 < 18:
                        val = msg.showerror(title='Error', message='You Are Not Eligible For Opening an account\n'
                                                                   'Age Requirement is Above 18\n'
                                                                   'Sorry For Inconvenience')
                        if val is True:
                            age.set(0)
                    elif v4 == '':
                        msg.showerror(title='Error', message='Please Select Your Gender')
                    elif v5 == '':
                        msg.showerror(title='Error', message='Select Account Type!!')
                    elif len(str(v6)) != 10:
                        msg.showerror(title='Error', message='Invalid Phone Number\nMust Contain 10 Digits')
                    elif v7 == "":
                        msg.showerror(title="Error", message="Please Enter G-mail Address")
                    elif "@" and 'g' and 'm' and 'a' and 'i' and 'l' and '.' not in g:
                        msg.showerror(title='Error', message='Invalid G-Mail Address')
                    elif v8 == '':
                        msg.showerror(title='Error', message='Please Enter Your City Name')
                    elif len(str(v9)) != 12:
                        msg.showerror(title='Error', message='Aadhar-Number Must Contain 12 Digits')
                    elif len(str(v10)) != 10:
                        msg.showerror(title='Error', message='Invalid PAN-Code\nMust Contain 10 Characters')
                    elif v11 == 0:
                        msg.showerror(title='Error', message='Please Enter Initial Amount')
                    elif v12 == '':
                        msg.showerror(title="Error", message='Password field is Empty!!')
                    elif len(str(v12)) < 5:
                        msg.showerror(title="Error", message='Password is Too Weak!!')
                    else:
                        data = msg.askyesno(title="Save Details", message="Do You Want To Save Info!!")
                        if data is True:
                            try:
                                cu.execute('use bank')
                                cu.execute(f"insert into signup(Username,Password) value(%s,%s)", (u1, u2))
                                db.commit()
                                cu.execute('use account')
                                cu.execute(f'insert into user_details(F_Name,M_Name,L_Name,Age,Gender,Account_Type,'
                                           f'Phone,'
                                           f'G_Mail,City,Aadhar_No,PAN_No,Balance,Password)values(%s,%s,%s,%s,%s,%s,'
                                           f'%s,%s,%s,%s,%s,%s,%s)', (v, v1, v2, v3, v4, v5, v6, v7, v8, v9,
                                                                      v10, v11, v12))
                                db.commit()
                                cu.execute('use transaction')
                                cu.execute(f'create table {u1}(Transaction_No int primary key AUTO_INCREMENT,'
                                           f'Date_Time datetime,Description varchar(50) Default "",'
                                           f'Debit bigint Default 0,'
                                           f'Credit bigint Default 0, Balance bigint)')
                                db.commit()
                                root.destroy()
                                transaction(u1)
                            except Exception as error1:
                                print(error1)

                def reset():
                    n.set('')
                    n1.set('')
                    n2.set('')
                    age.set(0)
                    x.set('')
                    x1.set('')
                    phn.set(0)
                    gml.set('')
                    dis.set('')
                    adh.set(0)
                    pan.set('')
                    bal.set(0)
                    password.set(0)
                root = Tk()
                root.wm_maxsize(700, 630)
                root.wm_minsize(700, 630)
                root.title("Bank Registration From")

                new = Canvas(root, height=630, width=700, bg="gainsBoro")
                new.pack()

                legend = Label(root, text="Bank Registration Form", font=('arial', 20),
                               bg="skyBlue", padx=210, pady=8, relief=GROOVE, bd=3)
                legend.place(x=0, y=0)
                i2 = 'darkSlateGray'
                h = 'gainsBoro'
                e1 = "blancheDalMOnd"

                n = StringVar()
                name = Label(root, text="Enter Your First-Name ", fg=i2, font=('arial', 14), bg=h)
                name.place(x=80, y=70)
                e2 = Entry(root, textvariable=n, width=25, font=('arial', 14), highlightcolor="green",
                           highlightthickness=1, bg=e1)
                e2.place(x=40, y=105)

                n1 = StringVar()
                add = Label(root, text="Enter Your Middle-Name ", fg=i2, font=('arial', 14), bg=h)
                add.place(x=410, y=70)
                e3 = Entry(root, textvariable=n1, width=25, font=('arial', 14), highlightcolor="green",
                           highlightthickness=1, bg=e1)
                e3.place(x=380, y=105)

                n2 = StringVar()
                age = Label(root, text="Enter Your Last-Name", fg=i2, font=('arial', 14), bg=h)
                age.place(x=80, y=150)
                e4 = Entry(root, textvariable=n2, width=25, font=('arial', 14), highlightcolor="green",
                           highlightthickness=1, bg=e1)
                e4.place(x=40, y=185)

                age = IntVar()
                lab2 = Label(root, text="Enter Your Age ", fg=i2, font=('arial', 14), padx=20, bg=h)
                lab2.place(x=435, y=150)
                e5 = Entry(root, textvariable=age, width=25, font=('arial', 14), highlightcolor="green",
                           highlightthickness=1, bg=e1)
                e5.place(x=380, y=185)

                x = StringVar()
                lab = Label(root, text="Enter Your Gender ", fg=i2, font=('arial', 14), padx=20, bg=h)
                lab.place(x=80, y=230)
                r1 = Radiobutton(root, text="Male", value="Male", variable=x, font=('arial', 14), bg=h)
                r1.place(x=40, y=265)
                r2 = Radiobutton(root, text="Female", value="Female", variable=x, font=('arial', 14), bg=h)
                r2.place(x=125, y=265)
                r2 = Radiobutton(root, text="Others", value="Others", variable=x, font=('arial', 14), bg=h)
                r2.place(x=235, y=265)

                x1 = StringVar()
                lab = Label(root, text="Enter Your Account-Type ", fg=i2, font=('arial', 14), bg=h)
                lab.place(x=410, y=230)
                c1 = Radiobutton(root, text="Savings", value="Savings", variable=x1, font=('arial', 14), bg=h)
                c1.place(x=400, y=265)
                c2 = Radiobutton(root, text="Current", value="Current", variable=x1, font=('arial', 14), bg=h)
                c2.place(x=550, y=265)

                phn = IntVar()
                lab2 = Label(root, text="Enter Your Mobile-Number  ", fg=i2, font=('arial', 14), bg=h)
                lab2.place(x=60, y=320)
                e5 = Entry(root, textvariable=phn, width=25, font=('arial', 14), highlightcolor="green",
                           highlightthickness=1, bg=e1)
                e5.place(x=40, y=355)

                gml = StringVar()
                lab3 = Label(root, text="Enter Your G-Mail ", fg=i2, font=('arial', 14), padx=20, bg=h)
                lab3.place(x=410, y=320)
                e6 = Entry(root, textvariable=gml, width=25, font=('arial', 14), highlightcolor="green",
                           highlightthickness=1, bg=e1)
                e6.place(x=380, y=355)

                dis = StringVar()
                lab3 = Label(root, text="Enter Your City-name ", fg=i2, font=('arial', 14), bg=h)
                lab3.place(x=80, y=400)
                e6 = Entry(root, textvariable=dis, width=25, font=('arial', 14), highlightcolor="green",
                           highlightthickness=1, bg=e1)
                e6.place(x=40, y=435)

                adh = IntVar()
                lab4 = Label(root, text="Enter Your Aadhar-number ", fg=i2, font=('arial', 14), bg=h)
                lab4.place(x=400, y=400)
                e8 = Entry(root, textvariable=adh, width=25, font=('arial', 14), highlightcolor="green",
                           highlightthickness=1, bg=e1)
                e8.place(x=380, y=435)

                pan = StringVar()
                lab4 = Label(root, text="Enter Your Pan-number ", fg=i2, font=('arial', 14), bg=h)
                lab4.place(x=80, y=480)
                e9 = Entry(root, textvariable=pan, width=25, font=('arial', 14), highlightcolor="green",
                           highlightthickness=1, bg=e1)
                e9.place(x=40, y=515)

                bal = IntVar()
                lab5 = Label(root, text="Enter Your Initial-Balance ", fg=i2, font=('arial', 14), bg=h)
                lab5.place(x=410, y=480)
                e10 = Entry(root, textvariable=bal, width=25, font=('arial', 14), highlightcolor="green",
                            highlightthickness=1, bg=e1)
                e10.place(x=380, y=515)

                password = IntVar()
                password1 = Label(root, text="Create A Password ", fg=i2, font=('arial', 14), bg=h)
                password1.place(x=80, y=555)
                e11 = Entry(root, textvariable=password, width=25, font=('arial', 14), highlightcolor="green",
                            highlightthickness=1, bg=e1, show="*")
                e11.place(x=40, y=590)

                but = Button(root, text="Save", font=('arial', 12), activebackground="green", padx=20, fg='green',
                             bg='lightblue', command=submit)
                but.place(x=550, y=585)

                but1 = Button(root, text="Reset", font=('arial', 12), activebackground="red", padx=20, fg='Red',
                              bg='lightblue', command=reset)
                but1.place(x=400, y=585)

                root.mainloop()
            except Exception as e1:
                db.rollback()
                print(e1)
        elif usr is False:
            top.destroy()


try:
    top = Tk()
    top.title('My Bank')
    top.wm_minsize(700, 500)
    top.wm_maxsize(700, 500)

    c = Canvas(top, height=500, width=700, bg="#4f9491")
    c.grid()

    Bn = Label(top, text="Login To Continue", font=("Arial", 20, 'bold'),
               padx=221, pady=10, fg="Black", bg="gainsBoro", relief=GROOVE, bd=5)
    Bn.place(x=1, y=0)

    u = Label(top, text="Please Enter Your Username ", font=("Arial", 15), padx=20)
    u.place(x=200, y=105)
    s = StringVar()
    ur = Entry(top, textvariable=s, font=("Arial", 16), highlightcolor="cyan",
               highlightthickness=2, width=25, bg="gainsBoro", relief=GROOVE, bd=1)
    ur.place(x=200, y=140)
    ur1 = Label(top, text="", bg="#4f9491")
    ur1.place(x=200, y=172)

    p = Label(top, text=" Enter A Login Password ", font=("Arial", 15), padx=40)
    p.place(x=200, y=220)
    s1 = StringVar()
    ur = Entry(top, textvariable=s1, font=("Arial", 16), show="*", highlightcolor="cyan",
               highlightthickness=2, width=25, bg="gainsBoro", relief=GROOVE, bd=1)
    ur.place(x=200, y=255)
    ur2 = Label(top, text="", bg="#4f9491")
    ur2.place(x=200, y=288)

    ot = Label(top, text="Please Enter 4-digit OTP", font=("Arial", 15), padx=40)
    ot.place(x=200, y=330)
    s2 = StringVar()
    ot1 = Entry(top, textvariable=s2, font=("Arial", 16), show="*", highlightcolor="cyan",
                highlightthickness=2, width=25, bg="gainsBoro", relief=GROOVE, bd=1)
    ot1.place(x=200, y=365)

    ur3 = Label(top, text="", bg="#4f9491")
    ur3.place(x=200, y=397)

    bt2 = Button(top, text="Sign Up", command=getval, activebackground="aqua", bg="Black", padx=5,
                 fg="White", font=("Arial", 13))
    bt2.place(x=200, y=440)

    bt = Button(top, text="Login", activebackground="aqua", command=login,  bg="Black", padx=10,
                fg="White", font=("Arial", 13))
    bt.place(x=295, y=440)

    bt2 = Button(top, text="Visit Website", command=web, activebackground="aqua", bg="Black", padx=5,
                 fg="White", font=("Arial", 13))
    bt2.place(x=385, y=440)

    top.mainloop()
except Exception as e:
    print(e)
