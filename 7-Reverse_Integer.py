class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		isMinus = False
		if x < 0:
			isMinus = True
		x = abs(x)
		ret = 0
		while x > 0:
			ret += x % 10
			x /= 10
			if x > 0:
				ret *= 10
		if ret > 2 ** 31:
			return 0
		return ret if isMinus else ret
