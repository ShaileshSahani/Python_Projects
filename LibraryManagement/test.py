import tkinter as tk
from tkinter import ttk

def on_treeview_click(event):
    item = tree.focus()
    if item:  # Make sure an item is selected
        item_text = tree.item(item, "text")
        print(f"Item clicked: {item_text}")
        # Call your function here with the selected item_text

# Create the main application window
root = tk.Tk()
root.title("TreeView Click Example")

# Create a TreeView widget
tree = ttk.Treeview(root)
tree["columns"] = ("Name", "Age")

# Add columns
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

# Insert some sample data
for i in range(1, 6):
    tree.insert("", "end", text=f"{i}", values=(f"Name{i}", f"{20 + i}"))

# Bind the function to the click event
tree.bind("<ButtonRelease-1>", on_treeview_click)

# Pack the TreeView widget
tree.pack()

# Start the main event loop
root.mainloop()

