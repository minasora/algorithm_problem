class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while (j != len(nums) - 2):
            if nums[i] == nums[j]:
                nums[j] = nums[j + 1]
            i = i + 1
            j = j + 1
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                print(i)


solution = Solution()
solution.removeDuplicates()
