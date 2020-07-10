"""
Program to print the permutations of a given string
"""

def permute(sofar, rest):
    if len(rest) == 0:
        print(sofar)
    else:
        for i in range(len(rest)):
            next = sofar + rest[i]
            remaining = rest[0:i]+rest[i+1:]
            permute(next,remaining)


def permute_index(chars, op, op_idx):
    if len(chars) == 0:
        print("".join(op[:op_idx]))
    else:
        for i in range(len(chars)):
            op[op_idx] = chars[i]
            new = chars[0:i]+chars[i+1:]
            permute_index(new, op, op_idx+1)


str = input("Enter the string: ")
print("String to Permute is {}".format(str))
permute("",str)
print("\nWith Index Method:\n")
chars = list(str)
op = [None]*len(chars)
permute_index(chars, op, 0)
print("New indexing method")
