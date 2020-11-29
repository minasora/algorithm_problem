class Solution:
    def intersection(self, nums1, nums2):
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        ans = []
        print(nums2)
        for i in nums1:
            l = 0
            r = len(nums2) - 1
            while l <= r:
                mid = int((l + r) / 2)
                print(mid)
                if nums2[mid] == i:
                    ans.append(i)
                    break
                elif nums2[mid] < i:
                    l = mid + 1
                else:
                    r = mid - 1
        return ans
solution = Solution()
print(solution.intersection([4,9,5],[9,4,9,8,4]))