class Solution(object):
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		ret = 0
		for i in range(0, len(s)):
			tmp = 1
			for j in range(i, len(s)-1):
				tmp *= 26
			ret += (ord(s[i]) - 64) * tmp
		return ret
