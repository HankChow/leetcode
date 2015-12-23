class Solution(object):
	def bulbSwitch(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		i = 1
		while i ** 2 <= n:
			i += 1
		return i - 1
