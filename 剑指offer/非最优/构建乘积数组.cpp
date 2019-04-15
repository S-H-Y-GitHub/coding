class Solution {
public:
    vector<int> multiply(const vector<int>& A) {
        vector<int> b,c;
        for (int i=0; i<A.size()-1; i++)
        {
            if(b.empty())
                b.push_back(1);
            b.push_back(A[i] * *(b.end()-1));
        }
        for(int i=A.size()-1; i>0; i--)
        {
            if(c.empty())
                c.push_back(1);
            c.push_back(A[i] * *(c.end()-1));
        }
        for(int i=0; i<b.size(); i++)
        {
            b[i] = b[i] * c[c.size()-i-1];
        }
        return b;
    }
};
