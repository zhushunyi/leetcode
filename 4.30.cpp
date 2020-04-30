class Solution {
public:
    int sum(int n){
        int temp = 0;
        while (n!=0){
            int i = n%10;
            n = (n-i)/10;
            temp = temp + i*i;
        }
        return temp;
    }


    bool isHappy(int n) {
        vector<int> vec;
        while(n!=1)
        {
            vec.push_back(n);
            n=sum(n);
            vector<int>::iterator it = find(vec.begin(),vec.end(),n);
            if (it != vec.end())
            {return false;}
        }
        return true;
    }
};