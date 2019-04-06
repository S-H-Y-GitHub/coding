class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
        if (rotateArray.empty())
            return 0;
        
        else if(rotateArray.size()==1)
            return rotateArray[0];
        else if(rotateArray.size()==2)
            return rotateArray[0]<rotateArray[1]?rotateArray[0]:rotateArray[1];
        else
        {
            int i=rotateArray.size()/2;
            if(rotateArray[i]<*(rotateArray.end()-1))
                return minNumberInRotateArray(vector<int>(rotateArray.begin(), rotateArray.begin()+i+1));
            else
                return minNumberInRotateArray(vector<int>(rotateArray.begin()+i+1, rotateArray.end()));
        }
    }
};
