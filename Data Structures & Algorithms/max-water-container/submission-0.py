class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # this feels similar to largest rectangle in histogram somewhat
        # that was solved using a monotonic stack

        # basically we want to find biggest area possible
        # area = width * height 
        # width is index difference
        # height is min height of the two indices that form the container

        # naive solution would be nested loop over all heights
        # that's O(n^2)
        # maxArea = 0
        # for i in range(len(heights)-1):
        #     for j in range(i+1, len(heights)):
        #         h = min(heights[i],heights[j])
        #         w = j-i
        #         maxArea = max(maxArea, w*h)
        

        maxArea = 0
        left, right = 0, len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            maxArea = max(maxArea,width * height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                

        return maxArea