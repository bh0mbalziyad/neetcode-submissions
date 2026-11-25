class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        """
        When traversing heights add each one's height along with the index to which it can extend farthest to the right (since we start from the left)
        """

        maxArea = 0
        stack = [] # pair of elems (index,height)

        for i,h in enumerate(heights):
            start = i

            # When a height is found to be less than the one at the top of the stack
            while stack and stack[-1][1] > h:

                # pop the stack and use the popped index to increase the width of the current height by 1
                index, height = stack.pop()
                start = index

                # keep tracking maxArea when popping elements from stack
                maxArea = max(maxArea, height * (i - index))
            stack.append((start, h))
            
        for index, height in stack:
            maxArea =  max(maxArea, height * (len(heights) - index))
        
        return maxArea