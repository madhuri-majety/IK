"""
number = 123456789123456789123456789123456789
sum = 1+2+3+4+5+6+7+8+9+...
if sum > 10 then add all digits of sum
else return the number

"""

def get_sum(num):
    sum = 0
    while num > 0:
        sum += num%10
        num = num//10

    return sum

def generate_sum(num):
    output = get_sum(num)

    while output > 10:
        output = get_sum(output)

    print(output)

def generate_sum_recursive(num):
    if num < 10:
        return num
    else:
        out = get_sum(num)
        generate_sum(out)


def main():
    generate_sum(123456)
    generate_sum(123456789123456789123456789123456789)

    print("\nUsing Recursive function")
    generate_sum_recursive(123456)

if __name__ == '__main__':
    main()

