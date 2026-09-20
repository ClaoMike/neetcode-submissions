class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def walls_left():
            walls = []
            stack = []
            for i in range(len(heights)):

                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                
                top = stack[-1] if stack else None
                stack.append(i)
                walls.append(top if top is not None else -1)

            return walls

        def walls_right():
            walls = []
            stack = []
            for i in reversed(range(len(heights))):

                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                
                top = stack[-1] if stack else None
                stack.append(i)
                walls.append(top if top is not None else len(heights))
            
            walls.reverse()

            return walls

        max_area = 0
        left_walls = walls_left()
        right_walls = walls_right()

        for i in range(len(heights)):
            curr_area = heights[i] * (right_walls[i] - left_walls[i] - 1)
            max_area = curr_area if curr_area > max_area else max_area

        return max_area