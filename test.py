# import time
# import pjsua2 as pj
# import tkinter as tk
# from call import Call


# def test_call():
#     ep = pj.Endpoint()
#     ep.libCreate()

#     ep_cfg = pj.EpConfig()
#     # ep_cfg.uaConfig.threadCnt = 0
#     # ep_cfg.uaConfig.mainThreadOnly = True
#     ep_cfg.logConfig.level = 1

#     ep.libInit(ep_cfg)

#     sip_cfg = pj.TransportConfig()
#     ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, sip_cfg)
#     ep.libStart()

#     print('Account Create')
#     acc = pj.Account()
#     acc_cfg = pj.AccountConfig()
#     acc_cfg.idUri = 'sip:1001@27.102.107.237'
#     acc_cfg.regConfig.registrarUri = 'sip:27.102.107.237'
#     acc_cfg.regConfig.registerOnAdd = True
#     acc_cfg.sipConfig.authCreds.append(pj.AuthCredInfo(
#         'digest', '*', '1001', pj.PJSIP_CRED_DATA_PLAIN_PASSWD, '1001'))

#     acc.create(acc_cfg)

#     print('Call Start')
#     call = Call(acc, 'sip:1002@27.102.107.237')
#     call_prm = pj.CallOpParam()
#     call.makeCall('sip:1002@27.102.107.237', call_prm)

#     print('Sleep')
#     time.sleep(10)

#     ep.libDestroy()
#     ep = None


# def test_tkinter():
#     root = tk.Tk()

#     btn_1 = tk.Button(root, text='1', width=10)
#     btn_1.pack(side=tk.TOP)
#     # tk.Button(root, text='2', width=10).pack(side=tk.TOP)
#     # tk.Button(root, text='3', width=10).pack(side=tk.LEFT)
#     btn_1['text'] = 'A'

#     root.mainloop()


# if __name__ == '__main__':
#     # test_call()
#     test_tkinter()
        
# import tkinter as tk

# def onCanvasConfigure(e):
#     canvas.itemconfig('frame', height=canvas.winfo_height(), width=canvas.winfo_width())

# root=tk.Tk()

# canvas = tk.Canvas(root, background="blue")
# frame = tk.Frame(canvas, background="red")

# # tk.Label(frame, text='a').pack(anchor='w')
# # tk.Label(frame, text='a').pack(anchor='e')
# # tk.Label(frame, text='a').pack(anchor='center')
# # tk.Label(frame, text='a').pack(anchor='e')
# # tk.Label(frame, text='a').pack(anchor='w')

# canvas.pack(expand=True, fill="both")
# canvas.create_window((0,0), window=frame, anchor="nw", tags="frame")

# canvas.bind("<Configure>", onCanvasConfigure)

# root.mainloop()


from tkinter import *   # from x import * is bad practice
from tkinter.ttk import *

# http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)


        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()
        Label(self.interior, text='fdahjfhsakj').pack()

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


if __name__ == "__main__":

    class SampleApp(Tk):
        def __init__(self, *args, **kwargs):
            root = Tk.__init__(self, *args, **kwargs)


            self.frame = VerticalScrolledFrame(root)
            self.frame.pack()
            self.label = Label(text="Shrink the window to activate the scrollbar.")
            self.label.pack()

    app = SampleApp()
    app.mainloop()