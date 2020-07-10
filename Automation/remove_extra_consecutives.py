"""
Write a function that takes two parameters, a string and an integer.
The function will return another string that is similar to the input string, but with certain characters removed.
 It's going to remove characters from consecutive runs of the same character,
 where the length of the run is greater than the input parameter.
"""

def remove_extra_consecutives(inp_str, max_occurences):
    prev_char = None
    count = 0
    output = []

    for cur_char in inp_str:
        if cur_char != prev_char:
            prev_char = cur_char
            count = 0
        else:
            count += 1

        if count < max_occurences:
            output.append(cur_char)

    return "".join(output)

def main():
    print(remove_extra_consecutives("aaabaabbb", 2))
    print(remove_extra_consecutives("aaabaabbb", 1))

if __name__ == '__main__':
    main()

