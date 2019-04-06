class Solution {
public:
    bool IsPopOrder(vector<int> pushV,vector<int> popV) {
        auto p1 = popV.begin();
		auto p2 = p1;
		auto found = false;
		auto j = 0;
		vector<int> checked;

		while (p1!=popV.end())
		{
			for (int i = pushV.size() - 1; i >= 0; i--)
			{
                if (find(checked.begin(), checked.end(), i) != checked.end())
                {
                    found=true;
                    break;
                }
				if (pushV[i] == *p1)
				{
					found = true;
					checked.push_back(i);
				}
				if (found)
				{
					while (pushV[i] != *p2)
					{
						p2++;
						if (p2 == popV.end())
							return false;
					}
				}
			}
            if(!found)
                return false;
			p1++;
			p2 = p1;
			found = false;
		}
		return true;
    }
};
