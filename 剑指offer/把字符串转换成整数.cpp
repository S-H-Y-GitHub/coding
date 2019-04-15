class Solution {
public:
    int StrToInt(string str) {
        int num = 0;
        if(str.size() == 0)
            return num;
        if(str.at(0) == '+')
        {
            for (int i=1; i<str.size(); i++)
            {
                if(str[i]>='0' && str[i]<='9')
                    num = num*10+ (str[i] - '0');
                else
                    return 0;
            }
        }
        else if(str.at(0) == '-')
        {
            for (int i=1; i<str.size(); i++)
            {
                if(str[i]>='0' && str[i]<='9')
                    num = num*10- (str[i] - '0');
                else
                    return 0;
            }
        }
        else
        {
            for (int i=0; i<str.size(); i++)
            {
                if(str[i]>='0' && str[i]<='9')
                    num = num*10+ (str[i] - '0');
                else
                    return 0;
            }
        }
        return num;
    }
};
