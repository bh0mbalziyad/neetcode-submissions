class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # if majority element always exists
        # it implies that the element takes up more than half the slots
        # in the given array. which means if we sort the array
        # the majority element will appear in the middle of the
        # sorted array

        nums = sorted(nums)
        return nums[len(nums)//2]
        