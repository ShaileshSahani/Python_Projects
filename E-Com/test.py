# import mysql.connector
# from tkinter import *
# from tkinter import filedialog
# import os
# import cv2
# from PIL import Image, ImageTk
# try:
#     db = mysql.connector.connect(host="localhost", password="root", user="root")
#     cu = db.cursor()
#
#     cu.execute("CREATE DATABASE IF NOT EXISTS e_com_db")
#     cu.execute("use e_com_db")
#     cu.execute("CREATE TABLE IF NOT EXISTS images (IMG BLOB)")
#
#     root = Tk()
#     root.geometry("400x400")
#
#     def openfile():
#         path = filedialog.askopenfilename()
#         if path:
#             s = open(path, "rb")
#             print(s.read())
#
#             op = cv2.imread(path, 0)
#             print(op)
#             img = ImageTk.PhotoImage(Image.open(path))
#
#             lab = Label(root, image=img)
#             lab.image = img
#             lab.pack()
#             print("do")
#
#
#     bt = Button(root, text="Open", command=openfile)
#     bt.pack()
#
#     root.mainloop()
#
#
# except Exception as e:
#     print(e)
# import tkinter as tk
#
# class ToggleFrameApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Toggle Frame Example")
#
#         self.frame_visible = False
#
#         # Create a button to toggle the frame
#         self.toggle_button = tk.Button(root, text="Toggle Frame", command=self.toggle_frame)
#         self.toggle_button.pack(pady=10)
#
#         # Create a frame
#         self.frame = tk.Frame(root, width=200, height=100, bg="lightblue")
#
#     def toggle_frame(self):
#         if self.frame_visible:
#             # If frame is visible, destroy it
#             self.frame.destroy()
#             self.toggle_button.config(text="Toggle Frame")
#         else:
#             # If frame is not visible, create and pack it
#             self.frame = tk.Frame(self.root, width=200, height=100, bg="lightblue")
#             self.frame.pack(pady=10)
#             self.toggle_button.config(text="Destroy Frame")
#
#         # Toggle the frame visibility flag
#         self.frame_visible = not self.frame_visible
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ToggleFrameApp(root)
#     root.mainloop()
# import tkinter as tk
#
# def toggle_frame():
#     if frame.winfo_ismapped():
#         # If frame is visible, hide it
#         frame.pack_forget()
#         toggle_button.config(text="Show Frame")
#     else:
#         # If frame is not visible, show it
#         frame.pack(pady=10)
#         toggle_button.config(text="Hide Frame")
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Toggle Frame Example")
#
#     # Create a button to toggle the frame
#     toggle_button = tk.Button(root, text="Show Frame", command=toggle_frame)
#     toggle_button.pack(pady=10)
#
#     # Create a frame
#     frame = tk.Frame(root, width=200, height=100, bg="lightblue")
#
#     root.mainloop()
