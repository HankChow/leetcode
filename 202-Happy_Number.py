class Solution(object):
	def isHadppy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		for i in range(0, 10):
			n = self.sumsqr(n)
			if n == 1;
				return True
		return False

	def sumsqr(self, n):
		if n == 1:
			return n
		ret = 0
		while n >= 1:
			ret += (n % 10) ** 2
			n = (n - (n % 10)) / 10
		return ret
