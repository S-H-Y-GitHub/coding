class Solution {
public:
    bool VerifySquenceOfBST(vector<int> s) {
        int mid=-1;
        if(s.empty())
            return false;
        int end = s[s.size()-1];
        for(int i=0; i<s.size()-1;i++)
        {
            if(s[i]<end)
                if(mid!=-1)
                    return false;
            if(s[i]>end)
                if(mid==-1)
                    mid=i;
        }
        if(mid==-1)
            return VerifySquenceOfBST2(vector<int>(s.begin(),s.end()-1));
        return VerifySquenceOfBST2(vector<int>(s.begin(),s.begin()+mid)) && VerifySquenceOfBST2(vector<int>(s.begin()+mid,s.end()-1));
    }
    bool VerifySquenceOfBST2(vector<int> s) {
        int mid=-1;
        if(s.empty())
            return true;
        int end = s[s.size()-1];
        for(int i=0; i<s.size()-1;i++)
        {
            if(s[i]<end)
                if(mid!=-1)
                    return false;
            if(s[i]>end)
                if(mid==-1)
                    mid=i;
        }
        if(mid==-1)
            return VerifySquenceOfBST2(vector<int>(s.begin(),s.end()-1));
        return VerifySquenceOfBST2(vector<int>(s.begin(),s.begin()+mid)) && VerifySquenceOfBST2(vector<int>(s.begin()+mid,s.end()-1));
    }
};
