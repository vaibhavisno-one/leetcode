class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        n=len(temperatures)
        arr=[0]*n
        x=0
        for i in range(n):
            while st and temperatures[st[-1]]<temperatures[i]:
                x=st.pop()
                arr[x]=i-x

            st.append(i)

        return arr



