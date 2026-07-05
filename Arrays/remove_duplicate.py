class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
list1 = [4,45,67,78,78,90,90,123,456,789,789]
s = Solution()
k = s.removeDuplicates(list1)
print(k)
print(list1[:k])