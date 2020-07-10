"""
Given an input as sequence of pass and fail status find the longest failed sequence
input = ['p','f','f','p','p','p','f','f','f','f','p']
output = 4
"""

def find_longest_failed_sequence_stack(seq):
    """
    Use stack method to find the max sequence
    Time Complexity = O(N+K)
    Space Complexity = O(K) where K is longest failed sequence
    :param seq:
    :return:
    """
    stack = []
    i = 0
    max = 0

    while (i < len(seq)):
        if seq[i] == 'f':
            stack.append(i)
        elif stack:
            top = stack.pop()
            last = 0
            while stack:
                last = stack.pop()
            print(last)
            if last:
                cur_max = top - last + 1
            else:
                cur_max = top - last

            if cur_max > max:
                max = cur_max

        i += 1

    if stack:
        top = stack.pop()
        last = 0
        while stack:
            last = stack.pop()

        if last:
            cur_max = top - last + 1
        else:
            cur_max = top - last

        if cur_max > max:
            max = cur_max


    print("Length of longest failed sequence is : {}".format(max))


def find_longest_failed_sequence_opt(seq):
    """
    Just look into prev and cur value and update the count
    Time Complexity = O(N)
    Space Complexity = O(1)
    :param seq:
    :return:
    """
    max = 0
    count = 0
    for i in range(1, len(seq)):
        if seq[i] == 'f' and seq[i-1] == 'f':
            count += 1

        else:
            if count+1 > max:
                max = count

            count = 0

    if count+1 > max:
        max = count+1

    print("Using Optimal way, longest failed sequence is {}".format(max))

def main():
    #input = ['p','f','f','p','p','p','f','f','f','f','f']
    input = ['p', 'f', 'p']
    find_longest_failed_sequence_stack(input)
    find_longest_failed_sequence_opt(input)

if __name__ == '__main__':
    main()
