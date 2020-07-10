"""
Create Pascals triangle
1
1 1
1 2 1
1 3 3 1

F(PascalTriangleArray) = ((1*1 + 1) + (2*1 + 1) + (2*1 + 2) + (3*1 + 1) + (3*2 + 2) + (3*1 + 3) + (4*1 + 1) + (4*3 + 2)
+ (4*3 + 3) + (4*1 + 4)) % (10^9 + 7) = 69

Return F(PascalTriangleArray)

https://www.geeksforgeeks.org/pascal-triangle/


"""

def get_pascal_traingle_array(n):
    result = []
    for line in range(n):
        cur_line = [1]
        if line == 0:
            result.append(cur_line)
        else:
            prev_line = result[line-1]
            for i in range(len(prev_line)-1):
                cur_line.append(prev_line[i] + prev_line[i+1])
            cur_line.append(1)
            result.append(cur_line)

    return result


def findfofpascaltriangle(n):
    pascal_traingle_array = get_pascal_traingle_array(n)
    print(pascal_traingle_array)
    sum = 0
    for line in range(1, n+1):
        cur_line = pascal_traingle_array[line-1]
        for i in range(1, len(cur_line)+1):
            sum += (line*cur_line[i-1] + i)
    print("Sum is {}".format(sum))
    value = sum % (10**9 + 7)
    return value


def main():
    n = int(input("Enter number of line:"))
    print(findfofpascaltriangle(n))


if __name__ == '__main__':
    main()
