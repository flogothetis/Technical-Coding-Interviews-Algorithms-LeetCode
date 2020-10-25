def atMostNGivenDigitSet( D, N):
	s = str(N)
	n = len(s)

	# Count all different combinations with digits K-1
	ans = 0
	for i in range(1, n):
		ans += len(D) ** i

	for i in range (n):
		prefix = False
		for d in D:
			if(d < s[i]):
				ans += len(D) ** (n - i - 1)
			elif ( d == s[i]):
				prefix = True
				break;
		if prefix is False:
			return ans
	return  ans + 1




digits = ["1","3","5","7"]
n = 100
print(atMostNGivenDigitSet(digits, n))