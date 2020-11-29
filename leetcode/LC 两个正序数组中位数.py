class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        if len(nums) % 2 == 0:
            ans = nums[int(len(nums)/2)-1]+nums[int(len(nums)/2)]
            return ans/2
        else:
            return nums[int(len(nums)/2) ]