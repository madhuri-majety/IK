"""
Sort an array of characters

Input: An string of characters, like a full english sentence, delimited by newline or NULL. Duplicates are okay
Output: A string of characters, in sorted order if their ASCII values. you can overwrite the exisiting array.

Aim for linear time and constant additional space
"""
import random
import time

def sort_characters(input_str):
    if not input_str or len(input_str) == 1:
        return input_str
    in_arr = list(input_str)
    out_arr = [0] * 256
    for c in in_arr:
        out_arr[ord(c)] += 1

    ctr = 0
    for idx, val in enumerate(out_arr):
        if val == 0:
            continue
        for count in range(val):
            in_arr[ctr+count] = chr(idx)
        ctr += val

    return ''.join(in_arr)

def sort_characters_qs(input_str):
    in_arr = bytearray(input_str.encode())
    quick_sort(in_arr, 0, len(in_arr)-1)
    return bytes(in_arr)

def quick_sort(input, st, end):
    if st < end:
        pivot = partition(input, st, end)
        quick_sort(input, st, pivot -1)
        quick_sort(input, pivot+1, end)

def partition(input, st, end):
    idx = random.randint(st, end)
    input[idx], input[end] = input[end], input[idx]

    pivot = input[end]
    pindex = st

    for i in range(st, end):
        if input[i] <= pivot:
            input[i], input[pindex] = input[pindex], input[i]
            pindex += 1

    input[pindex], input[end] = input[end], input[pindex]

    return pindex


def main():
    start_time = time.time()
    print(sort_characters("This is easy"))
    print("Elapsed time is : {}".format(time.time() - start_time))

    start_time = time.time()
    print(sort_characters_qs("This is easy"))
    print("Elapsed time is : {}".format(time.time() - start_time))

if __name__ == '__main__':
    main()