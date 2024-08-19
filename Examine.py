from Stacklist import StackList

class Examine():
    def Begin_Exam(self,equation):
        examiner=self.__symbol_ex(equation)
        if examiner != True :
            return examiner
        else:
            examiner = self.__Brace_ex(equation)
            if examiner != True :
                return examiner
            else:
                return True

    def __symbol_ex(self,equation):
            """
            括号检验
            """
            symbol=[".","x","0","1","2","3","4","5","6","7","8","9","^","-","+","*","'","(",")","[","]","{","}"]
            equlist=list(equation)
            stack=StackList()
            for i in equlist :
                if i in symbol :
                    if i =="(" or i =="[" or i == "{":
                        stack.Push(i)
                    elif i == ")" or i == "]" or i == "}":
                        if stack.IsEmpty() :
                            error = "表达式括号使用不合规！(可能：缺少左括号)"
                            return error
                        else:
                            if i == ")" and stack.Top == "(" :
                                stack.DeleteTop()
                            elif i == "]" and stack.Top == "[" :
                                stack.DeleteTop()
                            elif i == "}" and stack.Top == "{" :
                                stack.DeleteTop()
                            else:
                                error = "表达式括号使用不合规！(可能：括号出现交叉)"
                                return error
                else:
                    error = "表达式包含非法字符！"
                    return error
            if stack.IsEmpty() :
                return True
            else:
                error = "表达式括号使用不合规！(可能：缺少右括号)"
                return error

    def __Brace_ex(self,equation):
        number=["1","2","3","4","5","6","7","8","9"]
        equ_len = len(equation)
        i=0
        while i < equ_len :
            if equation[i] == "}" :
                if equation[i+1] == "'" :
                    i = i + 2
                elif equation[i+1] == "*" and equation[i+2] == "*" and equation[i+3] in number:
                    i = i + 3
                else:
                    error = "求导或次方表达式书写不合规！"
                    return error
            else:
                i = i + 1
        return True



'''
res=Examine().Begin_Exam("{(1+x^3+2x^3)+(2x^3+3x^5)}**2")
print(res)
'''