class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        one, two = 0, 0

        for i in range(0, len(nums)-1):
            tmp = two
            two = max(one+nums[i], tmp)
            one = tmp

        res = two
        one, two = 0, 0

        for i in range(1, len(nums)):
            tmp = two
            two = max(one+nums[i], tmp)
            one = tmp

        return max(res, two)
