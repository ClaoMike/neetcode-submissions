class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        class MonotonicDeque:
            from collections import deque

            def __init__(self):
                self.dq = deque()
            
            def append(self, value, index, left):
                self.cleanFront(left)
                self.cleanBack(left)

                if self.isEmpty():
                    self.dq.appendleft((value, index))
                else:  
                    # replace duplicates if that is what I am adding
                    front_value, _ = self.dq[0]
                    if value == front_value:
                        while value == front_value:
                            self.dq.popleft()
                            if not self.isEmpty():
                                front_value, _ = self.dq[0]
                            else:
                                break
                        self.dq.appendleft((value, index))
                    # else if the value is strictly bigger just add it 
                    elif value > front_value:
                        self.dq.appendleft((value, index))
                    # otherwise, remove from the end until it is good to add
                    else:
                        end_value, _ = self.dq[-1]
                        while value > end_value:
                            self.dq.pop()
                            end_value, _ = self.dq[-1]
                        self.dq.append((value, index))

            def cleanFront(self, left):
                if not self.isEmpty():
                    _, front_index = self.dq[0]
                    while front_index < left:
                        self.dq.popleft()
                        if not self.isEmpty():
                            _, front_index = self.dq[0]
                        else:
                            break
                    
            def cleanBack(self, left):
                if not self.isEmpty():
                    _, front_index = self.dq[-1]
                    while front_index < left:
                        self.dq.pop()
                        if not self.isEmpty():
                            _, front_index = self.dq[-1]
                        else:
                            break
            
            def getMax(self, left):
                self.cleanFront(left)
                front_value, _ = self.dq[0]
                return front_value

            def isEmpty(self):
                return len(self.dq) == 0

            def print(self):
                print(self.dq)

        max_values = []
        mq = MonotonicDeque()
        for i in range(k):
            mq.append(nums[i], i, 0)
        max_values.append(mq.getMax(0))

        left = 1
        right = k
        while right < len(nums):
            mq.append(nums[right], right, left)
            max_val = mq.getMax(0)
            max_values.append(max_val)

            left += 1
            right += 1

        return max_values