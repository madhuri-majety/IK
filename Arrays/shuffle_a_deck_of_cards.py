"""
Given an array, write a program to generate a random permutation of array elements.
This question is also asked as shuffle a deck of cards or randomize a given array.
Here shuffle means that every permutation of array element should equally likely.

The solution that this API should provide should follow an uniform distribution,
any solution that this API comes up with has to guarantee that it follows 1/N! Uniform distribution

shuffle-array

https://www.geeksforgeeks.org/shuffle-a-given-array/

Algorithm:
- Traverse from end to start
- pick random index from 0 to end
- swap the end index with randomly picked index
- Repeat until start of the array

"""

import random

def randamize(arr, n):
    for i in range(n-1,0,-1):
        #print(i)
        # Pick a random index from 0 to i
        j = random.randint(0,i)
        #print(j)

        # Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]

    return arr

def randamize_rec(arr, n):
    if n < 1:
        print("Recursive Shuffle a deck of cards:{}".format(arr))
        return
    else:
        #print(n)
        rand_idx = random.randint(0, n)
        #print(rand_idx)
        arr[n], arr[rand_idx] = arr[rand_idx], arr[n]
        randamize_rec(arr, n-1)



def main():
    arr = [1,2,3,4,5,6,7,8]
    n = len(arr)
    print("Iteration: Shuffle the deck of cards:{}".format(randamize(arr, n)))
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    randamize_rec(arr1, n-1)
    print("Recursion: Shuffle the deck of cards:{}".format(arr1))

if __name__ == '__main__':
    main()
