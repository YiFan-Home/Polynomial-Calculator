from Polynomial import *
from Stacklist import StackList
from Change import *

class BeginCalcu ():
    def Begin(self,equation):
        if "{" in equation :
            return self.complex_run(equation)
        else:
            return self.run(equation)

    def run(self,equation):
        var,express = Equation_Change().equ_change(equation)
        for i in var :
            if Pol_IsLegal(i) == False :
                return False #"多项式表达不规范"
        if len(var) == 1 :
            return var[0]
        else:  
            exp = Express_Change().exp_change(express)
            stack=StackList()
            for i in exp :
                if i == "+" :
                    A=stack.Pop()
                    B=stack.Pop()
                    result=Pol_Calculate().Add_func(A,B)
                    stack.Push(result)
                elif i == "-" :
                    A=stack.Pop()
                    B=stack.Pop()
                    result=Pol_Calculate().Minus_func(B,A)
                    stack.Push(result)
                elif i == "*" :               
                    A=stack.Pop()
                    B=stack.Pop()
                    result=Pol_Calculate().Multiply_func(A,B)
                    stack.Push(result)
                else:
                    stack.Push(var[i])
            all_res = (stack.Pop()).Change()
            return all_res

    def complex_run(self,equation):
        stack = StackList()
        final_equ=""
        equ_len = len(equation)

        i=0
        while i < equ_len :
            if equation[i] == "{" :
                stack.Push(str(equation[i]))
                i=i+1
            elif equation[i] == "}" :
                subequ=""
                while stack.Top != "{" :
                    subequ=stack.Pop() + subequ
                stack.DeleteTop()
                if subequ != "" :
                    subres=self.run(subequ)
                    if subres == False :
                        return False
                    else:
                        if equation[i+1] == "'" :
                            subres = Pol_Calculate().Derivat_func(subres)
                            subres="(" + subres.Change() + ")"
                            if stack.IsEmpty() :
                                final_equ = final_equ +subres
                            else:
                                stack.Push(subres)
                            i=i+2
                        else:
                            time=int(equation[i+3])-1
                            t=0
                            real_res = subres
                            while t < time :
                                real_res = Pol_Calculate().Multiply_func(real_res,subres)
                                #real_res="(" + real_res.Change() + ")"
                                real_res=real_res.Change()
                                t=t+1
                            real_res = "(" + real_res + ")"
                            if stack.IsEmpty() :
                                final_equ = final_equ + real_res
                            else:
                                stack.Push(real_res)
                            i=i+4
            else:
                if stack.IsEmpty() :
                    final_equ = final_equ + equation[i]
                    i=i+1
                else:
                    stack.Push(equation[i])
                    i=i+1
        final_res = self.run(final_equ)
        if final_res == False :
            return False
        else:
            return final_res


