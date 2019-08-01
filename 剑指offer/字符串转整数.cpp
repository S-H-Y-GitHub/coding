int convert_to_int(string s)
{
	auto is_neg = false;
	auto i = s.size()-1;
	long long result = 0;
	unsigned long long e = 1;
	
	for (; i > 0; i--)
	{
		if (s[i] - '0' < 10 && s[i] - '0' >= 0)
		{
			
			result += (s[i] - '0') * e;
			if (result > INT_MAX)
				return -1;
			e *= 10;
		}
		else
		{
			return -1;
		}
	}
	if (s[0] == '-')
	{
		result = -result;
		if (result < INT_MIN)
			return -1;
	}
	else if (s[0] <= '9' and s[0] >= '0')
	{
		result += (s[0] - '0') * e;
		if (result > INT_MAX)
			return -1;
	}
	else if (s[0] != '+')
	{
		return -1;
	}
	return result;
}
