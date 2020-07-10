"""
Program to print BFS traversal from a given source vertex. BFS(int s) traverses vertices reachable from s.

Time Complexity = O(V+E)
"""

from collections import defaultdict

"""
This graph class represents a directed graph using 
adjacency list representation
"""
class Graph:
    # Define Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add edge
    def addEdge(self, start_vertex, end_vertex):
        self.graph[start_vertex].append(end_vertex)

    # Function to print BFS of a graph
    def BFS(self, s):
        # Mark all the vertices as not not visited
        visited = set()

        # Create a queue for BFS
        queue = []

        # Mark source node as visited and enqueue it
        queue.append(s)
        visited.add(s)

        while queue:
            # dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=' ')

            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)


g = Graph()
g.addEdge(5,1)
g.addEdge(5,2)
g.addEdge(1,2)
g.addEdge(2,5)
g.addEdge(2,3)
g.addEdge(3,3)

print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)



