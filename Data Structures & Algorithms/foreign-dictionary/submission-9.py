from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        alphabet = set()
        graph = defaultdict(set)

        def findUnorderedAlphabet():
            for word in words:
                for letter in word:
                    alphabet.add(letter)

        def stringToQueue(s):
            return deque(list(s))

        def setUpGraphInitalState():
            for letter in alphabet:
                graph[letter] = set()
        
        def buildGraph():
            for i in range(len(words) - 1):
                j = i + 1

                word1 = stringToQueue(words[i])
                word2 = stringToQueue(words[j])

                while word1 and word2 and word1[0] == word2[0]:
                    word1.popleft()
                    word2.popleft()

                if not word2 and word1:
                    return False
                
                if word1:
                    graph[word1[0]].add(word2[0])

            return True
        
        def setUpIndegree():
            indegree = defaultdict(int)

            for key, values in graph.items():
                indegree[key] += 0
                for value in values:
                    indegree[value] += 1

            return indegree

        def setUpQueue(indegree):
            queue = deque()

            for key, i in indegree.items():
                if i == 0:
                    queue.append(key)
            
            return queue

        def topologicalSort(queue, indegree):
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

        findUnorderedAlphabet()
        setUpGraphInitalState()

        if not buildGraph():
            return ""

        indegree = setUpIndegree()
        
        return topologicalSort(setUpQueue(indegree), indegree)