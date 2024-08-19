import tkinter as tk
from tkinter import ttk
class AboutFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(master=root)
        self.about = "该计算器运用栈、链表等数据结构实现了多项式加、减、乘、次方、求导的混合运算。且支持直接输入计算表达式进行计算。"
        self.create_Apage()
    def create_Apage(self):
        tk.Label(self,text="关 于 我 们",font=('FangSong',30,'bold')).place(x=215,y=25,width=220,height=50)
        tk.Label(self,text=self.about,font=('FangSong',20),wraplength=430).place(x=50,y=100,width=550,height=150)
        #tk.Label(self,text=" ",font=20).pack(anchor='sw',pady=50)
        tk.Label(self,text="版本：2.1.16",font=20).place(x=50,y=320,width=130,height=30)
        tk.Label(self,text="开发者：fyf",font=20).place(x=50,y=370,width=120,height=30)
        tk.Label(self,text="更新日期：2022.10.4",font=20).place(x=50,y=420,width=200,height=30)

