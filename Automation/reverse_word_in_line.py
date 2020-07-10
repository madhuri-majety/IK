"""
Reverse every string in a line

Input = "TCP is a layer 4 protocol"
Output = "PCT si a reyal 4 locotorp"
"""

def reverse_words_in_line(line):
    words = line.split()
    print(words)
    new_words = []
    for word in words:
        new_words.append(word[::-1])

    return(" ".join(new_words))


def main():
    line = "TCP is a layer 4 protocol"
    print(reverse_words_in_line(line))

if __name__ == '__main__':
    main()
