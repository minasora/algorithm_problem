class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        answer = [0 * i for i in range(len(nums))]
        answer[0] = nums[0]
        answer[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            answer[i] = max(answer[i - 2] + nums[i], answer[i - 1])
        return answer[-1]
