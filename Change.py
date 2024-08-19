from Stacklist import StackList

class Equation_Change():  
    def equ_change(self,equation : str):
        """
        提取多项式
        """
        equ = equation
        equlist=list(equ)
        var=[]
        left=[]
        right=[]
        for i in range (0,len(equlist)):
            if equlist[i] == "(" :
                left.append(i)
            elif equlist[i] == ")" :
                right.append(i)
        left_len=len(left)
        for i in range (0,left_len):
            start=left[i]+1
            end=right[i]
            sub_equ=equ[start:end]
            var.append(sub_equ)

        for i in range(1,left_len+1) :
            varindex=left_len-i
            start=left[varindex]
            end=right[varindex]+1
            del equlist[start:end]
            equlist.insert(start,varindex)
            
        return var,equlist


class Express_Change():
    """
    转换表达式
    """
    def exp_change(self,express):
        oldexp = express
        stack=StackList()
        stack.Push("#")
        sysmbol=["#","[","+","-","*","]"]
        newexp=[]
        for i in oldexp :
            if i in sysmbol :
                if i == "[" :
                    stack.Push(i)
                elif i == "]" :
                    while stack.Top != "[" :
                        newexp.append(stack.Pop())
                    stack.DeleteTop()
                elif i == "+" or i == "-" :
                    if stack.Top == "[" or stack.Top == "#":
                        stack.Push(i)
                    else:
                        newexp.append(i)
                else:
                    if sysmbol.index(stack.Top) < 3 :
                        stack.Push(i)
                    else:
                        newexp.append(i)
            else:
                newexp.append(i)
        while stack.Top != "#" :
            newexp.append(stack.Pop())
        return newexp

