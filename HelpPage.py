import tkinter as tk
from tkinter import ttk

class HelpFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(master=root)
        self.help = "帮助文档"
        self.create_Hpage()
    
    def create_Hpage(self):
        tk.Label(self,text="相 关 帮 助",font=80).pack(anchor='n',pady=30)
        tk.Label(self,text=self.help,font=30,wraplength=430).pack(anchor='s')
