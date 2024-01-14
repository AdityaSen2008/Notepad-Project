import tkinter as tk

def go_to_window_for_notepad_clone():
    # Creating the main window
    go_window = tk.Tk()
    go_window.title("Go to line")
    go_window.geometry("270x90")
    go_window.maxsize(270,90)
    go_window.minsize(270,90)

    # defining functions:
    def quit_gotowin():
        print("Hello duniyA")
        # go_window.quit

    # input place widget
    line_label = tk.Label(go_window, text = "Line Number : ")
    line_label.grid(row = 0, column = 0)
    line_entry = tk.Entry(go_window, width = 40)
    line_entry.grid(row = 1, padx = 10, pady = 7, columnspan = 3)

    # Explaining the buttons
    go_to_button = tk.Button(go_window, width = 8, text='Go to', command = quit_gotowin)
    cancel_button = tk.Button(go_window, width = 8, text='Cancel', command = lambda: print("Im here in Cancel"))
    go_to_button.grid(row = 2, column = 1)
    cancel_button.grid(row = 2, column = 2)

    # running the tkinter event loop
    go_window.mainloop()
# go_to_window_for_notepad_clone()