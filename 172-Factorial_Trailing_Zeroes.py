class Solution(object):
	def trailingZeroes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		ret = n / 10
		if n % 10 >= 5:
			ret = ret * 2 + 1
		else:
			ret *= 2
		for i in range(2, 15):
			ret += n / (5 ** i)
		return ret
