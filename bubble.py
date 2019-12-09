"""
@project: PJSIP-Lab
@author: sam
@file bubble.py
@ide: Visual Studio Code
@time: 2019-12-08 01:08:47
@blog: https://jiahaoplus.com
"""
import tkinter as tk

class Bubble(tk.Frame):
    def __init__(self, parent=None, msg='', flag='left', **kw):
        tk.Frame.__init__(self, parent, kw)
        self.parent = parent

        self.content = tk.Label(self, text=msg, bg='#A0E759')
        self.content.pack(side='left')

        # self.canvas = tk.Canvas(self, bg='red', width=10)
        # self.canvas.create_polygon(-10, 0, -10, 0,0, 10, fill='#A0E759')
        # self.canvas.pack()

if __name__ == '__main__':
    root = tk.Tk()
    Bubble(root, 'fdsahfjsadhjkfh').pack()
    root.mainloop()

# from tkinter import *
# from datetime import datetime

# root = Tk()
# root.config(bg="lightblue")

# canvas = Canvas(root, width=200, height=200,bg="white")
# canvas.grid(row=0,column=0,columnspan=2)

# bubbles = []

# class BotBubble:
#     def __init__(self,master,message=""):
#         self.master = master
#         self.frame = Frame(master,bg="light grey")
#         self.i = self.master.create_window(90,160,window=self.frame)
#         Label(self.frame,text=datetime.now().strftime("%Y-%m-%d %H:%m"),font=("Helvetica", 7),bg="light grey").grid(row=0,column=0,sticky="w",padx=5)
#         Label(self.frame, text=message,font=("Helvetica", 9),bg="light grey").grid(row=1, column=0,sticky="w",padx=5,pady=3)
#         root.update_idletasks()
#         self.master.create_polygon(self.draw_triangle(self.i), fill="light grey", outline="light grey")

#     def draw_triangle(self,widget):
#         x1, y1, x2, y2 = self.master.bbox(widget)
#         return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2

# def send_message():
#     if bubbles:
#         canvas.move(ALL, 0, -65)
#     a = BotBubble(canvas,message=entry.get())
#     bubbles.append(a)

# entry = Entry(root,width=26)
# entry.grid(row=1,column=0)
# Button(root,text="Send",command=send_message).grid(row=1,column=1)
# root.mainloop()