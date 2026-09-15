class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in range(len(nums)):
            val = nums[i]
            count = 0

            for j in range(len(nums)):
                if val > nums[j]:
                    count += 1
            result.append(count)
        return result