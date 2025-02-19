# from tkinter import *
# from tkcalendar import Calendar
# def get_date():
#     def get_():
#         print(cal)
#         r.destroy()
#     r = Tk()
#     r.wm_minsize(250, 210)
#     r.wm_maxsize(250, 210)
#     cal = Calendar(r)
#     cal.pack()
#     but = Button(r, text='Select Date', command=get_)
#     but.pack()
#     r.mainloop()
# get_date()
# import datetime
# import time
#
#
# def date_time():
#     current_date_time = (f"{datetime.date.today()} "
#                          f"{time.strftime('%H:%M:%S', time.localtime())}")
#     print( current_date_time)
# date_time()
import random

# import tkinter as tk
#
# def on_key_press(event):
#     key = event.char
#     if key == 'k':
#         my_function()
#
# def my_function():
#     print("Function executed!")
#
# # Create a tkinter window
# root = tk.Tk()
#
# # Bind the function to the 'k' key press event
# root.bind('<KeyPress>', on_key_press)
#
# # Run the tkinter event loop
# root.mainloop()
# from tkinter import *
#
# OPTIONS = [
#     "hello_world",
#     "save_file",
#     "create_object"
# ]  # etc
#
#
# def hello_world():
#     print("Hello World")
#     pass
#
#
# def save_file():
#     print("File Saved")
#     pass
#
#
# def create_object():
#     print("Object Created")
#     pass
#
#
# def picker():
#     if variable.get() == "hello_world":
#         hello_world()
#     if variable.get() == "save_file":
#         save_file()
#     if variable.get() == "create_object":
#         create_object()
#
#
# root = Tk()
# root.geometry("100x100")
# root.title("Dropdown demo")
#
# variable = StringVar(root)
# variable.set(OPTIONS[0])  # default value
#
# om = OptionMenu(root, variable, *OPTIONS)
# om.pack()
#
# caller_button = Button(text="Call function", command=lambda: picker())
# caller_button.pack(pady=10)
#
# mainloop()
# from tkinter import *
# from PIL import ImageTk
# root = Tk()
# root.geometry("300x200")
#
# w = Label(root, text='GeeksForGeeks', font="50")
# w.pack()
# im = ImageTk.PhotoImage(file="brand.jpg")
# menubutton = Menubutton(root, image=im)
#
# menubutton.menu = Menu(menubutton)
# menubutton["menu"] = menubutton.menu
#
# var1 = IntVar()
# var2 = IntVar()
# var3 = IntVar()
# def hello():
#     print("dsf")
#     menubutton.destroy()
#
# menubutton.menu.add_checkbutton(label="Courses",
#                                 variable=var1, command=hello)
# menubutton.menu.add_checkbutton(label="Students",
#                                 variable=var2)
# menubutton.menu.add_checkbutton(label="Careers",
#                                 variable=var3)
#
# menubutton.pack()
# root.mainloop()

# IMAGES
# a = ["img1", "img2", "img3"]  # file name.jpg
# s = random.randint(0, len(a) - 1)
# print(s)  # file=s
# import tkinter as tk
#
# def on_vertical_scroll(*args):
#     canvas.yview(*args)
#
# root = tk.Tk()
# root.title("Scroll Bar Example")
#
# # Create a frame to hold the scrollable content
# scroll_frame = tk.Frame(root)
# scroll_frame.pack(fill=tk.BOTH, expand=True)
#
# # Create a canvas to contain the scrollable frame
# canvas = tk.Canvas(scroll_frame)
# canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# # Add a vertical scrollbar to the canvas
# scrollbar = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL, command=on_vertical_scroll)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#
# # Configure the canvas to use the scrollbar
# canvas.configure(yscrollcommand=scrollbar.set)
#
# # Create a frame to hold the content (replace this with your actual content)
# content_frame = tk.Frame(canvas)
# canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)
#
# # Add some sample content to the content frame
# for i in range(20):
#     tk.Label(content_frame, text=f"Label {i}").pack()
#
# # Bind the canvas to the frame resizing event
# def on_canvas_configure(event):
#     canvas.configure(scrollregion=canvas.bbox("all"))
#
# canvas.bind("<Configure>", on_canvas_configure)
#
# root.mainloop()
import tkinter as tk
from tkinter import ttk


def on_search():
    search_query = search_entry.get().lower()

    # Clear previous search results
    tree.selection_remove(tree.get_children())

    # Iterate through all items in the treeview
    for item in tree.get_children():
        values = tree.item(item, 'values')

        # Check if the search query is present in any of the columns
        if any(search_query in str(value).lower() for value in values):
            tree.selection_add(item)


# Create the main window
root = tk.Tk()
root.title("Treeview Search Example")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=('Name', 'Age', 'City'))

# Add columns to the Treeview
tree.heading('#0', text='ID')
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')
tree.heading('City', text='City')

# Insert sample data into the Treeview
data = [
    (1, 'John Doe', 25, 'New York'),
    (2, 'Jane Smith', 30, 'San Francisco'),
    (3, 'Bob Johnson', 22, 'Los Angeles'),
    # Add more data as needed
]

for row in data:
    tree.insert('', 'end', values=row)

# Create an Entry widget for the search query
search_entry = tk.Entry(root)
search_entry.pack(pady=10)

# Create a Search button
search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack()

# Pack the Treeview widget
tree.pack(expand=True, fill=tk.BOTH)

# Run the Tkinter event loop
root.mainloop()



