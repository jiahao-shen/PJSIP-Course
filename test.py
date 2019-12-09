import tkinter as tk
root = tk.Tk()

# 左对齐，文本居中
tk.Label(root, text='welcome to www.py3study.com', bg='yellow', width=40, height=3, wraplength=80, 
justify='left').pack()

# 居中对齐，文本居左
tk.Label(root, text='welcome to www.py3study.com', bg='red', width=40, height=3, wraplength=80,
 anchor='w').pack()

#居中对齐，文本居右
tk.Label(root, text='welcome to www.py3study.com', bg='blue', width=40, height=3, wraplength=80,
 anchor='e').pack()

root.mainloop()