class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums:List[int]
		:rtype:List[int]
		"""
		n = len(nums)
		if n < 2:
			return nums
		res = list(nums)
		# transform nums such that nums[i] = nums[1] x nums[2] x ... x nums[i-1]
		nums[0] = 1
		for i in range(1, n):
			nums[i] = nums[i-1] * res[i-1]
		# transform res such that res[i] = res[i] = res[i+1] x res[i+2] x ... x res[n-1]
		tmp = res[-1]
		res[-1] = 1
		for i in reversed(range(0, n - 1)):
			res[i], tmp = tmp * res[i+1], res[i]
		# transform res such that res[i] = res[1] x res[2] x ... x res[i-1] x res[i+1] x ... x res[n-1]
		for i in range(1, n):
			res[i] *= nums[i]
		return res
