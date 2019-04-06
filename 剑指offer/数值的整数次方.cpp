class Solution {
public:
    double Power(double base, int exponent) {
        vector<int> a;
        int flag = 0;
        double result = 1;
        if(exponent<0){
            exponent=-exponent;
            flag=1;
        }

        while(exponent>0)
        {
            if(exponent%2==0)
            {
                a.push_back(0);
                exponent /= 2;
            }
            else
            {
                a.push_back(1);
                exponent -= 1;
            }
        }
        for(int i=a.size()-1;i>=0;i--)
        {
            if(a[i] == 1)
                result*=base;
            else
                result*=result;
        }
        
        return flag?(1/result):result;
    }
};
