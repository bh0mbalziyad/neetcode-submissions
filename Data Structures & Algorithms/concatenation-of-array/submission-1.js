class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const ans = Array.from({length: nums.length}, (v, i) => 0)
        for(let i =  0; i < nums.length; i++) {
            ans[i] = nums[i]
            const target = i + nums.length
            ans[target] = nums[i]
        }
        return ans
    }
}
