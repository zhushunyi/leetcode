class Solution {
public:
int waysToStep(int n){
    if(n <= 2) return n;
    if (n == 3) return 4;
    int a = 1,b=2,c=4,d;
    n -= 3;
    while(n--){
        d = ((a+b)%1000000007+c)%1000000007;
        a = b;
        b = c;
        c = d;
    }
    return c;
}

};