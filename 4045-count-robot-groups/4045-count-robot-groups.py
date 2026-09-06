class Solution:
    def countGroups(self, position: List[int], speed: List[int], distance: int) -> int:
        n = len(position)
        is_inf = [False]*n
        m_num = [0]*n
        m_den = [1]*n
        st = []
        for i in range(n-1, -1, -1):
            while True:
                if not st:
                    is_inf[i]=True
                    break
                s = st[-1]
                delta_p = position[s]-position[i]-distance
                if delta_p <= 0:
                    t_inf=False
                    t_num=0
                    t_den=1
                else:
                    if speed[s] >= speed[i]:
                        t_inf=True
                    else:
                        t_inf=False
                        t_num=delta_p
                        t_den=speed[i]-speed[s]
                if t_inf:
                    if is_inf[s]:
                        is_inf[i]=True
                        break
                    else:
                        st.pop()
                        continue
                else:
                    if is_inf[s]:
                        is_inf[i]=False
                        m_num[i]=t_num
                        m_den[i]=t_den
                        break
                    else:
                        if t_num*m_den[s] <= m_num[s]*t_den:
                            is_inf[i]=False
                            m_num[i]=t_num
                            m_den[i]=t_den
                            break
                        else:
                            st.pop()
                            continue
            st.append(i)
        return sum(is_inf)
