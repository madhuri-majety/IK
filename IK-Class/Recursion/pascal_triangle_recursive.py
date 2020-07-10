#! /usr/bin/python3

def pascal(lines):
    if lines == 1:
        print("[1]".center(80))
        return [1]
    else:
        cur_line = [1]
        prev_line = pascal(lines-1)
        for x in range(len(prev_line)-1):
            cur_line.append(prev_line[x] + prev_line[x+1])
        cur_line += [1]
        print(str(cur_line).center(80))
        #print(cur_line)
    return cur_line

def pascal_lcomp(lines):
    if lines == 1:
        print("[1]".center(80))
        return [1]
    else:
        prev_line = pascal_lcomp(lines-1)
        cur_line = [prev_line[i+1] + prev_line[i] for i in range(len(prev_line)-1)]
        cur_line.insert(0,1)
        cur_line.append(1)
        print(str(cur_line).center(80))
    return cur_line

lines = input("Enter number of lines for pascal triangle:")
pascal_lcomp(int(lines))
pascal(int(lines))

