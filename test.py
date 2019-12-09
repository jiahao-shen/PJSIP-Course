import tkinter as tk


def on_change(event):
    print(event.widget.get())
    event.widget.delete(0, tk.END)


root = tk.Tk()

e = tk.Entry(root)
e.pack()
# Calling on_change when you press the return key
e.bind("<Return>", on_change)

root.mainloop()
