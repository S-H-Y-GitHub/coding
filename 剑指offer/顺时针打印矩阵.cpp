class Solution {
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        vector<int> result;
        if(matrix.size()==0)
            return result;
        int i = 0, j = 0, l=0,r=matrix[0].size(),t=0,b=matrix.size();
        bool flag = true, add = true;
        while(true)
        {
            if (l==r || t==b)
                return result;
            result.push_back(matrix[i][j]);
            if(flag && add)
            {
                if(j<r-1)
                    j++;
                else
                {
                    flag=false;
                    t++;
                    i++;
                }
            }
            else if (!flag && add){
                if(i<b-1)
                    i++;
                else
                {
                    flag=true;
                    add=false;
                    r--;
                    j--;
                }
            }
            else if (flag && !add){
                if(j>l)
                    j--;
                else
                {
                    flag=false;
                    b--;
                    i--;
                }
            }
            else if (!flag && !add){
                if(i>t)
                    i--;
                else
                {
                    flag=true;
                    add=true;
                    l++;
                    j++;
                }
            }
        }
    }
};
