"""
Given an integer reverse the integer

124 ===> 421

"""

def reverse_integer(num):
    result = []

    while num > 0:
        (num, left) = divmod(num, 10)
        #print(num, left)
        result.append(left)

    print result
    return int("".join(str(x) for x in result))

def reverse_integer_no_array(num):
    reversed = 0
    while num > 0:
        reversed = reversed*10 + num%10
        num = num/10

    return reversed


print(reverse_integer(124))
print("********************")
print(reverse_integer_no_array(124))
