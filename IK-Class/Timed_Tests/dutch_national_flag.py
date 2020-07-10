"""
Dutch National flag:
Given balls of 3 colros (Red, Green, Bluw) arranged randomly in  a line.
Arrange them as Red, Green, Blue
"""

def partition(word):
    a = list(word)
    #for i in range(len(word)):
        #a.append(word[i])

    print(a)
    i, red, blue = 0, 0, len(a)-1

    while i <= blue:
        if a[i] == 'r' or  a[i] == 'R':
            a[i], a[red] = a[red], a[i]
            i += 1
            red += 1
        elif a[i] == 'b' or a[i] == 'B':
            a[i], a[blue] = a[blue], a[i]
            #i += 1
            blue -= 1
        else:
            i += 1

    balls = "".join(a)
    return balls

def main():
    word = "RBRBBGGBBRBR"
    print("After sorting:", partition(word))



if __name__ == '__main__':
    main()

