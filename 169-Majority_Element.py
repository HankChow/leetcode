class Solution(object):
	def majorityEement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		return sorted(nums)[len(nums)/2]
