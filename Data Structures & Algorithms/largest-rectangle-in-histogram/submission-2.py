class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # calculate the area of each horizontal and vertical rectangle possible
        # pick the biggest one

        # vertical rectangle -> height > width
        # horizontal rectangle -> width > height

        # for each i, check right and left till we find heights[right,left] < heights[i]
        # that's a horizontal rectangle

        # areas = []
        
        # This is like O(n^2), not good

        # for i in range(len(heights)):
        #     height = heights[i]
        #     width = 1
        #     for left in range(i-1,-1,-1):
        #         if heights[left] < height:
        #             break
        #         width += 1
        #     for right in range(i+1,len(heights)):
        #         if heights[right] < height:
        #             break
        #         width += 1
        #     areas.append(width * height)
        
        # max_area = 0
        # for area in areas:
        #     max_area = max(max_area, area)
        # for area in heights:
        #     max_area = max(max_area, area)

        # we need a way to find horizontal areas faster
        increasing_stack = [] # array of (height, start_idx)
        max_area = 0
        for i in range(len(heights)):
            start = i
            while increasing_stack and increasing_stack[-1][0] > heights[i]:
                width = i - increasing_stack[-1][1]
                max_area = max(max_area,increasing_stack[-1][0] * width)
                start = increasing_stack[-1][1]
                increasing_stack.pop()

            increasing_stack.append((heights[i],start))
        
        while increasing_stack:
            width = len(heights) - increasing_stack[-1][1]
            max_area = max(max_area,increasing_stack[-1][0] * width)
            increasing_stack.pop()

        return max_area

            