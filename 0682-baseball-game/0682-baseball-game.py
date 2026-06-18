class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        

        stack=[]
        final=0

        for point in operations:
            if point != "D" and point !="C" and point!= "+":
                stack.append(int(point))
            
            elif point == "D":
                final=stack[-1]
                # stack.pop()
                stack.append(final*2)
            elif point =="+":
                one=int(stack[-1])
                two=int(stack[-2])

                final=one+two

                stack.append(final)

            elif point =="C":
                stack.pop()

            else:
                return 0

        return sum(stack)


