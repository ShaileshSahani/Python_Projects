import random
from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from PIL import ImageTk
from tkcalendar import Calendar
import time
import string
import textwrap

expression = ""

try:
    db = mysql.connector.connect(host="localhost", password="root", user="root")
    cu = db.cursor()
    cu.execute("CREATE DATABASE IF NOT EXISTS wifi_database")
    cu.execute("use wifi_database")
    cu.execute("CREATE table if not exists admin(username varchar(30) not null,"
               " password varchar(30) not null)")
    cu.execute("Create table if not exists bills(REP_ID varchar(6) primary key,"
               " NAME varchar(30) not null,"
               "CONTACT varchar(15) not null, ADDRESS varchar(100) not null,"
               " PLAN varchar(15) not null,"
               "VALIDITY varchar(10) not null, PAYMENT varchar(20) not null,"
               " SERVICE varchar(10),"
               " BILLINGDateTime varchar(30) not null, TOTAL_BILL int not null )")


    def select():
        cu.execute("select * from admin")
        return cu.fetchall()


    tab = select()
    if len(tab) == 0:
        cu.execute("insert into admin values('admin', 'admin')")
        db.commit()
        tab = select()


    def history():
        def clear_view():
            for item in view.get_children():
                view.delete(item)

        def pre():
            his_frame.destroy()

        def load_data():
            clear_view()
            cu.execute("select * from bills")
            for i in cu:
                view.insert("", END,
                            values=(i[0], i[1], i[2], textwrap.fill(i[3], 15), i[4],
                                    i[5], i[6], i[7], i[8], i[9]))

        def on_search():
            search_query = get_search.get().lower()
            view.selection_remove(view.get_children())
            for item in view.get_children():
                values = view.item(item, 'values')
                if any(search_query in str(value).lower() for value in values):
                    view.selection_add(item)

        his_frame = Frame(root, height=432, width=899.5, bd=1, relief=SOLID)
        his_frame.place(x=0.3, y=69)
        buttons = Frame(his_frame, height=59, width=899, bd=1, relief=SOLID, bg="#a5a8a0")
        buttons.place(x=0, y=0)
        get_search = StringVar()
        en1 = Entry(buttons, textvariable=get_search, width=19, font="serif 21 bold", fg="#585959", bg="#aaadad")
        en1.place(x=10, y=12)

        but1 = ttk.Button(buttons, text="search", command=on_search)
        but1.place(x=330, y=10)
        but2 = ttk.Button(buttons, text="Load All Data", command=load_data)
        but2.place(x=570, y=10)
        but3 = ttk.Button(buttons, text="Previous", command=pre)
        but3.place(x=730, y=10)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font="Serif 16 bold", foreground="#1fb01a")
        view = ttk.Treeview(his_frame, columns=('REP_ID', 'NAME', 'CONTACT', 'ADDRESS', 'PLAN', 'VALIDITY',
                                                'PAYMENT', 'SERVICE', 'BILLINGDateTime',
                                                'TOTAL_BILL'), show="headings", height=17)
        style.configure("Treeview", background="#8a8a8a", foreground="white")
        view.place(x=0, y=60)
        view.heading(text="REP_ID", column="REP_ID")
        view.column("REP_ID", anchor=CENTER, width=70)
        view.heading(text="NAME", column="NAME")
        view.column("NAME", anchor=CENTER, width=100)
        view.heading(text="CONTACT", column="CONTACT")
        view.column("CONTACT", anchor=CENTER, width=100)
        view.heading(text="ADDRESS", column="ADDRESS")
        view.column("ADDRESS", anchor=CENTER, width=120)
        view.heading(text="PLAN", column="PLAN")
        view.column("PLAN", anchor=CENTER, width=80)
        view.heading(text="VALIDITY", column="VALIDITY")
        view.column("VALIDITY", anchor=CENTER, width=100)
        view.heading(text="PAYMENT", column="PAYMENT")
        view.column("PAYMENT", anchor=CENTER, width=80)
        view.heading(text="SERVICE", column="SERVICE")
        view.column("SERVICE", anchor=CENTER, width=64)
        view.heading(text="BILLINGDateTime", column="BILLINGDateTime")
        view.column("BILLINGDateTime", anchor=CENTER, width=105)
        view.heading(text="TOTAL_BILL", column="TOTAL_BILL")
        view.column("TOTAL_BILL", anchor=CENTER, width=75)
        load_data()


    def main_window():  # Main Function
        main_frame = Frame(root, height=432, width=899.5, bd=1, relief=SOLID)
        main_frame.place(x=0.3, y=69)

        # Form
        gen_bill = Frame(main_frame, height=430, width=450, bd=1, relief=SOLID, bg="#9ef4f7")
        gen_bill.place(x=0, y=0)

        def generate():
            str_ = ""
            str_lis = list(string.ascii_uppercase)
            number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            for i in range(6):
                if i < 2:
                    str_ += random.choice(str_lis)
                else:
                    str_ += random.choice(number)
            cu.execute("Select REP_ID from bills")
            lis = []
            for i in cu:
                lis.append(i[0])
            if str_ in lis:
                generate()
            else:
                return str_

        def reset():
            main_frame.destroy()
            main_window()

        def save_to_database():
            ref = generate()
            v1 = c_name.get()
            v2 = c_con.get()
            v3 = c_add.get()
            v4 = cplan_var.get()
            v5 = cval_var.get()
            v6 = c_pay_var.get()
            v7 = c_typ_var.get()
            v8 = c_date.get()
            v9 = c_tot.get()

            if v1 == "" or v1 == " " or v2 == "" or v2 == " " or v3 == "" or v3 == " ":
                messagebox.showwarning("Empty", "Fields Cannot be Empty")
            elif len(v2) != 10:
                messagebox.showerror("Number", "Invalid Number")
            elif v7 == "" or v7 == " ":
                messagebox.showwarning("Option", "Select At least one option")
            elif v8 == "" or v8 == " ":
                messagebox.showwarning("Date", "Select Date!!")
            elif v9 == 0:
                messagebox.showwarning("Total", "Click on calculate to get Total Amount")
            else:
                now = time.strftime("%H:%M:%S", time.localtime())
                try:
                    cu.execute("insert into bills values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (ref, v1, v2, v3, v4, v5, v6, v7, v8 + " " + now, v9))
                    info = messagebox.askyesno("Data Entry", "Do you Want to Save and Print ?")
                    if info is True:
                        s2_res.config(text=ref, font="cambria 10")
                        s3_res.config(text=v8, font="cambria 10")
                        s7_res.config(text=v1, font="cambria 12")
                        s8_res.config(text=v2, font="cambria 12")
                        s9_res.config(text=v3, font="cambria 12")
                        s10_res.config(text=v9, font="cambria 13 bold", pady=9)
                        s11_res.config(text=v4, font="cambria 11")
                        s12_res.config(text=v5, font="cambria 11")
                        s13_res.config(text=v6, font="cambria 11")
                        s14_res.config(text=v7, font="cambria 11")
                        db.commit()

                except Exception as rr:
                    db.rollback()
                    messagebox.showerror("sql", f"SQL Error {rr}")

        def get_date():
            def my_date():
                c_date.set(cal_.get_date())
                nw.destroy()

            nw = Tk()
            nw.wm_minsize(250, 210)
            nw.wm_maxsize(250, 210)
            cal_ = Calendar(nw)
            cal_.pack()
            but = Button(nw, text="Select Date", command=my_date)
            but.pack()
            nw.mainloop()

        def calculate_():
            plan_dict_fibre = {'10 mbps ': 100, '20 mbps ': 200, '30 mbps ': 300, '40 mbps ': 400, '50 mbps ': 500,
                               '60 mbps ': 600, '70 mbps ': 700, '80 mbps ': 800, '90 mbps ': 900, '100 mbps': 1000}
            plan_dict_optic = {'10 mbps ': 150, '20 mbps ': 250, '30 mbps ': 350, '40 mbps ': 500, '50 mbps ': 600,
                               '60 mbps ': 700, '70 mbps ': 800, '80 mbps ': 900, '90 mbps ': 1000, '100 mbps': 1100}

            v4 = cplan_var.get()
            v5 = cval_var.get()
            v7 = c_typ_var.get()
            if v7 == "":
                messagebox.showwarning("Option", "Select At least one option From Radiobutton")
            elif v7 == "Fibre":
                if v5 == "12 Months":
                    c_tot.set(plan_dict_fibre.get(v4) * 12)
                else:
                    c_tot.set(int(v5[0]) * plan_dict_fibre.get(v4))
            elif v7 == "Optic":
                if v5 == "12 Months":
                    c_tot.set(plan_dict_optic.get(v4) * 12)
                else:
                    c_tot.set(int(v5[0]) * plan_dict_optic.get(v4))

        l1 = Label(gen_bill, text="Customer name", font="Aller 15 bold", padx=14, bd=1, relief=GROOVE)
        l1.place(x=20, y=10)
        c_name = StringVar()
        e1 = Entry(main_frame, textvariable=c_name, font="Aller 15 bold", width=16)
        e1.place(x=20, y=45)

        l2 = Label(gen_bill, text="Customer contact", font="Aller 15 bold", padx=5, bd=1, relief=GROOVE)
        l2.place(x=250, y=10)
        c_con = StringVar()
        e2 = Entry(main_frame, textvariable=c_con, font="Aller 15 bold", width=16)
        e2.place(x=250, y=45)

        l3 = Label(gen_bill, text="Customer address", font="Aller 15 bold", bd=1, relief=GROOVE, padx=3)
        l3.place(x=20, y=85)
        c_add = StringVar()
        e3 = Entry(main_frame, textvariable=c_add, font="Aller 15 bold", width=16)
        e3.place(x=20, y=120)

        l4 = Label(gen_bill, text="Service Provider", font="Aller 15 bold italic", padx=10, relief=GROOVE, bd=1)
        l4.place(x=250, y=85)
        c_pro = StringVar()
        c_pro.set("Hk Internet Service")
        e1 = Entry(main_frame, state=DISABLED, textvariable=c_pro, font="Aller 15", width=16)
        e1.place(x=250, y=120)

        plan_list = ('10 mbps ', '20 mbps ', '30 mbps ', '40 mbps ', '50 mbps ', '60 mbps ', '70 mbps ',
                     '80 mbps ', '90 mbps ', '100 mbps')
        l5 = Label(main_frame, text="Select Plan", font="Aller 15 bold", padx=36, relief=GROOVE, bd=1)
        l5.place(x=20, y=160)
        cplan_var = StringVar()
        cplan_var.set("10 mbps ")
        plan = OptionMenu(main_frame, cplan_var, *plan_list)
        plan.place(x=20, y=195)
        plan.configure(font="Aller 13 bold", padx=37)

        l6 = Label(main_frame, text="Plan Validity", font="Aller 15 bold", padx=29, relief=GROOVE, bd=1)
        l6.place(x=250, y=160)
        v_list = ('1 Month  ', '3 Months  ', '6 Months  ', '12 Months')
        cval_var = StringVar()
        cval_var.set('1 Month  ')
        val = OptionMenu(main_frame, cval_var, *v_list)
        val.place(x=250, y=195)
        val.configure(font="Aller 13 bold", padx=33)

        l7 = Label(main_frame, text="Payment method", font="Aller 15 bold", padx=10, relief=GROOVE, bd=1)
        l7.place(x=20, y=245)
        p_list = ('Online ', 'Cash   ', 'Cheque')
        c_pay_var = StringVar()
        c_pay_var.set('Cash   ')
        pay = OptionMenu(main_frame, c_pay_var, *p_list)
        pay.place(x=20, y=280)
        pay.configure(font="Aller 13 bold", padx=44)

        l8 = Label(main_frame, text="Service Type", font="Aller 15 bold", padx=28, relief=GROOVE, bd=1)
        l8.place(x=250, y=245)
        c_typ_var = StringVar()
        b1 = Radiobutton(main_frame, text="Fibre", variable=c_typ_var, value="Fibre", bd=3, relief=GROOVE,
                         font="Aller 13 bold", padx=7)
        b1.place(x=250, y=282)
        b1 = Radiobutton(main_frame, text="Optic", variable=c_typ_var, value="Optic", bd=3, relief=GROOVE,
                         font="Aller 13 bold", padx=7)
        b1.place(x=345, y=282)

        date = Label(main_frame, text="Select Date", font="Aller 15 bold", padx=36, bd=1, relief=GROOVE)
        date.place(x=20, y=325)
        c_date = StringVar()
        c_date.set("")
        but_dt = Button(main_frame, text='Calender', font="ariel 9 bold", pady=2, bg="#ebe431", command=get_date)
        but_dt.place(x=20, y=360)
        selected = Entry(main_frame, textvariable=c_date, font="Aller 15", width=10, state=DISABLED)
        selected.place(x=89, y=360)

        l9 = Label(main_frame, text="Total Amount", font="Aller 15 bold italic", padx=24, bd=1, relief=GROOVE)
        l9.place(x=250, y=325)
        c_tot = IntVar()
        e1 = Entry(main_frame, state=DISABLED, textvariable=c_tot, font="Aller 15", width=16)
        e1.place(x=250, y=360)

        save = Button(main_frame, text="Save & Print", font="ariel 10 bold", padx=7, bg="#36abed", bd=2, relief=GROOVE,
                      command=save_to_database)
        save.place(x=20, y=397)
        history_ = Button(main_frame, text="History", font="ariel 10 bold", padx=10, bg="#0fdb86", bd=2,
                          relief=GROOVE, command=history)
        history_.place(x=129, y=397)
        total = Button(main_frame, text="Calculate", font="ariel 10 bold", padx=10, bg="#3ef0b2", bd=2, relief=GROOVE,
                       command=calculate_)
        total.place(x=250, y=397)
        print_bill = Button(main_frame, text="Reset ", font="ariel 10 bold", padx=15, bg="#bcfc68", bd=2, relief=GROOVE,
                            command=reset)
        print_bill.place(x=348, y=397)

        # bill printer
        bill = Frame(main_frame, height=215, width=448, bd=1, relief=GROOVE, bg="#ffffff")
        bill.place(x=450, y=0)
        sep = ttk.Separator(bill, orient=HORIZONTAL)
        sep.place(relx=0, rely=0.15, relwidth=1, relheight=0.01)
        sep = ttk.Separator(bill, orient=HORIZONTAL)
        sep.place(relx=0, rely=0.79, relwidth=1, relheight=0.01)
        img_logo = Label(bill, image=logo_)
        img_logo.place(x=2, y=34)

        header = Label(bill, text="Internet Invoice", font="cambria 16 bold", padx=145, bg="#ffffff")
        header.place(x=0, y=0)
        s1 = Label(bill, text="Receipt Details", font="cambria 14 bold", bg="#ffffff")
        s1.place(x=300, y=35)
        s2 = Label(bill, text="Receipt Number:", font="cambria 11 bold", bg="#ffffff")
        s2.place(x=270, y=65)
        s2_res = Label(bill, text="---", bg="#ffffff")
        s2_res.place(x=393, y=66)
        s3 = Label(bill, text="Date:", font="cambria 11 bold", bg="#ffffff")
        s3.place(x=335, y=90)
        s3_res = Label(bill, text="---", bg="#ffffff")
        s3_res.place(x=380, y=91)
        s4 = Label(bill, text="Internet Provider Details", font="cambria 13 bold", bg="#ffffff")
        s4.place(x=230, y=115)
        s5 = Label(bill, text="Hk Internet Services", font="cambria 11 bold", bg="#ffffff")
        s5.place(x=285, y=143)

        s6 = Label(bill, text="Billed to, ", font="cambria 14 bold", bg="#ffffff")
        s6.place(x=80, y=35)

        s7 = Label(bill, text="Name:", font="cambria 11 bold", bg="#ffffff")
        s7.place(x=80, y=65)
        s7_res = Label(bill, text="---", bg="#ffffff")
        s7_res.place(x=132, y=65)
        s8 = Label(bill, text="Contact: ", font="cambria 11 bold", bg="#ffffff")
        s8.place(x=80, y=92)
        s8_res = Label(bill, text="---", bg="#ffffff")
        s8_res.place(x=150, y=92)
        s9 = Label(bill, text="Address: ", font="cambria 11 bold", bg="#ffffff")
        s9.place(x=2, y=120)
        s9_res = Label(bill, text="---", bg="#ffffff")
        s9_res.place(x=75, y=121)

        s10 = Label(bill, text="Amount: ", font="cambria 13 bold", pady=9, bg="#ffffff")
        s10.place(x=292, y=170)
        s10_res = Label(bill, text="---", font="cambria 13 bold", pady=9, bg="#ffffff")
        s10_res.place(x=366, y=170)

        s11 = Label(bill, text="Plan", font="cambria 10 bold", padx=20, bg="#ffffff")
        s11.place(x=0, y=170)
        s11_res = Label(bill, text="---", font="cambria 10", padx=5, bg="#ffffff")
        s11_res.place(x=0, y=192)
        sep3 = ttk.Separator(bill, orient=VERTICAL)
        sep3.place(relx=0.16, rely=0.79, relwidth=0.001, relheight=0.21)

        s12 = Label(bill, text="Validity", font="cambria 10 bold", padx=15, bg="#ffffff")
        s12.place(x=74, y=170)
        s12_res = Label(bill, text="---", font="cambria 10", padx=9, bg="#ffffff")
        s12_res.place(x=74, y=192)
        sep3 = ttk.Separator(bill, orient=VERTICAL)
        sep3.place(relx=0.35, rely=0.79, relwidth=0.001, relheight=0.21)

        s13 = Label(bill, text="Payment", font="cambria 10 bold", padx=2, bg="#ffffff")
        s13.place(x=158, y=170)
        s13_res = Label(bill, text="---", font="cambria 10", padx=9, bg="#ffffff")
        s13_res.place(x=158, y=192)
        sep4 = ttk.Separator(bill, orient=VERTICAL)
        sep4.place(relx=0.49, rely=0.79, relwidth=0.001, relheight=0.21)

        s14 = Label(bill, text="Service", font="cambria 10 bold", padx=12, bg="#ffffff")
        s14.place(x=221, y=170)
        s14_res = Label(bill, text="---", font="cambria 10", padx=18, bg="#ffffff")
        s14_res.place(x=221, y=192)
        sep4 = ttk.Separator(bill, orient=VERTICAL)
        sep4.place(relx=0.65, rely=0.79, relwidth=0.001, relheight=0.21)

        # calculator Frame
        cal = Frame(main_frame, height=215, width=448, bd=1, relief=GROOVE, bg="grey")
        cal.place(x=450, y=215)

        def get_val(val_):
            global expression
            expression += val_
            exp.set(expression)

        def del_():
            global expression
            if expression == "":
                pass
            else:
                new = list(expression)
                new.pop()
                expression = "".join(new)
                exp.set(expression)

        def clr():
            global expression
            expression = ''
            exp.set(expression)
            output.set('Result')

        def solve():
            global expression
            if expression == "":
                output.set("error")
            else:
                try:
                    try:
                        output.set(str(eval(expression)))
                    except ZeroDivisionError:
                        output.set("Infinity")
                except SyntaxError:
                    output.set("Expression Error")

        exp = StringVar()
        equation = Entry(cal, font=('cambria', 19), bd=0, width=32, textvariable=exp, state=DISABLED,
                         disabledforeground="#545353", disabledbackground="#e0e0e0")
        equation.place(x=0, y=0)

        output = StringVar()
        output.set("Result")
        result = Entry(cal, font=('cambria', 19), bd=0, width=32, textvariable=output, state=DISABLED,
                       disabledforeground="#545353", disabledbackground="#e0e0e0")
        result.place(x=0, y=32)

        # buttons
        b1 = Button(cal, text="1", padx=32, command=lambda: get_val("1"), font=('cambria', 15))
        b1.place(x=0, y=65)
        b2 = Button(cal, text="2", padx=32, command=lambda: get_val("2"), font=('cambria', 15))
        b2.place(x=89, y=65)
        b3 = Button(cal, text="3", padx=32, command=lambda: get_val("3"), font=('cambria', 15))
        b3.place(x=178, y=65)
        b_plus = Button(cal, text="+", padx=32, command=lambda: get_val("+"), font=('cambria', 15), bg="#86dbd4")
        b_plus.place(x=267, y=65)
        b_minus = Button(cal, text="–", padx=32.5, command=lambda: get_val("-"), font=('cambria', 15), bg="#86dbd4")
        b_minus.place(x=356, y=65)

        b4 = Button(cal, text="4", padx=32, command=lambda: get_val("4"), font=('cambria', 15))
        b4.place(x=0, y=102)
        b5 = Button(cal, text="5", padx=32, command=lambda: get_val("5"), font=('cambria', 15))
        b5.place(x=89, y=102)
        b6 = Button(cal, text="6", padx=32, command=lambda: get_val("6"), font=('cambria', 15))
        b6.place(x=178, y=102)
        b_mul = Button(cal, text="×", padx=32, command=lambda: get_val("*"), font=('cambria', 15), bg="#86dbd4")
        b_mul.place(x=267, y=102)
        b_div = Button(cal, text="÷", padx=32, command=lambda: get_val("/"), font=('cambria', 15), bg="#86dbd4")
        b_div.place(x=356, y=102)

        b7 = Button(cal, text="7", padx=32, command=lambda: get_val("7"), font=('cambria', 15))
        b7.place(x=0, y=139)
        b8 = Button(cal, text="8", padx=32, command=lambda: get_val("8"), font=('cambria', 15))
        b8.place(x=89, y=139)
        b9 = Button(cal, text="9", padx=32, command=lambda: get_val("9"), font=('cambria', 15))
        b9.place(x=178, y=139)
        b_clear = Button(cal, text="C", padx=77, command=clr, font=('cambria', 15), bg="red")
        b_clear.place(x=267, y=139)

        b00 = Button(cal, text="⋅", padx=34, command=lambda: get_val("."), font=('cambria', 15))
        b00.place(x=0, y=176)
        b0 = Button(cal, text="0", padx=32, command=lambda: get_val("0"), font=('cambria', 15))
        b0.place(x=89, y=176)
        b_del = Button(cal, text="Del", padx=23, command=del_, font=('cambria', 15), bg="#e66d22")
        b_del.place(x=178, y=176)
        b_res = Button(cal, text="=", padx=77, command=solve, font=('cambria', 15), bg="#009c49")
        b_res.place(x=267, y=176)


    def login():
        usr = username.get()
        pas = password.get()
        if usr == "" or pas == "":
            messagebox.showerror(title="Error", message="Fields cannot be empty")
        elif usr != tab[0][0] or pas != tab[0][1]:
            messagebox.showerror(title="Error", message="Incorrect Username / Password !!!")
        else:
            main_window()


    def update_fun(type_):
        def update():
            global tab
            new_val = new_value.get()
            o_use = old_value1.get()
            o_pass = old_value2.get()
            if new_val == "" or new_val == " " or o_pass == "" or o_use == "" or o_pass == " " or o_use == " ":
                messagebox.showerror("Login", "Fields cannot be empty!!")
            elif type_ == "password" and len(new_val) < 5:
                messagebox.showerror("Length", "Password is too weak")
            elif o_use != tab[0][0]:
                messagebox.showerror("Incorrect", "Enter Correct Username!!")
            elif o_pass != tab[0][1]:
                messagebox.showerror("Incorrect", "Enter Correct Password!!")
            else:
                if type_ == "username":
                    try:
                        cu.execute(f"update admin set username='{new_val}' where password='{tab[0][1]}'")
                        db.commit()
                    except Exception as ser:
                        messagebox.showerror(message=str(ser))
                else:
                    try:
                        cu.execute(f"update admin set password='{new_val}' where username='{tab[0][0]}'")
                        db.commit()
                    except Exception as ser:
                        messagebox.showerror(message=str(ser))

                tab = select()
                val = messagebox.askyesno(message=f"{type_} Updated Successfully\nMove to Previous window")
                frame.destroy() if val is True else None

        frame = Frame(root, height=432, width=899.5, bd=1, relief=SOLID, bg="#80c4bf")
        frame.place(x=0.3, y=69)

        a = 21
        if type_ == "password":
            a = 23
        new_chane = Label(frame, text=f"Enter new_{type_}", font="Georgia 20 bold", padx=a)
        new_chane.place(x=270, y=20)
        new_value = StringVar()
        e1 = Entry(frame, textvariable=new_value, font="Georgia 20 bold", width=18)
        e1.place(x=270, y=70)

        old_user = Label(frame, text=f"Enter current username", font="Georgia 20 bold", padx=3)
        old_user.place(x=270, y=140)
        old_value1 = StringVar()
        e2 = Entry(frame, textvariable=old_value1, font="Georgia 20 bold", width=18)
        e2.place(x=270, y=190)

        old_pass = Label(frame, text="Enter current password", font="Georgia 20 bold", padx=5)
        old_pass.place(x=270, y=260)
        old_value2 = StringVar()
        e2 = Entry(frame, textvariable=old_value2, font="Georgia 20 bold", width=18)
        e2.place(x=270, y=310)

        ttk.Style().configure("TButton", font="Serif 17 bold", foreground="#1fb01a")
        but = ttk.Button(frame, text="Update", command=update)
        but.place(x=270, y=380)

        back = ttk.Button(frame, text="Previous", command=frame.destroy)
        back.place(x=465, y=380)
        back.config()


    root = Tk()
    root.wm_maxsize(900, 501)
    root.wm_minsize(900, 501)
    root.title("Login Page")

    c = Canvas(root, height=501, width=900, bg="#9c9494")
    c.pack()
    logo_ = ImageTk.PhotoImage(file="logo.jpg")
    img_file = ImageTk.PhotoImage(file="brand.jpg")
    setting_logo = ImageTk.PhotoImage(file="setting.png")
    head = Label(root, text="HK Broadband Services", font=('Palatino', 30, 'bold', 'underline'), bg="#7ec2d9",
                 fg="blue", padx=240, bd=3, relief=SOLID, pady=10)
    head.place(x=0, y=0)

    setting = Menubutton(root, image=setting_logo, bg="#7ec2d9", bd=0, activebackground="#7ec2d9")
    setting.menu = Menu(setting, background="#a1f0ed")
    setting['menu'] = setting.menu
    setting.menu.add_cascade(label="Update setting", font="Ariel 14 bold")
    setting.menu.add_separator()
    setting.menu.add_command(label='Username', command=lambda: update_fun("username"))
    setting.menu.add_command(label='Password', command=lambda: update_fun("password"))
    setting.menu.add_command(label="Exit", command=root.destroy)
    setting.place(x=3, y=5)

    img_lab = Label(root, image=img_file, height=320, width=400, bd=4.4, relief=SOLID)
    img_lab.place(x=450, y=120)

    user = Label(root, text="Username", font=('sarif', 20, 'italic', 'bold'), padx=40)
    user.place(x=120, y=120)
    username = StringVar()
    userEn = Entry(root, textvariable=username, font=('sarif', 20), width=14,
                   bg="#ededed", insertbackground="blue", fg="Blue")
    userEn.place(x=120, y=180)

    pass_ = Label(root, text="Password", font=('sarif', 20, 'italic', 'bold'), padx=42)
    pass_.place(x=120, y=280)
    password = StringVar()
    passEn = Entry(root, textvariable=password, show="*", font=('sarif', 20), width=14,
                   bg="#ededed", insertbackground="blue", fg="Blue")
    passEn.place(x=120, y=340)

    button = Button(root, text="Login", command=login, font=("sarif", 13, "bold"), padx=80)
    button.place(x=120, y=415)
    root.mainloop()
except Exception as E:
    messagebox.showerror(message=f"Error while connection!!\n{E}")
