class Solution {
public:
    double geta(int p1x, int p1y, int p2x, int p2y)
    {
        if (p2x-p1x == 0)
        {
            return DBL_MAX;
        }
        else
        {
            double c = ((double)p2y - (double)p1y);
            double d = ((double)p2x - (double)p1x);
            return c/d;
        }
    }

    double getb(int p1, int p2, double x)
    {
        return ((double)p2 - x*(double)p1);
    }

    double getpoint(int x1,int x2,int x3,int x4)
    {
        int a[4] = {x1,x2,x3,x4};
        for (int i = 0; i < 3; ++i)
        {
            for (int j = 0; j < 3 - i; ++j)
            {
                if (a[j] > a[j+1])
                {
                    swap(a[j],a[j+1]);
                };
            };
        };
        return (double)a[1];
    }
    vector<double> intersection(vector<int>& start1, vector<int>& end1, vector<int>& start2, vector<int>& end2) {
        int p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y;
        p1x = start1[0];
        p1y = start1[1];
        p2x = end1[0];
        p2y = end1[1];
        p3x = start2[0];
        p3y = start2[1];
        p4x = end2[0];
        p4y = end2[1];
        double a1,b1,a2,b2;
        vector <double> target = {};
        a1 = geta(p1x,p1y,p2x,p2y);
        a2 = geta(p3x,p3y,p4x,p4y);
        if (a1 == DBL_MAX || a2 == DBL_MAX)
        {
            if (a1 == DBL_MAX && a2 != DBL_MAX)
            {
                if (max(p3x,p4x) < p1x || min(p3x,p4x) > p1x)
                {
                    cout << 1 << endl;
                    return target;}
                else
                {
                    cout << 2 << endl;
                    cout << a2 << " " << getb(p3x,p3y,a2) << endl;
                    target = {(double)p1x,a2 *p1x + getb(p3x,p3y,a2)};
                    return target;
                }
            }
            if (a1 != DBL_MAX && a2 == DBL_MAX)
            {
                if (max(p1x,p2x) < p3x || min(p1x,p2x) > p3x)
                {return target;}
                else
                {
                    target = {(double)p3x,a1*p3x + getb(p1x,p1y,a1)};
                    return target;
                }
            }
            if (a1 == DBL_MAX && a2 == DBL_MAX)
            {
                cout << 3 << endl;
                if (p1x!=p3x)
                {return target;}
                if (min(p1y,p2y)>max(p3y,p4y) || min(p3y,p4y)>max(p1y,p2y))
                {
                    cerr << 4 << endl;
                    return target;}
                else
                {
                    double p1 = getpoint(p1y,p2y,p3y,p4y);
                    target = {(double)p1x,p1};
                    return target;
                }

            }
        }
        b1 = getb(p1x,p1y,a1);
        b2 = getb(p3x,p3y,a2);
        if (a1 == a2 && b1 != b2)
        {
            return target;
        }
        else if  (a1 == a2 && b1 == b2)
        {
            cout << 5 << endl;
            if (min(p1x,p2x)>max(p3x,p4x) || min(p3x,p4x)>max(p1x,p2x))
            {
                cout << 6 << endl;
                return target;}
            else
            {
                double p1 = getpoint(p1x,p2x,p3x,p3x);
                target = {p1,a1*p1 + b1};
                return target;
            }
        }
        else
        {
            cout << 7 << endl;
            double x = (b2-b1)/(a1-a2);
            if (x>=min(p1x,p2x) && x<=max(p1x,p2x) && x >= min(p3x,p4x) && x <=max(p3x,p4x))
            {
                target = {x,a1*x + b1};
                return target;
            }
            else
            {return target;}
        }

        return target;
    }
};