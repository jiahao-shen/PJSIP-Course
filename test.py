# from win32gui import *
# import win32con
# import pywintypes
# from tkinter import *

# root=Tk()

# hwnd = pywintypes.HANDLE(int(root.frame(), 16))
# hdc=GetDC(hwnd)

# def callback(event):
#     root.update()

#     hbrush=GetStockObject(win32con.NULL_BRUSH)
#     oldbrush=SelectObject(hdc,hbrush)
#     Rectangle(hdc,50,50,100,100)

# root.geometry("400x400")

# root.bind("<Configure>",callback)

# root.mainloop()