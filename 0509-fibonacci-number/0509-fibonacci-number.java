class Solution {
    public int fib(int n) {
        if(n==0)return 0;
        if(n==1)return 1;
        int first=0;
        int sec=1;
        for(int i = 2 ;i<=n;i++){
int next=first+sec;

first = sec;
sec = next;
        }
return sec;
    }
}