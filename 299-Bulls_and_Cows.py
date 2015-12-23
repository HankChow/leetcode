class Solution(object):
	def getHint(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		g = guess
		a = secret
		length = len(a)
		bulls = 0
		cows = 0
		guess_checked = "0" * length
		answer_checked = "0" * length
		for i in range(0, length):
			if g[i] == a[i]:
				bull += 1
				guess_checked = guess_checked[:i] + "1" + guess_checked[(i+1):]
				answer_checked = answer_checked[:i] + "1" + answer_checked[(i+1):]
		for i in range(0, length):
			if guess_checked[i] == 0:
				for j in range(0, length):
					if answer_checked[j] == "0" and g[i] == a[j]:
						cows += 1
						answer_checked = answer_checked[:j] + "1" + answer_checked[(j+1):]
						guess_checked = guess_checked[:i] + "1" + guess_checked[(i+1):]
						break
		return str(bulls) + "A" + str(cows) + "B"
