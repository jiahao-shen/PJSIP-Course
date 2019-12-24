def __init__(self):
    super().__init__()

    """
    Initialize PJSUA2
    """
    self.ep = Endpoint()
    self.ep.libCreate()

    self.ep_cfg = pj.EpConfig()
    # self.ep_cfg.uaConfig.threadCnt = 0
    # self.ep_cfg.uaConfig.mainThreadOnly = True
    self.ep_cfg.logConfig.level = 1

    self.ep.libInit(self.ep_cfg)

    self.ts_cfg = pj.TransportConfig()
    self.ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, self.ts_cfg)
    self.ep.libStart()

    """
    Initialize Account
    """
    self.acc = None
    self.domain = DEFAULT_DOMAIN

    self.buddy_list = {}
    self.chat_list = {}

    """
    Initialize UI
    """
    self.title('SIP Client')
    self.resizable(width=False, height=False)
    self.geometry('+{}+{}'.format(int(self.winfo_screenwidth() / 2),
                                  int(self.winfo_screenheight() / 2)))

    self.buddy = tk.Entry(self, font=FONT_CONTENT, width=30)
    self.buddy.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    self.buddy.bind('<Return>', self._add_buddy)

    self.buddy_view = ttk.Treeview(self, column=['1', '2'], show='headings',
                                   selectmode='browse')
    self.buddy_view.column('1', width=80, anchor='center')
    self.buddy_view.column('2', width=200, anchor='center')
    self.buddy_view.heading('1', text='Buddies')
    self.buddy_view.heading('2', text='Status')
    self.buddy_view.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    self.buddy_view.bind('<Double-Button-1>', self._create_chat)
    self.buddy_view.bind('<BackSpace>', self._delete_buddy)

    tk.Button(self, text='Logout', font=FONT_CONTENT, width=8,
              command=self._login).grid(row=2, column=0, padx=10, pady=10)
    tk.Button(self, text='Exit', font=FONT_CONTENT, width=8,
              command=self._exit).grid(row=2, column=2, padx=10, pady=10)

    self._login()

    # self._on_timer()

    self.mainloop()