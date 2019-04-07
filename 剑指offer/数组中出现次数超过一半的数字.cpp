class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers) {
        if(numbers.empty())
            return 0;
        int num,count=0;
        for(auto i : numbers)
        {
            if(count==0||i==num)
            {
                num=i;
                count++;
            }
            else
            {
                count--;
            }
        }
        if(count>0)
        {
            count=0;
            for(auto i : numbers)
            {
                if(i==num)
                    count++;
            }
        }
        if(count>numbers.size()/2)
            return num;
        else
            return 0;
    }
};
