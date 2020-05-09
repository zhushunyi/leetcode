class Solution {
public:
    int mySqrt(int x) {
        if (x==0)
        {return 0;}
        if (x==1)
        {return 1;}
        double i = 1;
        while (i*i<=x)
        {
            ++i;
        }
        return --i;
        
    }
};