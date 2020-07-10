"""
https://www.geeksforgeeks.org/find-number-of-islands/

https://leetcode.com/problems/number-of-islands/solution/

"""
from collections import deque

class SolutionDFSLeetCode(object):
    """
    Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Depth First Search.
    During DFS, every visited node should be set as '0' to mark as visited node.
    Count the number of root nodes that trigger DFS, this number would be the number of islands since
    each DFS starting at some root identifies an island.

    Complexity Analysis

    Time complexity : O(M×N) where M is the number of rows and N is the number of columns.

    Space complexity : worst case O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.

    """
    def explore_dfs(self, grid, row, col):
        """
        This will explore all 4 directions in depth to find the island
        When visiting Grass, it will coverts Grass to Water to avoid
        the looping.
        :param grid:
        :param row:
        :param col:
        :return:
        """
        nr = len(grid)
        nc = len(grid[0])

        # Convert the current location to water
        grid[row][col] = 'W'

        # Explore all the way Up
        if row-1 > 0 and grid[row-1][col] == 'G':
            self.explore_dfs(grid, row-1, col)

        # Explore all the way down
        if row + 1 < nr and grid[row+1][col] == 'G':
            self.explore_dfs(grid, row+1, col)

        # Explore all the way to the left
        if col - 1> 0 and grid[row][col-1] == 'G':
            self.explore_dfs(grid, row, col-1)

        # Explore all the way to the right
        if col+1 < nc and grid[row][col+1] == 'G':
            self.explore_dfs(grid, row, col+1)


    def num_of_islands(self, grid):
        rows = len(grid)
        if not rows:
            return

        cols = len(grid[0])
        num_islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'G':
                    num_islands += 1
                    self.explore_dfs(grid,i,j)

        return num_islands

class SolutionDFSIK(object):
    def get_neighbors(self, curr_loc, nr, nc):
        r, c = curr_loc

        neighs = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

        def is_valid(x):
            return (x[0] >=0 and x[0] < nr and x[1] >= 0 and x[1] < nc)

        return list(filter(is_valid, neighs))

    def explore_islands(self, grid, curr_loc):
        nr = len(grid)
        nc = len(grid[0])

        row = curr_loc[0]
        col = curr_loc[1]

        grid[row][col] = 'W'

        for (i, j) in self.get_neighbors(curr_loc, nr, nc):
            if grid[i][j] == 'G':
                self.explore_islands(grid, (i,j))

    def count_islands(self, grid):
        nr = len(grid)

        if not nr:
            return 0
        nc = len(grid[0])

        count = 0

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 'G':
                    count += 1
                    self.explore_islands(grid, (i,j))

        return count

class SolutionDFSVisited():
    def get_neighbors(self, cur_loc, nr, nc):
        r = cur_loc[0]
        c = cur_loc[1]

        neighs = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

        def is_valid(x):
            return (x[0] >= 0 and x[0] < nr and x[1] >=0 and x[1] < nc)

        return list(filter(is_valid, neighs))

    def dfs(self, grid, visited, row, col):
        visited.add((row,col))

        for (i,j) in self.get_neighbors((row,col), len(grid), len(grid[0])):
            if (i,j) not in visited and grid[i][j] == 'G':
                self.dfs(grid, visited, i, j)


    def count_islands(self, grid):
        nr = len(grid)
        if not nr:
            return 0
        nc = len(grid[0])

        visited = set()
        count = 0

        for i in range(nr):
            for j in range(nc):
                if (i,j) not in visited and grid[i][j] == 'G':
                    count += 1
                    self.dfs(grid, visited, i, j)

        return count

class SolutionBFS(object):
    """
    * Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search.
    Put it into a queue and set its value as '0' to mark as visited node.
    Iteratively search the neighbors of enqueued nodes until the queue becomes empty.
    * Complexity Analysis
    * Time complexity : O(M×N) where M is the number of rows and N is the number of columns.
    * Space complexity : O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N).
    """
    def count_islands_bfs(self, grid):
        nr = len(grid)
        if not nr:
            return 0
        nc = len(grid[0])
        count = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 'G':
                    # Increment the count
                    count += 1

                    # Append it to Queue for exploring its neighbors
                    queue = deque()
                    queue.append((r,c))

                    # Mark as Visited
                    grid[r][c] = 'W'

                    # Explore the neigbors of a node
                    while queue:
                        row, col = queue.popleft()

                        # Check Up Neighbor
                        if row - 1 >= 0 and grid[row-1][col] == 'G':
                            queue.append((row-1, col))
                            grid[row-1][col] = 'W'

                        # Check Down Neighbor
                        if row + 1 < nr and grid[row+1][col] == 'G':
                            queue.append((row+1, col))
                            grid[row+1][col] = 'W'

                        # Check Left Neighbor
                        if col - 1 >= 0 and grid[row][col-1] == 'G':
                            queue.append((row, col-1))
                            grid[row][col-1] = 'W'

                        # Check Right Neighbor
                        if col + 1< nc and grid[row][col+1] == 'G':
                            queue.append((row, col+1))
                            grid[row][col+1] = 'W'

        return count

def main():
    grid = [['W','W','W','G','G','G'],
            ['G','W','W','W','W','W'],
            ['G','G','W','W','W','W'],
            ['W','W','G','G','W','W'],
            ['W','W','G','W','W','W']]

    print("Printing using DFS Leetcode way")
    sol1 = SolutionDFSLeetCode()
    print(sol1.num_of_islands(grid))

    grid1 = [['W','W','W','G','G','G'],
             ['G','W','W','W','W','W'],
             ['G','G','W','W','W','W'],
             ['W','W','G','G','W','W'],
             ['W','W','G','W','W','W']]

    print("Printing using DFS IK way")
    sol2 = SolutionDFSIK()
    print(sol2.count_islands(grid1))

    grid2 = [['W','W','W','G','G','G'],
             ['G','W','W','W','W','W'],
             ['G','G','W','W','W','W'],
             ['W','W','G','G','W','W'],
             ['W','W','G','W','W','W']]

    print("Printing using DFS Visited Set")
    sol3 = SolutionDFSVisited()
    print(sol3.count_islands(grid2))

    grid3 = [['W','W','W','G','G','G'],
             ['G','W','W','W','W','W'],
             ['G','G','W','W','W','W'],
             ['W','W','G','G','W','W'],
             ['W','W','G','W','W','W']]

    print("Printing using BFS")
    sol4 = SolutionBFS()
    print(sol4.count_islands_bfs(grid3))


if __name__ == '__main__':
    main()
