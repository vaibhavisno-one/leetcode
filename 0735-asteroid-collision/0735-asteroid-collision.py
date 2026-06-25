class Solution(object):
    def asteroidCollision(self, asteroids):

        st=[]

        for stone in asteroids:

            while st and st[-1] > 0 and stone < 0:

                if abs(st[-1]) < abs(stone):
                    st.pop()

                elif abs(st[-1]) == abs(stone):
                    st.pop()
                    break

                else:
                    break

            else:
                st.append(stone)

        return st