from collections import deque
from copy import deepcopy

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0

        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        seen = set()

        alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        alphabet = alphabet.split()

        def getNeighbours(word):
            neighbours = []
            word = list(word)

            for i in range(len(word)):
                for j in range(len(alphabet)):
                    new_word = deepcopy(word)
                    new_word[i] = alphabet[j]
                    new_word = "".join(new_word)
                    if new_word not in seen and new_word in wordList:
                        neighbours.append(new_word)
            
            return neighbours

        queue = deque()
        queue.append( (beginWord, 1) )
        seen.add(beginWord)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for neighbour in getNeighbours(word):
                queue.append( (neighbour, steps + 1) )
                seen.add(neighbour)

        return 0