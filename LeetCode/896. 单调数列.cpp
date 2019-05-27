class Solution {
public:
    bool isMonotonic(vector<int>& A) {
      int up = 0;
      for(int i=0; i<A.size()-1; i++)
      {
        if (A[i]<A[i+1] && up!=2)
        {
          up=1;
          continue;
        }
        else if (A[i]>A[i+1] && up!=1)
        {
          up=2;
          continue;
        }
        else if (A[i]==A[i+1])
        {
          continue;
        }
        else
        {
          return false;
        }
      }
      return true;
    }
};
