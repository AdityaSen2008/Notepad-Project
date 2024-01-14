import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import datetime
from replace_window_show import *
from go_to_window import *

# Creating the main window
notepad_root = tk.Tk()
notepad_root.title("Notepad Clone")
notepad_root.geometry("500x400")

#making the functions
def confirm_the_msg():
    messagebox.showinfo('Notepad Clone', 'Are you sure to remove the previous text?')
    new_text()
def new_text():
    text_widget.delete("1.0", tk.END)
def new_window():
    root = tk.Tk()
    root.title("Notepad Clone")
    root.geometry("500x400")
    # Creating a menu bar
    top_menubar = tk.Menu(root)

    #making the menus
    m1 = tk.Menu(top_menubar, tearoff=0)
    m1.add_command(label = "New", command = confirm_the_msg)
    m1.add_command(label = "New Window", command = new_window)
    m1.add_command(Label = "Save", command=save1)
    m1.add_command(Label = "Save as" , command = save_as)
    m1.add_separator()
    m1.add_command(label = "Exit", command = root.quit)
    top_menubar.add_cascade(label = "File", menu = m1)
    root.configure(menu = top_menubar)

    m2 = tk.Menu(top_menubar, tearoff=0)
    m2.add_command(label = "Date and Time", command = show_time)
    m2.add_command(label = "Replace", command = replace_word)
    m2.add_separator()
    m2.add_command(label = "Find Line", command = go_to_window_for_notepad_clone)
    top_menubar.add_cascade(label = "Edit", menu = m2)
    root.configure(menu = top_menubar)

    m3 = tk.Menu(top_menubar, tearoff=0)
    root.config(menu=top_menubar)

    submenu1 = tk.Menu(m3, tearoff=0)
    m3.add_cascade(label="Zoom", menu=submenu1)
    submenu1.add_command(label="Zoom In", command=about_notepad)
    submenu1.add_command(label="Zoom Out", command=about_notepad)
    submenu1.add_command(label="Re-store Default Zoom", command=about_notepad)
    top_menubar.add_cascade(label="View", menu=m3)

    m4 = tk.Menu(top_menubar, tearoff=0)
    m4.add_command(label="About Notepad", command=about_notepad)
    top_menubar.add_cascade(label="Help", menu=m4)
    root.configure(menu=top_menubar)

    # Creating a Text widget for typing
    text_widget = tk.Text(root)
    text_widget.pack()

def save_as():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
    )

    if file_path:
        # Get the text from your text widget (assuming it's named text_widget)
        text_content = text_widget.get("1.0", tk.END)

        # Write the text to the chosen file
        with open(file_path, "w") as file:
            file.write(text_content)

def show_time():
    x = datetime.datetime.now()
    messagebox.showinfo('Date and Time', f'The accurate time is {x}')
def replace_word():
    open_replace_window()
def about_notepad():
    pass
def zoom_in():
    pass
def zoom_out():
    pass
def restore():
    pass
def save1():
    pass

# Creating a menu bar
top_menubar = tk.Menu(notepad_root)

#making the menus
m1 = tk.Menu(top_menubar, tearoff=0)
m1.add_command(label = "New", command = confirm_the_msg)
m1.add_command(label = "New Window", command = new_window)
m1.add_command(label = "Save", command=save1)
m1.add_command(label = "Save as" , command = save_as)
m1.add_separator()
m1.add_command(label = "Exit", command = notepad_root.quit)
top_menubar.add_cascade(label = "File", menu = m1)
notepad_root.configure(menu = top_menubar)

m2 = tk.Menu(top_menubar, tearoff=0)
m2.add_command(label = "Date and Time", command = show_time)
m2.add_command(label = "Replace", command = replace_word)
m2.add_separator()
m2.add_command(label = "Find Line", command = go_to_window_for_notepad_clone)
top_menubar.add_cascade(label = "Edit", menu = m2)
notepad_root.configure(menu = top_menubar)

m3 = tk.Menu(top_menubar, tearoff=0)
notepad_root.config(menu=top_menubar)

submenu1 = tk.Menu(m3, tearoff=0)
m3.add_cascade(label="Zoom", menu=submenu1)
submenu1.add_command(label="Zoom In", command=zoom_in)
submenu1.add_command(label="Zoom Out", command=zoom_out)
submenu1.add_command(label="Re-store Default Zoom", command=restore)
top_menubar.add_cascade(label="View", menu=m3)

m4 = tk.Menu(top_menubar, tearoff=0)
m4.add_command(label="About Notepad", command=about_notepad)
top_menubar.add_cascade(label="Help", menu=m4)
notepad_root.configure(menu=top_menubar)

# Creating a Text widget for typing
text_widget = tk.Text(notepad_root)
text_widget.pack()

# Running the Tkinter event loop
notepad_root.mainloop()
