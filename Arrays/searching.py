class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return l


# Take input
nums=[1,3,5,6]
target = 2

# Create object and call function
sol = Solution()
result = sol.searchInsert(nums, target)

# Print result
print("Index:", result)