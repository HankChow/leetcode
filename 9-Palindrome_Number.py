class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		s = str(x)
		ll = list(s)
		lr = list(s)
		lr.reverse()
		for i in range(0, len(s)):
			if ll[i] != lr[i]
				return False
		return True
