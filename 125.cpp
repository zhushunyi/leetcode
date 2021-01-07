class Solution {
public:
    bool isPalindrome(string s) {
        string sgood;
        for (char ch: s) {
            if (isalnum(ch)) {
                sgood += tolower(ch);
            }
        }
        cout << sgood << endl;
        int n = sgood.size() - 1;
        if (n<= 0)
        {return true;}
        int m = 0;
        while (m < n)
        {
            if (sgood[m] == sgood[n])
            {
                ++m;
                --n;
            }
            else
            {return false;}
        }
        return true;
    }
};