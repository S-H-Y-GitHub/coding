class Solution {
public:
    int rectCover(int number) {
        int a1=1,a2=2;
        if(number<=2)
            return number;
        while (number > 2)
        {
            if(a1<a2)
                a1+=a2;
            else
                a2+=a1;
            number--;
        }
        return a1>a2?a1:a2;
    }
};
