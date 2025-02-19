from time import strftime, localtime
from tkinter import *
from datetime import date

root = Tk()
try:
    def get_current_time():
        local = localtime()
        time_string = strftime("%H : %M : %S  %p ", local)
        time_label.config(text=time_string)
        time_label.after(1000, get_current_time)
    root.title("Digital_Clock")
    root.wm_minsize(400, 180)
    root.wm_maxsize(400, 180)

    heading = Label(root, text="Digital Clock", bd=3, relief=GROOVE, font=("ariel", 20, "bold"),
                    padx=113, bg="#50ebe5", fg="#f01d35", pady=10)
    heading.place(x=0, y=0)

    time_label = Label(root, text="", bd=3, relief=GROOVE, font=("ariel", 20, "bold"),
                       padx=94, bg="black",  fg="red", pady=14)
    time_label.place(x=0, y=55)
    get_current_time()

    date_string = date.today()

    date_label = Label(root, text=str(date_string), bd=3, relief=GROOVE, font=("ariel", 20, "bold"),
                       padx=128, bg="black",  fg="red", pady=11)
    date_label.place(x=0, y=120)

    root.mainloop()
except Exception as Er:
    print(Er)
