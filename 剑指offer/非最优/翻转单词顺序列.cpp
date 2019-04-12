class Solution {
public:
    string ReverseSentence(string str) {
        string s;
        int j = 0;
        
        for(int i=str.size()-1; i>=0; i--)
        {
            char ch = str[i];
            
            if(ch==' ')
            {
                j = s.size();
                s.insert(s.begin()+j, ch);
                j++;
            }
            else
                s.insert(s.begin()+j, ch);
            
        }
        return s;
    }
};
