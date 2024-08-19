import tkinter as tk
from tkinter import ttk
from NumberChange import *

class NumChangeFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(master=root)
        self.oldnum = tk.StringVar()
        self.F=tk.IntVar()
        self.Y=tk.IntVar()
        self.textvar = tk.StringVar()
        self.create_NCpage()

    def create_NCpage(self):

        s = ttk.Style()
        s.configure('my.TButton', font=('FangSong',15,'bold'))

        ttk.Label(self,text="数 制 转 换",font=('FangSong',25,'bold')).grid(row=0,column=1,columnspan=3,padx=15,pady=30)
        ttk.Label(self,text="请输入将要转换的数：",font=('FangSong',15,'bold')).grid(row=1,column=1,padx=15)
        self.numenter = ttk.Entry(self,textvariable=self.oldnum,font=30,width=20)
        self.numenter.grid(row=1,column=2,padx=15)

        self.oldsystem = ttk.Labelframe(self,text="请选择输入数的进制")
        self.oldsystem.grid(row=2,column=1,columnspan=2,pady=20)

        self.C2 = ttk.Radiobutton(self.oldsystem,text="2",variable=self.F,value=2).grid(row=1,column=1,padx=15,pady=5)
        self.C3 = ttk.Radiobutton(self.oldsystem,text="3",variable=self.F,value=3).grid(row=2,column=1,pady=5)
        self.C4 = ttk.Radiobutton(self.oldsystem,text="4",variable=self.F,value=4).grid(row=1,column=2,padx=15)
        self.C5 = ttk.Radiobutton(self.oldsystem,text="5",variable=self.F,value=5).grid(row=2,column=2)
        self.C6 = ttk.Radiobutton(self.oldsystem,text="6",variable=self.F,value=6).grid(row=1,column=3,padx=15)
        self.C7 = ttk.Radiobutton(self.oldsystem,text="7",variable=self.F,value=7).grid(row=2,column=3)
        self.C8 = ttk.Radiobutton(self.oldsystem,text="8",variable=self.F,value=8).grid(row=1,column=4,padx=15)
        self.C9 = ttk.Radiobutton(self.oldsystem,text="9",variable=self.F,value=9).grid(row=2,column=4)
        self.C10 = ttk.Radiobutton(self.oldsystem,text="10",variable=self.F,value=10).grid(row=1,column=5,padx=15)
        self.C16 = ttk.Radiobutton(self.oldsystem,text="16",variable=self.F,value=16).grid(row=2,column=5)

        ttk.Button(self,text="开始转换",style='my.TButton',command=self.NumChange).grid(row=2,column=3)

        ttk.Label(self,text="进制转换后数据:",font=('FangSong',15,'bold')).grid(row=3,column=1,padx=15)
        self.outwin = tk.Text(self,font=30,height=2,width=30)
        self.outwin.grid(row=3,column=2,columnspan=2,padx=15)

        self.newsystem = ttk.Labelframe(self,text="请选择需要转换的进制")
        self.newsystem.grid(row=4,column=1,columnspan=2,pady=20)

        ttk.Radiobutton(self.newsystem,text="2",variable=self.Y,value=2).grid(row=1,column=1,padx=15,pady=5)
        ttk.Radiobutton(self.newsystem,text="3",variable=self.Y,value=3).grid(row=2,column=1,pady=5)
        ttk.Radiobutton(self.newsystem,text="4",variable=self.Y,value=4).grid(row=1,column=2,padx=15)
        ttk.Radiobutton(self.newsystem,text="5",variable=self.Y,value=5).grid(row=2,column=2)
        ttk.Radiobutton(self.newsystem,text="6",variable=self.Y,value=6).grid(row=1,column=3,padx=15)
        ttk.Radiobutton(self.newsystem,text="7",variable=self.Y,value=7).grid(row=2,column=3)
        ttk.Radiobutton(self.newsystem,text="8",variable=self.Y,value=8).grid(row=1,column=4,padx=15)
        ttk.Radiobutton(self.newsystem,text="9",variable=self.Y,value=9).grid(row=2,column=4)
        ttk.Radiobutton(self.newsystem,text="10",variable=self.Y,value=10).grid(row=1,column=5,padx=15)
        ttk.Radiobutton(self.newsystem,text="16",variable=self.Y,value=16).grid(row=2,column=5)

    def NumChange(self):

        try:
            oldnum = self.oldnum.get()
            oldsystem = self.F.get()
            newsystem = self.Y.get()
            newnum = SystemChange(oldnum,oldsystem,newsystem)
            self.outwin.delete('1.0','end')
            self.textvar = newnum + "\n"
            self.outwin.insert("end",self.textvar)
        except:
            self.outwin.delete('1.0','end')
            self.textvar = "请检查输入和进制选择"+"\n"
            self.outwin.insert("end",self.textvar)

        '''
        oldnum = self.oldnum.get()
        oldsystem = self.F.get()
        newsystem = self.Y.get()
        newnum = SystemChange(oldnum,oldsystem,newsystem)
        self.outwin.delete('1.0','end')
        self.textvar = newnum + "\n"
        self.outwin.insert("end",self.textvar)
        '''