class Solution {
public:
    int FindGreatestSumOfSubArray(vector<int> array) {
        vector<int> max_array;
        int max = INT_MIN;
        if (array.empty())
            return max;
        max_array.push_back(array[0]);
        for(int i=1; i<array.size();i++)
        {
            if(max_array[i-1]>0)
                max_array.push_back(max_array[i-1]+array[i]);
            else
                max_array.push_back(array[i]);
            max=max<max_array[i]?max_array[i]:max;
        }
        return max;
    }
};
