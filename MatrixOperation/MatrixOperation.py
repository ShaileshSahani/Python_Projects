from tkinter import *


def calculate():
    def solve():
        string = value.get()
        string = list(map(int, string.split()))
        array = []
        iterative = 0
        for i in range(rows):
            sub_array = []
            for j in range(cols):
                sub_array.append(int(string[iterative]))
                iterative += 1
            array.append(sub_array)
        lab = Label(R, text=f"Array: {str(array)}")
        lab.update()
        lab.pack()
    rows = r.get()
    cols = c.get()
    res = Label(R, text=f"Enter {rows * cols} Elements")
    res.pack()
    value = StringVar()
    ee3 = Entry(R, textvariable=value)
    ee3.pack()
    but = Button(R, text="Goo", command=solve)
    but.pack()


R = Tk()
R.wm_maxsize(400, 700)
R.wm_minsize(400, 700)
r = IntVar()
Row = Entry(R, textvariable=r)
Row.pack()
c = IntVar()
Col = Entry(R, textvariable=c)
Col.pack()
bt = Button(R, text="Go", command=calculate)
bt.pack()
R.mainloop()
