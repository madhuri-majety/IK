"""

Company: Juniper Networks



You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in a group. And the group of two or more people wants to meet and minimize the total travel distance. They can meet anywhere means that there might be a home or not.

    The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x – p1.x| + |p2.y – p1.y|.
    Find the total distance that needs to be traveled to reach the best meeting point (Total distance traveled is minimum).

Steps :-
1) Store all horizontal and vertical positions of all group member.
2) Now sort it to find minimum middle position, which will be the best meeting point.
3) Find the distance of all members from best meeting point.

https://www.geeksforgeeks.org/best-meeting-point-2d-binary-array/

"""

def best_meeting_point(grid, nrows, ncols):
    """
    TC = O(M*N)
    SC = O(N)
    :param grid:
    :param nrows:
    :param ncols:
    :return:
    """
    if nrows == 0 or ncols == 0:
        return 0

    vertical = []
    horizontal = []

    # Step1 : Find all members home positions and update the lists
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 1:
                vertical.append(i)
                horizontal.append(j)

    # Step 2: sort positions so we can find most beneficial point
    vertical.sort()
    horizontal.sort()

    # Step 3: middle position will always be beneficial for all group members but if it is sorted lsit
    middle = len(vertical)//2

    x = vertical[middle]
    y = horizontal[middle]

    # Step 4: Find total distance from best meeting point (x,y) from all members
    distance = 0
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 1:
                distance += abs(x-i) + abs(y-j)

    return distance


if __name__ == '__main__':
    grid = [[1,0,1,0,1], [0,1,0,0,0], [0,1,1,0,0]]
    print(best_meeting_point(grid, len(grid), len(grid[0])))

    grid1 = [[1,0,0,0,1], [0,0,0,0,0], [0,0,1,0,0]]
    print(best_meeting_point(grid1, len(grid1), len(grid1[0])))
