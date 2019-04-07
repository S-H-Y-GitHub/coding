class Solution {
public:
    int NumberOf1Between1AndN_Solution(int n)
    {
        int sum=0;
        for(int i=1; n>=i;i*=10)
        {
            sum+=i*(n/(10*i));
            if(n%(10*i)-i>=0)
                for(int j=0;j<i && j<=n%(10*i)-i;j++)
                    sum++;
        }
        return sum;
    }
};
