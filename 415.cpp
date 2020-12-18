class Solution {
public:
    string add(string num1, string num2){
        int l1 = num1.length();
        int l2 = num2.length();
        // l1 <= l2
        int n = 0;
        string temp = "";
        int com = 0;
        while (n < l1)
        {
            int j = com + (num1[l1 - n - 1] - '0') + (num2[l2 - n - 1] - '0');
            if (j >= 10)
            {
                com = 1;
                j = j - 10;
            }
            else
            { com = 0;};
            cout << j << endl;
            temp = to_string(j) + temp;
            ++n;
        }
        while (n < l2)
        {
            int j = com +  (num2[l2 - n - 1] - '0');
            if (j >= 10)
            {
                com = 1;
                j = j - 10;
            }
            else
            { com = 0;};
            temp = to_string(j) + temp;
            ++n;
        }
        if (com == 1)
        {temp = to_string(com) + temp;}
        return temp;
    }
    string addStrings(string num1, string num2) {
        string temp;
        int l1 = num1.length();
        int l2 = num2.length();
        temp = (l1 <= l2)? add(num1,num2):add(num2,num1);
        return temp;
    }
};