class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.length() == 0)
        {return 0;}
        int total = haystack.length();
        int need = needle.length();
        if (total < need)
        {return -1;}
        int i = 0;
        int flag = -1;
        // following is not needed
        /*if (total == need)
        {
            for (int j =0; j < need; ++j)
            {
                if (needle[j] != haystack[j])
                {
                    return -1;
                }
            }
            return 0;
        }*/ 
        while (i < total - need + 1)
        {
            if (needle[0] != haystack[i])
            {
                ++i;
            }
            else
            {
                flag = -1;
                for (int j = 0; j < need; ++j)
                {
                    if (needle[j] != haystack[j+i])
                    {
                        cout << j << endl;
                        flag = -2;
                    }
                }
                if (flag != -2)
                {return i;}
                ++i;
            }
        }
        return -1;
    }
};