class Solution {
public:
	void replaceSpace(char *str,int length) {
        int blank_count = 0;
        for(int i=0; i<length; i++)
        {
            if (str[i] == ' ')
                blank_count++;
        }
        for(int i=length; i>=0; i--)
        {
            if (str[i] == ' ')
            {
                
                str[i+blank_count*2] = '0';
                str[i+blank_count*2 - 1] = '2';
                str[i+blank_count*2 - 2] = '%';
                blank_count--;
            }
            else
                str[i+blank_count*2] = str[i];
        }
	}
};
