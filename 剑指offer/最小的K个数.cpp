class Solution {
public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        if(k<=0)
            return vector<int>();
        if(k>input.size())
            return vector<int>();
        int a;
        vector<int> s1,s2;
        while(true)
        {
            a=input[input.size()-1];
            for(auto i : input)
            {
                if(i<=a)
                    s1.push_back(i);
                else
                    s2.push_back(i);
            }
            if(s1.size()<k)
            {
                input=s2;
            }
            else if(s1.size()>k)
            {
                input=s1;
                s1.clear();
                s2.clear();
                input.pop_back();
            }
            else
                return s1;
        }
    }
};
