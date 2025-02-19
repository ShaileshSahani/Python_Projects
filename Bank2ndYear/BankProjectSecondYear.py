from tkinter import *
import mysql.connector
import random
import datetime
import time
from tkinter import messagebox as msg
from PIL import ImageTk
root = Tk()
db = mysql.connector.connect(host="localhost", user="root", password="root")
cu = db.cursor()
try:
    def date_time():
        current_date_time = (f"{datetime.date.today()} "
                             f"{time.strftime('%H:%M:%S', time.localtime())}")
        return current_date_time


    # Connection and Database Creation
    cu.execute("CREATE DATABASE IF NOT EXISTS domain_bank")
    cu.execute('USE domain_bank')
    cu.execute('CREATE TABLE IF NOT EXISTS username_password'
               '(user_id int primary key AUTO_INCREMENT, username varchar(50)'
               ', password varchar(20))')
    # End Database

    # Tkinter View
    root.geometry("1000x720")
    root.title("Domain Bank")
    root.resizable(False, False)

    # Frames Define
    main_nav = Frame(root, height=60, width=1000, bd=1, relief=SOLID, bg="red")
    main_nav.place(x=0, y=0)

    img_frame = Frame(root, height=580, width=1000, bd=1, relief=SOLID, bg="#918f8e")
    img_frame.place(x=0, y=60)

    footer_frame = Frame(root, height=80, width=1000, bd=1, relief=SOLID, bg="blue")
    footer_frame.place(x=0, y=640)

    # Image
    bank_img = ImageTk.PhotoImage(file="BankImage.jpg")
    img_label = Label(img_frame, image=bank_img, height=580, width=1000)
    img_label.place(x=0, y=0)

    root.mainloop()

except Exception as err:
    msg.showerror(title="Uncaught Error", message=f"Error while execution\n"
                                                  f"{err}")
