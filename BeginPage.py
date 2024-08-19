import tkinter as tk
from tkinter import ttk
#from tkinter import *
#from tkinter.ttk import *
from CalculatePage import CalculateFrame
from HelpPage import HelpFrame
from AboutPage import AboutFrame
from NumchangePage import NumChangeFrame

class InitialPage():
    def __init__(self,root):
        self.root=root
        self.root.title('Polynomial Calculator V2.5.16')
        self.root.geometry('650x500')
        self.create_Ipage()

        self.calculate_frame=CalculateFrame(self.root)
        self.numchang_frame=NumChangeFrame(self.root)
        self.help_frame=HelpFrame(self.root)
        self.about_frame=AboutFrame(self.root)
        self.calculate_frame.place(x=0,y=0,width=650,height=450)

    def create_Ipage(self):
        menu_bar=tk.Menu(self.root)
        menu_bar.add_command(label='计算',command=self.show_CPage)
        menu_bar.add_command(label='数制转换',command=self.show_NCPage)
        menu_bar.add_command(label='帮助',command=self.show_HPage)
        menu_bar.add_command(label='关于',command=self.show_APage)
        self.root['menu']=menu_bar

    def show_CPage(self):
        self.calculate_frame.place(x=0,y=0,width=650,height=450)
        self.help_frame.forget()
        self.about_frame.place_forget()
        self.numchang_frame.forget()

    def show_HPage(self):
        self.help_frame.pack()
        self.calculate_frame.place_forget()
        self.about_frame.place_forget()
        self.numchang_frame.forget()

    def show_APage(self):
        self.about_frame.place(x=0,y=0,width=650,height=450)
        self.help_frame.forget()
        self.calculate_frame.place_forget()
        self.numchang_frame.forget()

    def show_NCPage(self):
        self.numchang_frame.pack()
        self.about_frame.place_forget()
        self.help_frame.forget()
        self.calculate_frame.place_forget()



root=tk.Tk()
InitialPage(root)
root.mainloop()