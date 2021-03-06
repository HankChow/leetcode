class Solution(object):
	def intToRoman(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		roman = [["0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"], ["0", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"], ["0", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"], ["0", "M", "MM", "MMM"]]
		ret = ""
		if num / 1000 != 0:
			ret += roman[3][num/1000]
		if (num % 1000) / 100 != 0:
			ret += roman[2][(num % 1000) / 100]
		if (num % 100) / 10 != 0:
			ret += roman[1][(num % 100) / 10]
		if num % 10 != 0:
			ret +=roman[0][num % 10]
		return ret
