class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        if m==1 and n==1:
            return grid[0][0]
        if m==1:
            return sum(grid[0])
        if n==1:
            return sum(r[0] for r in grid)
        INF=10**18
        prevD=[[INF]*n for _ in range(m)]
        prevR=[[INF]*n for _ in range(m)]
        prevU=[[INF]*n for _ in range(m)]
        prevL=[[INF]*n for _ in range(m)]
        ans=INF
        for t in range(k+1):
            curD=[[INF]*n for _ in range(m)]
            curR=[[INF]*n for _ in range(m)]
            curU=[[INF]*n for _ in range(m)]
            curL=[[INF]*n for _ in range(m)]
            if t==0:
                curD[0][0]=curR[0][0]=grid[0][0]
                for i in range(m):
                    for j in range(n):
                        if i==0 and j==0: continue
                        if i>0 and curD[i-1][j]<INF:
                            curD[i][j]=curD[i-1][j]+grid[i][j]
                        if j>0 and curR[i][j-1]<INF:
                            curR[i][j]=curR[i][j-1]+grid[i][j]
            else:
                for i in range(m):
                    for j in range(n):
                        if i>0:
                            best=curD[i-1][j]
                            tb=prevR[i-1][j]
                            if prevU[i-1][j]<tb: tb=prevU[i-1][j]
                            if prevL[i-1][j]<tb: tb=prevL[i-1][j]
                            if tb<best: best=tb
                            if best<INF: curD[i][j]=best+grid[i][j]
                        if j>0:
                            best2=curR[i][j-1]
                            tb2=prevD[i][j-1]
                            if prevU[i][j-1]<tb2: tb2=prevU[i][j-1]
                            if prevL[i][j-1]<tb2: tb2=prevL[i][j-1]
                            if tb2<best2: best2=tb2
                            if best2<INF: curR[i][j]=best2+grid[i][j]
                for i in range(m-1,-1,-1):
                    for j in range(n-1,-1,-1):
                        if i+1<m:
                            best=curU[i+1][j]
                            tb=prevD[i+1][j]
                            if prevR[i+1][j]<tb: tb=prevR[i+1][j]
                            if prevL[i+1][j]<tb: tb=prevL[i+1][j]
                            if tb<best: best=tb
                            if best<INF: curU[i][j]=best+grid[i][j]
                        if j+1<n:
                            best2=curL[i][j+1]
                            tb2=prevD[i][j+1]
                            if prevR[i][j+1]<tb2: tb2=prevR[i][j+1]
                            if prevU[i][j+1]<tb2: tb2=prevU[i][j+1]
                            if tb2<best2: best2=tb2
                            if best2<INF: curL[i][j]=best2+grid[i][j]
            for a in (curD,curR,curU,curL):
                if a[m-1][n-1]<ans: ans=a[m-1][n-1]
            prevD,prevR,prevU,prevL=curD,curR,curU,curL
        return -1 if ans>=INF//2 else ans