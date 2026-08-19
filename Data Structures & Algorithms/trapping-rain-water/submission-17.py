class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        while left < len(height) and height[left] == 0:
            left += 1

        right = left + 1
        max_water_going_right = 0

        while right < len(height):
            if height[right] >= height[left]:
                water = 0
                for i in range(left+1, right):
                    water += height[left] - height[i]
                max_water_going_right += water
                
                left = right
                right += 1
            
            else:
                right += 1

        # reverse
        right = len(height)-1
        while right > 0 and height[right] == 0:
            right -= 1

        left = right - 1
        max_water_going_left = 0

        while left >= 0:
            # print(left)
            # print(right)
            if height[left] > height[right]:
                water = 0
                for i in range(left+1, right):
                    water += height[right] - height[i]
                    # print(water)
                max_water_going_left += water
                
                right = left
                left -= 1
            
            else:
                left -= 1

        return max_water_going_right + max_water_going_left