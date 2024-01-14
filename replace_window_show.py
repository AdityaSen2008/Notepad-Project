import tkinter as tk

def open_replace_window():
    # Creating the main window
    replace_window = tk.Tk()
    replace_window.title("Replace")
    replace_window.geometry("285x100")
    replace_window.maxsize(285,100)
    replace_window.minsize(285,100)

    # defining functions:
    def next_word():
        pass
    def replace_word():
        pass
    def replace_all_word():
        pass

    # input place widget
    missing_word_label = tk.Label(replace_window, text = "Find What : ")
    missing_word_label.grid(row = 0, column = 0)
    missing_word_entry = tk.Entry(replace_window, width = 20)
    missing_word_entry.grid(row = 0, column = 1, padx = 5)

    replace_word_label = tk.Label(replace_window, text = "Replace With : ")
    replace_word_label.grid(row=1, column=0)
    replace_word_entry = tk.Entry(replace_window, width = 20)
    replace_word_entry.grid(row = 1, column = 1, padx = 5)

    # Explaining the buttons
    next_button = tk.Button(replace_window, width = 8, text='Find Next', command = next_word)
    replace_button = tk.Button(replace_window, width = 8, text='Replace', command = replace_word)
    replace_all_button = tk.Button(replace_window, width = 8, text='Replace All', command = replace_all_word)
    cancel_button = tk.Button(replace_window, width = 8, text='Cancel', command = replace_window.quit)

    # # making the grid
    # missing_word_entry.grid(row = 0, column = 0)
    # replace_word_entry.grid(row = 1, column = 0)

    next_button.grid(row = 0, column = 2)
    replace_button.grid(row = 1, column = 2)
    replace_all_button.grid(row = 2, column = 2)
    cancel_button.grid(row = 3, column = 2)


    # running the tkinter event loop
    replace_window.mainloop()
# open_replace_window()