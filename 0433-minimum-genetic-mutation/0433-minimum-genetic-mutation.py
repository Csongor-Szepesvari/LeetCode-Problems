class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        def distance(a, b):
            # this method will calculate the distance of two strings
            mutations = 0
            for (letter_a, letter_b) in zip(a, b):
                if letter_a != letter_b:
                    mutations += 1
            
            return mutations


        # Example:
        #   Input: start = "AACCGGTT", end = "AACCGGTA", bank = ['AACCGGTA'], output: 1

        # Idea: use a breadth first search
        # Use a dictionary:
        bank.append(startGene)
        gene_dictionary = {}
        

        for geneString in bank:
            
            # compare this geneString to all other geneStrings already contained as keys in the dictionary
            gene_strings = gene_dictionary.keys()

            # add it to the dictionary now as a key
            gene_dictionary[geneString] = []
            for pre_existing_string in gene_strings:
                if distance(geneString, pre_existing_string) == 1:
                    gene_dictionary[geneString].append(pre_existing_string)
                    gene_dictionary[pre_existing_string].append(geneString)

        # Now we will start from our startGene and execute a breadth first search with a deque
        # and use a set to track which ones we have visited
        from collections import deque
        q = deque()
        visited = set()

        q.append((startGene, 0))

        while q:
            # while the queue isn't empty we will keep adding to the end of it 
            # if the node we're looking at is unvisited
            node = q.popleft()
            geneString = node[0]
            visited.add(geneString)
            if geneString == endGene:
                return node[1]
            depth = node[1]
            possibleNextGenes = gene_dictionary[geneString]
            for string in possibleNextGenes:
                if string not in visited:
                    q.append((string,depth+1))
        
        return -1

    


                

        