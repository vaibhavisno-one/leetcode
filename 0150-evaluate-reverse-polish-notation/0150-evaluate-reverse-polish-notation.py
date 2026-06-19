class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack=[]
        operators = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                second = stack.pop()
                first = stack.pop()

                if i == "+":
                    stack.append(first + second)
                elif i == "-":
                    stack.append(first - second)
                elif i == "*":
                    stack.append(first * second)
                else:  
                    stack.append(int(float(first) / second)) 

        return stack[-1]