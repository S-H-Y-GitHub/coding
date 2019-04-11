class Solution {
public:
    int GetNumberOfK(vector<int> data ,int k) {
        int temp, l=data.size(), x=0, b=0;
        while(l>0 && b+l/2<data.size())
        {
            temp = data[l/2+b];
            if(temp == k)
            {
                for(int i=l/2+b; i>=0 && data[i]==k; i--)
                {
                    x++;
                }
                for(int i=l/2+b+1; i<data.size()&&data[i]==k; i++)
                {
                    x++;
                }
                break;
            }
            else if (temp < k)
            {
                b=b+l/2;
                l=l/2;
            }
            else
            {
                l=l/2;
            }
        }
        return x;
    }
};
