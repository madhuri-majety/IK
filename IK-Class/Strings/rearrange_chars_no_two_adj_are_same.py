"""
Rearrange characters in a string such that no two adjacent are same
Given a string with repeated characters, the task is to rearrange characters in a string so that no two adjacent characters are same.

Note : It may be assumed that the string has only lowercase English alphabets.

Examples:

Input: aaabc
Output: abaca

Input: aaabb
Output: ababa

Input: aa
Output: Not Possible

Input: aaaabc
Output: Not Possible


Prerequisite : priority_queue.

The idea is to put the highest frequency character first (a greedy approach). We use a priority queue
(Or Binary Max Heap) and put all characters and ordered by their frequencies (highest frequency character at root).
We one by one take the highest frequency character from the heap and add it to result.
After we add, we decrease the frequency of the character and we temporarily move this character
out of priority queue so that it is not picked next time.

We have to follow the step to solve this problem, they are:
1. Build a Priority_queue or max_heap, pq that stores characters and their frequencies.
 Priority_queue or max_heap is built on the bases of the frequency of character.
2. Create a temporary Key that will be used as the previously visited element
3. While pq is not empty.
    Pop an element and add it to the result.
    Decrease frequency of the popped element by 1
    Push the previous element back into the priority_queue if its frequency > 0
    Make the current element as the previous element for the next iteration.
4. If the length of the resultant string and original, print not possible. Else print result.

https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/
"""

import heapq

def rearrange_chars_no_two_adj_same(txt):
    """
    Maintain a count map
    Main idea is to pick the characters in descending order of their frequency
    To do this we need to maintain a max heap with always giving us the element with max frequency
    pop the max element and store that character is result and reduce the frequency of the character in the count map
    If heap is not empty, Again pop next max element and store the character in result and reduce the frequency in the count map
    If the frequency of first popped element is > 0 then add it back to the heap
    If the frequency of second popped element is also > 0 then add it back to the heap.
    repeat until the heap is empty

    :param txt:
    :return:
    """
    n = len(txt)
    txt_chars = list(txt)
    result = []
    count_map = {}
    heap = []

    for char in txt_chars:
        if char not in count_map:
            count_map[char] = -1
        else:
            count_map[char] = -(abs(count_map[char])+1)

    print(count_map)

    for key,value in count_map.items():
        heapq.heappush(heap, (value,key))

    print(heap)

    while heap:
        cur_key = heapq.heappop(heap)[1]
        result.append(cur_key)
        count_map[cur_key] = -(abs(count_map[cur_key])-1)
        prev_key = cur_key

        if heap:
            cur_key = heapq.heappop(heap)[1]
            result.append(cur_key)
            count_map[cur_key] = -(abs(count_map[cur_key])-1)
            if abs(count_map[prev_key]) > 0:
                heapq.heappush(heap, (count_map[prev_key], prev_key))
            if abs(count_map[cur_key]) > 0:
                heapq.heappush(heap, (count_map[cur_key], cur_key))

        else:
            break

    if n != len(result):
        print("Not possible to rearrange")
    else:
        print("".join(result))




def main():
    rearrange_chars_no_two_adj_same("aaabc")
    rearrange_chars_no_two_adj_same("aa")
    rearrange_chars_no_two_adj_same("aaabb")
    rearrange_chars_no_two_adj_same("aaabbb")
    rearrange_chars_no_two_adj_same("aaaabc")
    rearrange_chars_no_two_adj_same("bbbaa")


if __name__ == '__main__':
    main()
