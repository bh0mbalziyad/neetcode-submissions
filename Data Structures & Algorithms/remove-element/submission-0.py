# (1) Brute Force

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
# Track all non-matching items
#         tmp = []

#         for num in nums:
#             if num == val:
#                 continue
#             tmp.append(num)
#
# modify the array in-place
#         for i in range(len(tmp)):
#             nums[i] = tmp[i]
#         return len(tmp)
        
# (2) Two Pointers - I

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # track position of where to store non-matching number
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # store non-matching number at pointer then increment pointer
                nums[k] = nums[i]
                k += 1
        # return number of non-matching items
        return k