class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = sorted(nums)
		for i in range(0, (len(nums)-1)/2):
			if nums[i*2] != nums[i*2+1]:
				return nums[i*2]
		return nums[len(nums)-1]
