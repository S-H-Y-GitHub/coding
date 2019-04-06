class Solution {
public:
    int Fibonacci(int n) {
        if(n==0)
            return 0;
        int a=0,b=1;
        for(int i=1; i<n; i++)
        {
            if(a<b)
                a=a+b;
            else
                b=a+b;
        }
        return a<b?b:a;
    }
};
