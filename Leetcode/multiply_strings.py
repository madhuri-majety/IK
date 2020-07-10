"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""
from operator import add

class Multiply(object):
    def multiply_integers(self, s1, s2):
        if not int(s1) or not int(s2):
            print('0')
        len1 = len(s1)
        len2 = len(s2)

        result = [0]*(len1+len2)

        i_s1, i_s2 = 0, 0
        for i in range(len1-1, -1, -1):
            n1 = int(s1[i])
            carry = 0
            i_s2 = 0

            for j in range(len2-1, -1, -1):
                n2 = int(s2[j])
                sum = (n1*n2) + result[i_s1 + i_s2] + carry
                carry = sum/10
                result[i_s1 + i_s2] = sum % 10

                i_s2 += 1

            if carry > 0:
                result[i_s1 + i_s2] += carry

            i_s1 += 1


        for num in range(len(result)-1, -1, -1):
            if result[num] == 0:
                result.pop(num)
            else:
                break

        prod = "".join([str(i) for i in result])
        print(prod[::-1])




def main():
    mul = Multiply()
    mul.multiply_integers('0', '0')

if __name__ == '__main__':
    main()
