class Solution {
public:
    vector<vector<int> > FindContinuousSequence(int sum) {
        vector<vector<int> > r;
        if(sum<=1)
            return r;
        int x = int(sqrt(2*sum));
        while(x>1)
        {
            vector<int> t;
            if(x%2==0 && sum%x == x/2)
            {
                int start = sum/x - x/2 + 1;
                int end = sum/x + x/2;
                for (int i=start; i<=end; i++)
                {
                    t.push_back(i);
                }
                r.push_back(t);
            }
            else if(x%2==1 && sum%x == 0)
            {
                int start = sum/x - x/2;
                int end = sum/x + x/2;
                for (int i=start; i<=end; i++)
                {
                    t.push_back(i);
                }
                r.push_back(t);
            }
            x--;
        }
        return r;
    }
};
