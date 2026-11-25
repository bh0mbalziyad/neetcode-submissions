class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, val in enumerate(nums):
            val = nums[idx]
            hashmap[val] = idx

        for idx, val in enumerate(nums):
            complement = target - val
            if complement in hashmap and idx != hashmap[complement]:
                return [idx, hashmap[complement]]

        return []