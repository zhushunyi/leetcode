class Twitter {
        vector<pair<int,int> >pst;
        vector<pair<int,int> >followid;

public:
    /** Initialize your data structure here. */
    Twitter() {


    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        pst.push_back(make_pair(userId,tweetId));

    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<int>output;
        vector<int>follower;
        int k = pst.size();
        int tmp = 0;
        int m = followid.size();
        follower.push_back(userId);
        for (int i = 0; i < m; ++i)
        {
            if (followid[i].first==userId)
            {
                follower.push_back(followid[i].second);
            };
        };
        for (int j = k - 1; j >=0; --j)
        {
            vector<int>::iterator iter = find(follower.begin(),follower.end(),pst[j].first);
            if (iter!=follower.end())
            {
                output.push_back(pst[j].second);
                ++tmp;
            };
            if (tmp == 10)
            {break;}
        };
        return output;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        followid.push_back(make_pair(followerId,followeeId));
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        vector<pair<int,int> >::iterator it;
        for (it=followid.begin();it!=followid.end();++it)
        {
            if (*it == make_pair(followerId,followeeId))
            {
                it = followid.erase(it);
                break;
            };
        };
    };
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */