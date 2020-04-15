class Solution {
    int bound[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
public:
    /*int getdistance(vector<vector<int>>& matrix, pair<int,int>point, int height, int width)
    {
        int temp = 0;
        queue<pair<int,int>>myqueue;
        if (matrix[point.first][point.second] == 0)
        {return temp;};
        while (matrix[point.first][point.second]!= 0)
        {
            if (point.first == 0 && point.second == 0)
            {
                myqueue.push(make_pair(1,0));
                myqueue.push(make_pair(0,1));
            };
            else if (point.first == 0 && point.second == height - 1)

        }

        
    }*/
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int height = matrix.size();
        int width = matrix[0].size();
        queue<pair<int,int>> myqueue;
        vector<vector<int> > vec(height, vector<int>(width));
        vector<vector<int> > visited(height,vector<int>(width));
        for (int i =0; i < height; ++i)
        {
            for (int j = 0; j < width; ++j)
            {
                if (matrix[i][j]==0)
                {
                    myqueue.push(make_pair(i,j));
                    visited[i][j] = 1;
                };
            };
        };
        while (!myqueue.empty())
        {
            pair<int,int> temp = myqueue.front();
            int i = temp.first;
            int j = temp.second;
            myqueue.pop();
            for (int k = 0; k < 4; ++k)
            {
                int temp1 = i + bound[k][0];
                int temp2 = j + bound[k][1];
                if (temp1>-1 && temp1 < height && temp2>-1 && temp2<width && visited[temp1][temp2] == 0)
                {
                    vec[temp1][temp2] = vec[i][j]+1;
                    visited[temp1][temp2] = 1;
                    myqueue.push(make_pair(temp1,temp2));
                };
            };
        };

        return vec;

    }
};