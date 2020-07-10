"""
Program to print DFS Traversal for complete graph
TC = O(V+E)

"""

from collections import defaultdict

"""
This graph class represents a directed graph using 
adjacency list
"""

class Graph:
    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add edge to the graph
    def addEdge(self, start_vertex, end_vertex):
        self.graph[start_vertex].append(end_vertex)
        #print(self.graph)

    def printGraph(self):
        print(self.graph)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v)
        for i in self.graph[v]:
            if i not in visited:
                self.DFSUtil(i, visited)



    # The function to do DFS traversal using recursion
    def DFS(self):
        # Create a empty visited set.
        visited = set()
        for i in self.graph.keys():
            print("Visiting : {}".format(i))
            if i not in visited:
                self.DFSUtil(i, visited)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(5, 1)
g.addEdge(5, 2)
g.addEdge(1, 2)
g.addEdge(2, 5)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.printGraph()

print("Following is Depth First Traversal")
g.DFS()
