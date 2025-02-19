from tkinter import *

value = ""


class Calculator:

    @classmethod
    def cal_min(cls):
        def get_val(val):
            global value
            value += val
            output_res.config(text=value)

        def clear():
            global value
            value = ""
            output_res.config(text="")
            output_final.config(text="", foreground="black")

        def solve():
            global value
            if value == "":
                output_final.config(text="error")
            else:
                try:
                    try:
                        output_final.config(text=str(eval(value)))
                    except ZeroDivisionError:
                        output_final.config(text="Infinity")
                except SyntaxError:
                    output_final.config(text="Expression Error")

        def delete():
            global value
            if value == "":
                output_res.config(text="Error")
            else:
                s = list(value)
                s.pop()
                new = ""
                for i in s:
                    new += i
                value = new
                output_res.config(text=value)

        root = Tk()
        root.geometry("250x350")
        root.resizable(False, False)
        root.wm_title("My Calculator")

        output = Frame(root, height=150, width=250, bg="white", bd=1, relief=SOLID)
        output.place(x=0, y=0)

        output_res = Label(output, text="", bg="White", font=("Cambria Math", 17), anchor=SE)
        output_res.place(x=2, y=0)

        output_final = Label(output, text="Result", bg="White", font=("Cambria", 17), anchor=SE, fg="#414142")
        output_final.place(x=2, y=100)

        inp = Frame(root, height=200, width=250, bg="black")
        inp.place(x=0, y=151)

        but1 = Button(inp, text="1", font=('cambria', 15), padx=19, command=lambda: get_val("1"))
        but1.place(x=2, y=1)
        but2 = Button(inp, text="2", font=('cambria', 15), padx=19, command=lambda: get_val("2"))
        but2.place(x=65, y=1)
        but3 = Button(inp, text="3", font=('cambria', 15), padx=19, command=lambda: get_val("3"))
        but3.place(x=128, y=1)
        but_add = Button(inp, text="+", font=('cambria', 15), padx=16, bg="#b8e3e2", command=lambda: get_val("+"))
        but_add.place(x=191, y=1)

        but4 = Button(inp, text="4", font=('cambria', 15), padx=19, command=lambda: get_val("4"))
        but4.place(x=2, y=40)
        but5 = Button(inp, text="5", font=('cambria', 15), padx=19, command=lambda: get_val("5"))
        but5.place(x=65, y=40)
        but6 = Button(inp, text="6", font=('cambria', 15), padx=19, command=lambda: get_val("6"))
        but6.place(x=128, y=40)
        but_add = Button(inp, text="-", font=('cambria', 15), padx=18, bg="#b8e3e2", command=lambda: get_val("-"))
        but_add.place(x=191, y=40)

        but7 = Button(inp, text="7", font=('cambria', 15), padx=19, command=lambda: get_val("7"))
        but7.place(x=2, y=79)
        but8 = Button(inp, text="8", font=('cambria', 15), padx=19, command=lambda: get_val("8"))
        but8.place(x=65, y=79)
        but9 = Button(inp, text="9", font=('cambria', 15), padx=19, command=lambda: get_val("9"))
        but9.place(x=128, y=79)
        but_mul = Button(inp, text="x", font=('cambria', 15), padx=17, bg="#b8e3e2", command=lambda: get_val("*"))
        but_mul.place(x=191, y=79)

        but_des = Button(inp, text=".", font=('cambria', 15), padx=22, bg="#b8e3e2", command=lambda: get_val("."))
        but_des.place(x=2, y=118)
        but0 = Button(inp, text="0", font=('cambria', 15), padx=20, command=lambda: get_val("0"))
        but0.place(x=64, y=118)
        but_exp = Button(inp, text="**", font=('cambria', 15), padx=15, bg="#b8e3e2", command=lambda: get_val("**"))
        but_exp.place(x=129, y=118)
        but_div = Button(inp, text="/", font=('cambria', 15), padx=17, bg="#b8e3e2", command=lambda: get_val("/"))
        but_div.place(x=191, y=118)

        but_c = Button(inp, text="C", font=('cambria', 15), padx=19, bg="red", command=clear)
        but_c.place(x=2, y=157)
        but00 = Button(inp, text="00", font=('cambria', 15), padx=14, command=lambda: get_val("00"))
        but00.place(x=65, y=157)
        but_del = Button(inp, text="Del", font=('cambria', 15), padx=10, bg="orange", command=delete)
        but_del.place(x=129, y=157)
        but_eq = Button(inp, text="=", font=('cambria', 15), padx=16, bg="green", command=solve)
        but_eq.place(x=191, y=157)

        root.mainloop()


Calculator.cal_min()
