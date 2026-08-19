class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(i, j):
            return (j - i) * min(heights[i], heights[j])

        max_area = 0
        left = 0
        right = len(heights) -1

        while left < right:
            current_area = area(left, right)
            if current_area > max_area:
                max_area = current_area
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return max_area
