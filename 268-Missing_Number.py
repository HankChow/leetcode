class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = sorted(nums)
		if nums[0] == 1:
			return 0
		for i in range(0, len(nums)):
			if nums[i] != i:
				return i
		return i + 1
