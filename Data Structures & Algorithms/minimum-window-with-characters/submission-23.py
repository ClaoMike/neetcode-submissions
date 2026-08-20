class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best = ""
        minimun_length = 0

        #  if t is bigger than s, exit
        if len(t) > len(s):
            return best
        
        class Window:
            def __init__(self, s, t):
                self.s = s
                self.t = t

                self.best = ""
                self.minimum_length = float('inf')

                self.left = 0
                self.right = 0

                from collections import defaultdict
                self.t_frequency = defaultdict(int)
                self.t_permutations = defaultdict(int)
                for c in self.t:
                    self.t_permutations[c] += 1
            
            def expand_until_valid(self):
                while self.right < len(self.s):
                    if self.s[self.right] in self.t_permutations:
                        self.t_frequency[self.s[self.right]] += 1

                    if self.is_valid():
                        self.save_window()
                        break

                    self.right += 1

            def squeeze(self):
                while self.left < len(self.s) and ( 
                    self.s[self.left] not in self.t_permutations or ( 
                        s[self.left] in self.t_permutations and self.t_frequency[self.s[self.left]] - 1 >= self.t_permutations[self.s[self.left]] 
                        ) 
                        ):
                    if self.s[self.left] in self.t_permutations:
                        self.t_frequency[self.s[self.left]] -= 1
                    self.left += 1
                self.save_window()

            # def expand_until_valid_again(self):
            #     if self.left < len(s) and self.s[self.left] in self.t_permutations:
            #         self.t_frequency[self.s[self.left]] -= 1
            #     self.left += 1

            #     while self.right < len(self.s):
            #         self.right += 1

            #         if self.right < len(s) and self.s[self.right] in self.t_permutations:
            #             self.t_frequency[self.s[self.right]] += 1

            #         if self.is_valid():
            #             self.save_window()
            #             break
            
            # def find_best(self):
            #     self.expand_until_valid()
            #     self.squeeze()

            #     while self.right < len(self.s):
            #         self.expand_until_valid_again()
            #         self.squeeze()
            #         self.print_current_state()

            def expand_until_valid_again(self):
                if self.left < len(self.s) and self.s[self.left] in self.t_permutations:
                    self.t_frequency[self.s[self.left]] -= 1
                self.left += 1

                while self.right < len(self.s) - 1:
                    self.right += 1
                    if self.s[self.right] in self.t_permutations:
                        self.t_frequency[self.s[self.right]] += 1
                    if self.is_valid():
                        self.save_window()
                        return True
                return False

            def find_best(self):
                self.expand_until_valid()

                if not self.is_valid():
                    return

                self.squeeze()

                while self.right < len(self.s):
                    if not self.expand_until_valid_again():
                        break
                    self.squeeze()

            def save_window(self):
                current = self.s[self.left:self.right+1]
                current_length = len(current)
                if current_length < self.minimum_length:
                    self.minimum_length = current_length
                    self.best = current

            def print_current_state(self):
                print(f"Left: {self.left}")
                print(f"Right: {self.right}")
                print(f"Current: {self.s[self.left:self.right+1]}")
                print(f"Best: {self.best}")

            def is_valid(self):
                if len(self.t_permutations) != len(self.t_frequency):
                    return False

                for character, freq in self.t_permutations.items():
                    if freq > self.t_frequency[character]:
                        return False
                return True

        window = Window(s, t)
        window.find_best()

        return window.best