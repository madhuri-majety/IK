"""
Hamming weight

We are given a large array of 4-byte integers. We need to write a method that find out how many total bits are turned
on inside such array, Such a digital sum of binary representation of a number, is also called its Hamming weight.

If input arra has two numbers 31 and 51, the answer is nine, because 31 has 5 bits turned on and 51 has 4.

We are looking for  fast solution, even if it take extra memory.

Hint: Think Hash tables

https://stackoverflow.com/questions/8871204/count-number-of-1s-in-binary-representation

https://www.geeksforgeeks.org/program-to-count-number-of-set-bits-in-an-big-array/

"""

def count_set_bits(input_arr):
    result = 0
    for input in input_arr:
        result += str(bin(input)).count('1')

    return result

def count_set_bits_binary_ops(input_arr):
    result = 0
    for input in input_arr:
        result += get_set_bit_count(input)
    return result

def get_set_bit_count(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num & (num-1)
    return count

def main():
    in_arr = [51, 31]
    in_arr1 = [2147483647, 3]

    print(count_set_bits(in_arr1))

    print(count_set_bits_binary_ops(in_arr1))


if __name__ == '__main__':
    main()