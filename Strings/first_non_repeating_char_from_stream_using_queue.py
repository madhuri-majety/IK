"""

Queue based approach for first non-repeating character in a stream

Given a stream of characters and we have to find first non repeating character each time a character is inserted to the stream.

Examples:

Input  : a a b c
Output : a -1 b b

Input  : a a c
Output : a -1 c

https://www.geeksforgeeks.org/queue-based-approach-for-first-non-repeating-character-in-a-stream/

Approach-

Create a count array of size 26(assuming only lower case characters are present) and initialize it with zero.
Create a queue of char datatype.
Store each character in queue and increase its frequency in the hash array.
For every character of stream, we check front of the queue.
If the frequency of character at the front of queue is one, then that will be the first non repeating character.
Else if frequency is more than 1, then we pop that element.
If queue became empty that means there are no non repeating character so we will print -1.

"""

from collections import deque

MAX_CHARS = 26

def find_first_non_repeating_char_using_queue(stream):
    """
    Time Complexity : O(NK) where K is the number of unique chars
    Space Complexity: O(K) # frequency list is constant
    :param stream:
    :return:
    """
    queue = deque()
    char_count = [0] * MAX_CHARS

    #Traverse the stream
    for i in range(len(stream)):
        # Push each character in queue
        queue.append(stream[i])

        # Increament the frequency count
        char_count[ord(stream[i]) - ord('a')] += 1

        # Check for non-repeating character for every character read from stream
        while queue:
            if char_count[ord(queue[0]) - ord('a')] > 1:
                queue.popleft()
            else:
                print(queue[0], end = ' ')
                break

        if not queue:
            print(-1, end=" ")
    print()

def main():
    find_first_non_repeating_char_using_queue("aabc")
    find_first_non_repeating_char_using_queue("GeeksforGeeks")

if __name__ == '__main__':
    main()

