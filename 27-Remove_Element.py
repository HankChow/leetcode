class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		if len(nums) == 0:
			return 0
		i = 0
		j = len(nums) - 1
		while(i < j):
			if nums[i] == val:
				nums[i] = nums[j]
				j -= 1
			else:
				i += 1
		if nums[i] == val:
			return i
		return i + 1
