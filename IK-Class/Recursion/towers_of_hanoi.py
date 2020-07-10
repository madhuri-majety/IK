"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.

https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

The pattern here is :
Shift 'n-1' disks from 'A' to 'B'.
Shift last disk from 'A' to 'C'.
Shift 'n-1' disks from 'B' to 'C'.

******** For n disks, total 2n – 1 moves are required. ******


"""

def tower_of_hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        print("Move disk 1 from {} to {}".format(from_peg, to_peg))
    else:
        tower_of_hanoi(n-1, from_peg, aux_peg, to_peg)
        print("Move disk {} from {} to {}".format(n, from_peg, to_peg))
        tower_of_hanoi(n-1, aux_peg, to_peg, from_peg)


def main():
    n = 3
    tower_of_hanoi(n, "A", "B", "C")

if __name__ == '__main__':
    main()
