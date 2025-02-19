from tkinter import *
import time
from tkinter import messagebox as ms
import pygame.mixer as mix


def set_alarm():
    while True:
        time.sleep(1)
        now_time = time.strftime("%H:%M:%S", time.localtime())

        if h.get() == "" or m.get() == "" or s.get() == "":
            ms.showerror(title="Alarm", message="Time Cannot be null")
            break
        elif h.get() > "23" or m.get() > "59" or s.get() > "59":
            ms.showerror(title="Alarm", message="Invalid Time Format")
            break
        else:
            if m.get() < "10" or s.get() < "10":
                m1 = m.get()
                s1 = s.get()
            else:
                m1 = m.get()
                s1 = s.get()
            mix.init()
            alarm_time = f"{h.get()}:{m1}:{s1}"
            s_ = Label(lab_frame, text=f'Alarm has been Set: {time.strftime("%H:%M:%S", time.localtime())}',
                       font=("ariel", 16, 'bold'), pady=6, padx=49, bd=1, relief=SOLID)
            s_.place(x=0, y=235)
            print(now_time)
            print(alarm_time)

            if now_time == alarm_time:
                head.config(text="Wake up! Wake Up! Wake Up!", bg="red", fg="green")
                v = mix.Sound("sound.wav")
                v.play()
                v.set_volume(0.5)
                s_.destroy()
                break


def reset():
    print(time.strftime("%H:%M:%S", time.localtime()))
    h.set("")
    m.set("")
    s.set("")
    head.config(text="Enter Your Time to wake up!!")


root = Tk()
root.geometry("402x302")
root.resizable(False, False)
root.title("My Alarm Clock")
# frame
lab_frame = LabelFrame(root, text="Alarm Clock", bg="#807473", height=300, width=400, font=("san-serif", 16, "bold"),
                       fg="#00f8fc", bd=2, relief=SOLID)
lab_frame.place(x=0, y=0)

head = Label(lab_frame, text="Enter Your Time to wake up!!", font=("san-serif", 15, "bold"), padx=45, pady=4,
             bg="#65dee0", fg="#3e4242")
head.place(x=10, y=10)

h = StringVar(root)
hour = Label(lab_frame, text="Hours ", font=("san-serif", 15, "bold"), padx=19, bg="#8deba9")
hour.place(x=60, y=60)
h_E = Entry(lab_frame, textvariable=h, font=("san-serif", 16, "bold"), width=10, bg="#c1c9c4", fg="#e6393f")
h_E.place(x=210, y=60)

m = StringVar()
min_ = Label(lab_frame, text="Minutes ", font=("san-serif", 15, "bold"), padx=9, bg="#8deba9")
min_.place(x=60, y=100)
h_E = Entry(lab_frame, textvariable=m, font=("san-serif", 16, "bold"), width=10, bg="#c1c9c4", fg="#e6393f")
h_E.place(x=210, y=100)

s = StringVar()
sec = Label(lab_frame, text="Seconds ", font=("san-serif", 15, "bold"), padx=7, bg="#8deba9")
sec.place(x=60, y=140)
h_E = Entry(lab_frame, textvariable=s, font=("san-serif", 16, "bold"), width=10, bg="#c1c9c4", fg="#e6393f")
h_E.place(x=210, y=140)

setBut = Button(lab_frame, text="Set Alarm", command=set_alarm, font=("san-serif", 13, "bold"), padx=9,
                bg="green", fg="#e3756d")
setBut.place(x=60, y=190)

retBut = Button(lab_frame, text="Reset Alarm", command=reset, font=("san-serif", 13, "bold"), padx=8,
                fg="green", bg="#e3756d")
retBut.place(x=210, y=190)

root.mainloop()
