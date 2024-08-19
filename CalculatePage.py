import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PolyCalcu import BeginCalcu
from Examine import Examine

class CalculateFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(master=root)
        self.answer = ""
        self.result = ""

        self.equation=tk.StringVar()
        self.var=tk.StringVar()
        self.ans_var = tk.StringVar()
        self.create_Cpage()

    def create_Cpage(self):
        s = ttk.Style()
        s.configure('my.TButton', font=('FangSong',15,'bold'))

        ttk.Label(self,text="方 程 输 入 框",font=('FangSong',20,'bold')).place(x=215,y=25,width=220,height=50)

        self.equ_enter=ttk.Entry(self,textvariable=self.equation,font=20,width=50)
        self.equ_enter.place(x=50,y=100,width=550,height=50)
        self.scr=ttk.Scrollbar(self,orient="horizontal")  # 创建一个横向滚动条
        self.scr.place(x=50,y=160,width=550,height=20)   # 定位滚动条
        self.equ_enter.config(xscrollcommand = self.scr.set)  # 文本框绑定滚动条滚动
        self.scr.config(command =self.equ_enter.xview) 

        ttk.Button(self,text="开始计算",style='my.TButton',command=self.calculate_func).place(x=275,y=190,width=100,height=30)
    
        self.res_text=tk.Text(self,font=30,height=8,width=50)
        self.res_text.place(x=50,y=230,width=550)
        
        self.save = ttk.Button(self,text="保存结果",style='my.TButton',command=self.save)
        self.save.place(x=500,y=420,width=100,height=30)

        self.ans_text=tk.Text(self,font=30,height=3,width=50)
        self.ans_text.place(x=50,y=410,width=400)
        

    def calculate_func(self):
        equation = self.equation.get()
        if "answer" in equation :
            equ="(" + self.answer + ")"
            equation = equation.replace("answer",equ)

        try:
            examiner = Examine().Begin_Exam(equation)
            if examiner == True :
                self.result = BeginCalcu().Begin(equation)
                if self.result == False :
                    self.var = "= 多项式书写不规范" + "\n"
                    self.res_text.insert("end",self.var)
                else:
                    self.var =equation + "\n" "=" + self.result + "\n" + "\n"
                    self.res_text.insert("end",self.var)
                    self.equ_enter.delete(0,"end")
            else:
                self.var = examiner + "\n"
                self.res_text.insert("end",self.var)
        except:
            self.var = "请检查书写规范" + "\n"
            self.res_text.insert("end",self.var)
        
    def save(self):
        if self.result == False or self.result == "":
            self.ans_var = "失败" + "\n"
            self.ans_text.insert("end",self.ans_var)
        else:
            self.answer = self.result
            self.ans_text.delete('1.0','end')
            self.ans_var="保存成功"+"\n"+"answer="+self.answer + "\n"
            self.ans_text.insert("end",self.ans_var)


        '''
        examiner = Examine().Begin_Exam(equation)
        if examiner == True :
            self.result = BeginCalcu().Begin(equation)
            if self.result == False :
                self.var = "= 多项式书写不规范" + "\n"
                self.res_text.insert("end",self.var)
            else:
                self.var =equation + "\n" "=" + self.result + "\n" + "\n"
                self.res_text.insert("end",self.var)
                self.equ_enter.delete(0,"end")
        else:
            self.var = examiner + "\n"
            self.res_text.insert("end",self.var)
        '''