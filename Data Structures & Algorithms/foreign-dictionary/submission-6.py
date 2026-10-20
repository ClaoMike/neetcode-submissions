from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        alphabet = set()
        for word in words:
            for letter in word:
                alphabet.add(letter)

        graph = defaultdict(set)

        for i in range(len(words) - 1):
            j = i + 1

            word1 = deque(list(words[i]))
            word2 = deque(list(words[j]))

            while word1 and word2 and word1[0] == word2[0]:
                word1.popleft()
                letter = word2.popleft()

                if letter not in graph.keys():
                    graph[letter] = set()

            if not word2 and word1:
                return ""
            
            if word1:
                graph[word1[0]].add(word2[0])
            
            while word1:
                if word1[0] not in graph.keys():
                    graph[word1[0]] = set()
                word1.popleft()
            
            while word2:
                if word2[0] not in graph.keys():
                    graph[word2[0]] = set()
                word2.popleft()
        
        indegree = defaultdict(int)

        for key, values in graph.items():
            indegree[key] += 0
            for value in values:
                indegree[value] += 1

        queue = deque()
        for key, i in indegree.items():
            if i == 0:
                queue.append(key)

        result = []
        while queue:
            letter = queue.popleft()
            result.append(letter)

            for neighbour in graph[letter]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if len(result) != len(alphabet):
            return ""

        return "".join(result)