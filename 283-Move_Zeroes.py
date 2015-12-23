class Solution(object):
	def movezeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void. Do not return anything, modify nums in-place instead.
		"""
		runnerIndex = 0
		chaserIndex = 0
		for runnerIndex in range(0, len(nums)):
			if num[runnerIndex] != 0:
				if runnerIndex != chaserIndex:
					nums[runnerIndex] = nums[chaserIndex]
					nums[runnerIndex] = 0
				chaserIndex += 1

